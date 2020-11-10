# dokkanz

SetUp the project:

Run this commands:

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

python manage.py createsuperuser

Open this link at browser  http://127.0.0.1:8000/admin/  to create Categories and Products

Then you can check the ( products, categories ) data from this endpoints:

 http://127.0.0.1:8000/api/v1/categories/
  http://127.0.0.1:8000/api/v1/products/
