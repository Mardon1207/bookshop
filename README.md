# bookshop

## API docs

cutomer table

1. create customer - `api/v1/customers/`
2. delete customer by pk - `api/v1/customers/{id}/`
3. update customer by pk - `api/v1/customers/{id}/`
4. get customer by pk - `api/v1/customers/{id}/`
5. get customers - `api/v1/customers/`

contact table

1. create customer's contact - `api/v1/customers/{id}/contact/`
2. delete customer's contact - `api/v1/customers/{id}/contact/`
3. update customer's contact - `api/v1/customers/{id}/contact/`
4. get customer's contact - `api/v1/customers/{id}/contact/`

## Database schema

customer

- id
- first_name
- last_name
- username
- password

contact

- id
- customer_id
- email
- address
- phone

publisher

- id
- name
- description

language

- id
- lang

book

- id
- title
- description
- price
- quantity
- isbn
- languege FK
- pages
- publisher FK
- published_date 