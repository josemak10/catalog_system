<h1 align="center">Catalog System</h1>


<em>About</em>

It is a Catalog System that manages products, these products have basic information such as sku, name, price and brand.

In this system, we need to have at least two type of users: (i) admins to create / update / delete products and to create / update / delete other admins; and (ii) anonymous users who can only retrieve products information but can't make changes.


<em>Getting Started</em>

Below are the instructions that the system requires to terminate the service.


<em>Prerequesites</em>

You need to create a virtualenv

python -m venv env


<em>Install</em>

Install requirements

pip install -r requirements.py


<em>Deployment</em>

uvicorn main:app


<em>Running to test</em>

pytest


<em>Built</em>

FastApi  Server

Pytest  Testing