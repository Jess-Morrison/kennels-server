import sqlite3
import json
from models import Customer

CUSTOMERS= [{"customer": "Kad Mine",
            "id": 4,
            "address": "244 Highway",
            "email": "kadmeni@gmail.com",
            "password" : "log me in"}]



def create_customer(customer):
    """CREATE"""
    # Get the id value of the last animal in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
    """DELETE"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM customer
        WHERE id = ?
        """, (id, ))

def get_single_customer(id):
    """GET SINGLE"""
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer


def get_all_customers():
    """GET ALL"""
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        """)

        # Initialize an empty list to hold all animal representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            customer = Customer(row['id'], row['name'], row['address'],row['email'],row['password'])

            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers)


def get_customers_by_email(email):
    """GET BY EMAIL"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'],
                                row['address'],
                                row['email'] ,
                                row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)

def update_customer(id, new_customer):
    """UPDATE"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Customer
            SET
                id = ?,
                name = ?,
                address = ?,
                email = ?,
                password = ?
        WHERE id = ?
        """, (new_customer['id'], new_customer['name'],
              new_customer['address'], new_customer['email'],
              new_customer['password'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
