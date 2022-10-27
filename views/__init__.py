from .animal_requests import (
delete_animal,
get_all_animals,
get_single_animal,
create_animal,
update_animal,
get_animals_by_location_id,
get_animals_by_status
)
from .customer_requests import (
  create_customer,
  get_single_customer,
  get_all_customers,
  delete_customer,
  get_customers_by_email,
  update_customer
)
from .location_requests import (
  get_single_location,
  get_all_locations,
  create_location,
  delete_location,
  update_location
)
from .employee_requests import(
  get_single_employee,
  get_all_employees,create_employee,
  delete_employee,
  get_employees_by_location_id,
  update_employee
)
