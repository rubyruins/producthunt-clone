Producthunt Clone 🛍
============

[![](https://img.shields.io/badge/Made_with-Python3-orange?style=for-the-badge&logo=python)]()
[![](https://img.shields.io/badge/Made_with-django-orange?style=for-the-badge&logo=django)]()
[![](https://img.shields.io/badge/deployed_on-heroku-orange?style=for-the-badge&logo=heroku)]()

A simple clone based on Producthunt made using Django and Bootstrap. It allows users to create or login to their account, create new products and upvote the existing ones.

Visit it [here.](https://product-hunt-python.herokuapp.com/)

---

## Features:

- Create accounts using Django's built-in User model
- Add and view existing products
- Vote for your favourite ones
- Homepage features a random product picked from the featured list
- Search, filter and sort through all existing products

---

## Deployment:

The live project is deployed on https://product-hunt-python.herokuapp.com/. 

---

## Local installation:

**You must have Python 3.6 or higher to run the file.**

- Create a new virtual environment for running the application. You can follow the instructions [here.](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)
- Navigate to the virtual environment and activate it.
- Install the dependancies using `pip install -r requirements.txt`
- Run the app file with `python manage.py runserver`