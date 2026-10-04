# microservice-que

A small bookstore built as microservices with Django, from a PTIT microservices assignment (see `tutorial_assigment-05_assignment-06.pdf`). The code lives in `bookstore-microservice/`.

## Features

- `book-service`: REST API to list and create books (title, author, price, stock).
- `customer-service`: customer model (name, unique email) with its own API.
- `cart-service`: carts per customer, cart items (book id and quantity), and an endpoint to view a customer's cart.
- `api-gateway`: Django app with server-rendered pages that call the other services over HTTP: `/books/` and `/cart/<customer_id>/`.
- Each service has its own Dockerfile and its own SQLite database; services reference each other by id only.

## Tech stack

- Python 3.11, Django, Django REST Framework
- Docker and Docker Compose

## Getting started

```bash
cd bookstore-microservice
docker compose up --build
```

Host ports: gateway 8010, customer-service 8011, book-service 8012, cart-service 8013. Each container runs `manage.py migrate` before starting the dev server.
