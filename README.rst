North Bay Python
=================

The website for North Bay Python is a Django application with Symposion and Registrasion.

Setup
-----

Development
~~~~~~~~~~~
1. pip install -r requirements/base.txt
2. python manage.py migrate
3. python manage.py createsuperuser
4. python manage.py loaddata fixtures/*

Prod
~~~~
Use `pip install -r requirements.txt` instead.

Reference Material
------------------

* Registrasion docs are at http://registrasion.readthedocs.io
* Symposion docs are at http://symposion.readthedocs.io
