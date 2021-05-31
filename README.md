# TodoApiDjango

Klónozd le/Töltsd le és csomagold ki
Lépj be a mappájába
Hozz létre virtuális környezetet
```
python -m venv .
```
Telepítsd a Django-t
```
pip install django
```
Telepítsd a DjangoRestFramework-öt
```
pip install djangorestframework
```
Lépj be a backend mappába, és végezz migrate-t (ez létrehozza az adatbázist)
```
python manage.py migrate
```
Ellenőrizd hogy működik-e
```
python manage.py runserver
```
Majd menj el az URL-re (alap esetben):
127.0.0.1:8000/api/
