# DRF Assignment for Intern @ RiDiv Technologies

## Problem Statmemt

✅ Create a single url Django and Django Rest Framework (DRF) application.

✅ Create a single url  `/invoices/` for this

- `/invoices/`
- `/invoices/<int:pk>/`

✅ Create two Django models

- **Invoice** -> date, customerName.
- **Invoice Detail** -> invoice (ForeignKey), description, quantity, unit_price, price.

✅ Create APIs using DRF for all the HTTP methods for the invoice models. 

❎ Create test cases to test all the API endpoints. 

## Dependencies

- Python3
- Django (pip-module)
- Django Rest Framework (pip-module)

## Run/Deploy

- On Debian/Ubuntu Linux Environment
  ``` bash
  # Install Git and Python
  sudo apt install git python3 -y

  # Install Django and DRF
  pip install django
  pip install djangorestframework

  # Clone Repo
  git clone https://github.com/thekarananand/RiDiv_tech_assignment.git

  # Migration
  cd RiDiv_tech_assignment
  python3 manage.py makemigrations
  python3 manage.py migrate

  # Run Server
  python3 manage.py runserver
  ```

- On Other Environments
  1. Download Python 3, and Setup it up as an Enviroment Variable
  2. Download Django and DRF via python3-pip
    ```
    pip install django
    pip install djangorestframework
    ```
  3. Download the Code of this Repo and Extract it.
  4. Open CMD/Powershell/Terminal in code directory of the Code. Run the following commands
    ```
      # Migration
    cd RiDiv_tech_assignment
    python3 manage.py makemigrations
    python3 manage.py migrate
  
    # Run Server
    python3 manage.py runserver
    ```
