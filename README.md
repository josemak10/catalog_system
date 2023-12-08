<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Catalog System</h3>


---


## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Test](#tests)
- [Usage](#usage)
- [Built Using](#built_using)

## 🧐 About <a name = "about"></a>

It is a Catalog System that manages products, these products have basic information such as sku, name, price and brand.

In this system, we need to have at least two type of users: (i) admins to create / update / delete products and to create / update / delete other admins; and (ii) anonymous users who can only retrieve products information but can't make changes.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

You need to create a virtualenv.

```
python -m venv env
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
pip install -r requirements.py
```


End with an example of getting some data out of the system or using it for a little demo.

## 🔧 Running the tests <a name = "tests"></a>

Running to test.

```
pytest
```

## 🎈 Usage <a name="usage"></a>

The system has endpoints that allow users to be created, updated and deleted, in the same way for products. Each endpoint mentioned is sent the administrator user parameter which allows access to them.

A user with id=1 is configured in the system, this will allow access to all the endpoints requested by the user.

When the product information is updated, the system will send a notification email to all users.

## 🚀 Deployment <a name = "deployment"></a>

```
uvicorn main:app
```

## ⛏️ Built Using <a name = "built_using"></a>

- [FastAPI](https://fastapi.tiangolo.com/) - Server Framework
- [PyTest](https://pytest.org) - Testing
