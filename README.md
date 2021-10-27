# Project 8 : Créez une plateforme pour amateurs de Nutella

This website was devloped as part of coding learning with Open Classroom.
The website 

It works with data from OpenFoodFacts API : https://wiki.openfoodfacts.org/API
and it was devloped with Django : https://docs.djangoproject.com/en/3.2/
## Installation
- Install python : https://www.python.org/downloads/
- Install pipenv :  
``pip install --user pipenv``
### Pull
``git clone https://github.com/Nicolasdvl/P8``
### Create virtual environment
``pipenv install``
### Create a database
This app configure django to use a PostgreSQL database.
Get started with PostgreSQL here : https://www.postgresql.org/docs/current/tutorial-start.html
You also can configure django to use an other database : https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-DATABASES

### Create file .env
Create a file name ".env" at the project root.  
Write the next line in the file with your information :  
``DATABASE_PASSWORD = <YOUR DATABASE PASSWORD>``
``DJANGO_KEY = <YOUR DJANGOKEY>``
``BROWSER_LOCATION = <PATH TO YOUR BROWSER>``
``DRIVER_PATH = <PATH TO YOUR SELENIUM DRIVER>``
More informations on selenium drivers : https://selenium-python.readthedocs.io/installation.html
## Usage
### Use the virtual environment 
``pipenv shell``  
### Use the command
Insert the data :
``python manage.py insert_data``

Delete the data : 
``python manage.py delete_data``

Launch the local host:
``python manage.py runserver``
## Tests
### Fixtures
Users: authentification/fixtures/test_users.json
Products: products/fixtures/test_products.json
Categories: products/fixtures/test_categories.json
### Launch tests
All the tests are in 'test' folder.
``python manage.py test test``
## Deployment
The next steps explain how deploy the application on heroku.  
### Install heroku
 https://devcenter.heroku.com/articles/heroku-cli#download-and-install  
### Log in to heroku CLI  
``heroku login``  
### Deploy the app  
``heroku create``  
``git push heroku main``
### Procfile
The procfile is already define on the git depo.
### Config var
Config vars in settings of the heroku app : https://devcenter.heroku.com/articles/config-vars