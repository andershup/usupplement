<h1 align="center">Usupplements<br>
Milestone project 4: e-commerce web application</h1>

## Table of content 
* [**UX**](#ux)   
* [**UI**](#ui)
    * [**Wireframes**](#wireframes)
    * [**Features**](#features)
* [**Colour Scheme**](#colour-schemes)
* [**Technologies used**](#technologies-used)
    * [**languages**](#programming-languages)
    * [**Framesworks, Libraries and tools**](#frameworks-libraries-tools)
    * [**Other**](#other)
* [DATA](#data)
    * [DATA Models](#data-models)
* [Testing](#testing)
* [Deployment](#Deployment)
* [Other](#otherr)

-- ----------

## **UX** 

Usupplement was designed, built and deployed by Anders Olesen as the final project for the diploma in software development. It is an E-Commerce website aimed at people seeking to supplement their healthy lifestyle. The aim is to provide an approachable site where the user can be presented with a clear and easy selection of the full range of vitamin types.

The project utilizes Python 3, Django 2.2, JavaScript, and various other frameworks and libraries. Full CRUD functionality is offered throughout features of the project.

### USER/OWNER STORIES 

|  **As a** | **I want to...** | **so that...** |
| --- | --- | --- |
|  Customer | be able to view a list of products | I can quickly add product to my basket. |
|  Customer | be able to sort products by category | I can easily narrow down search. |
|  Customer | be able to create my own account | I can complete a purchase more easily in the future. |
|  Customer | I want a clear summary of my basket | I can make an informed decision as to whether to commit to purchase. |
|  Customer | I want a clear presentation of products | I can make an informed decision |
|  Customer | I want to feel secure in making a payment | I can make my purchases with confidence. |
|  Customer | I want to be able to freely browse products. | I can inform myself about available products |
|  Customer | I want a website that is easy to navigate. | I can spend the miminum amount of time finding the right product. |

|  **As an** | **I want to...** | **so that...** |
| --- | --- | --- |
|  Owner | be able to create a database of clients | I can expand on repeat business. |
|  Owner | be able to achieve a secure revenue stream | I can maintain and expand my business. |
|  Owner | be able to hold information about my customer securely | the likelyhood of a purchase is maximised. |
|  Owner | be able to add/remove  products to/from my range as a superuser | the likelyhood of a purchase is maximised. |
|  Owner | have an aesthetically pleasing site | the likelyhood of a purchase is maximised. |
|  Owner | have my site and its features accessable on all formats | the likelyhood of a purchase is maximised. |
|  Owner | have the route from arriving on site to purchase be as short and as simple as possible. | the likelyhood of a purchase is maximised. |

## **UI** <a name="ui"></a>

### wireframes 


[Click here](https://github.com/andershup/usupplement/tree/master/wireframes) 

### Features 

* Navbar with the following features:
    * Dropdown menu for mobile view
    * Home button/link 
    * search bar 
    * dropdown category menu
    * account login/sign-up
    * shopping basket
* Clearly displayed product images on a scrollable homepage
* Product images will be links to the option to "add to order".
* Full user authentication system including email confirmations and user profiless.
* Live fully functioning payment system.
* postgres relational database.
* User interaction, with validation, that allow for the creation and editing of models in the backend.
* A blog function that will allow anyone who is signed in as superuser to author a blog.

### ITEMS

## colour schemes 

* ![#313638](https://placehold.it/15/313638/000000?text=+) #313648 - Navbar color
* ![#000000](https://placehold.it/15/000000/000000?text=+) #000000 - Font color
* ![#FFFFFF](https://placehold.it/15/FFFFFF/000000?text=+) #FFFFFF - Font color

## TECHNOLOGIES USED

### Programming Languages

* HTML5 - Structure 
* CSS3 - Styling
* JavaScript - Frontend functionality
* Python - Database backend management


### Frameworks Libraries Tools 

* Bootstrap - Framework to Build the basic structure.
* Django - Python based framework for the full development of the site.
* jQuery.js - JavaScript library for HTML DOM manipulation
* Google Fonts
* Font Awesome - for icons
* Stripe - for payment processing.
* Psycopg2 - a database adaptor for Python
* Gunicorn (green unicorn) - WSGI server implementation for running Python web apps.
* Git/Github - for version control.
* Gitpod - for developed and editing code.
* Heroku - for application deployment.
* Pixabay - for background image.
* W3C Validator - HTML and CSS. 
* PEP8 Validator - Python 
* Balsamiq - for creating wireframes
* AWS S3 - for cloud storage.
* miniwebtool for generating secret key for Django.

### Other 

* Google Fonts
* Font Awesome - Icons
* Git - Version control
* Gitpod - development

## DATA

### Databases

Sqlite3 was used during development. For deployment, data tables and data was migrated to a PostgreSQL database.

### Data models

#### Blog app

Blog models

| **Field** | **Type**       | **Notes**                   |
|:--------- |:-------------- |:----------------------------|
| title     | Charfield      | Blog title                  |
| slug      | SlugField      | urls                        |
| updated_on| DateTimeField  | Auto addition of date       |
| content   | Textfield      | Article body                |
| created_on| DateTimeField  | Auto addition of date       |
| status    | IntegerField   |    default=0                |

#### Products app

Category Model

| **Field**   | **Type**      | **Notes**                   |
|:------------|:--------------|:--------------------------- |
|name         | Charfield     | Programmatic name           |
|friendly_name| Charfield     | Frontend name               |

Product Model

| **Field**  | **Type**      | **Notes**                   |
|:-----------|:--------------|:--------------------------- |
|   category | ForeignKey    | Linked to Category model    |
|    sku     | CharField     | Product identifier          |
|    name    | Charfield     | Product name                |
|  first_sold| DateTimeField | When product first sold     |
|uploaded_by |  Charfield    | Employee name               |
|description |   TextField   | Product description         |
| price      |DecimalField   |  Product price              |
|image       |  ImageField   | Product ImageField          |

Order Model

| Field           | Type      |
| :-------------- | :-------- |
| full_name       | CharField |
| phone_number    | CharField |
| country         | CharField |
| postcode        | CharField |
| town_or_city    | CharField |
| street_address1 | CharField |
| street_address2 | CharField |
| county          | CharField |
| date            | DateField |

OrderLineItem Model

| Field          | Type               |
| :-------       | :----------------- |
| order          | ForeignKey(Order)  |
| product        | ForeignKey(Product)|       |
| quantity       | IntegerField       |
| lineitem_total | DecimalField       |

Profile Model

| Field                    | Type               |
| :-------                 | :----------------- |
|  user                    | OneToOneField      |
|default_street_address1   | CharField          |
|default_street_address1   | CharField          |
|default_town_or_city      | CharField          |
|default_postcode          | CharField          |
|default_country           | CountryField       |
|default_phone_number      | CharField          |

## TESTING

 Google Chrome developer tools was used throughout this project. 

| Code                                                        | Files Tested                                                       | Result |
| :---------------------------------------------------------- | :----------------------------------------------------------------- | :----- |
| CSS ([W3C](https://jigsaw.w3.org/css-validator/))           | style.css                                                          | PASS   |
| HTML ([W3C](https://validator.w3.org/))                     | templates                                                          | PASS   |
| Javascript: no major errors ([jshint](https://jshint.com/)) | dashboard.js, base.js                                              | PASS   |
| Python ([PEP8](https://pep8online.com/))                    | views.py, models.py, forms.py, urls.py, settings.py, test\_\*\*.py | PASS   |

## Manual Testing 

Google Chrome developer tools was used throughout this project to test Desktop, Tablet and Mobile
Testing was done on all major browsers (Chrome, Firefox, Edge and Firefox) 
Tested ok on darkmode of tablet and mobile.

### Home

* All Category links functional
* Only if superuser is logged in does the "Manage Account" and "Create Blog" options show under account in the Navbar
* When logged in shopping basket continues to show total amount after session has been closed and re-opened.
* All links from index.html functional and directed correctly.
* Navbar functional in mobile view with all options and links working.
* Error message showing if search does not return relevant products.

### Products

* Only when signed in as superuser does the edit/delete products appear. Links tested functional.
* Clicking on images connecting to product_details page.

### Product Detail

* Adding product brings up success message with order summary.
* Return to shopping links to home page
* Quantity limited to 10

### Add Product

* Adding product tested fuctional 

### Edit Product

* Tested fuctional 

### Delete Product 

* Tested functional

### Bag 

* Able to remove product
* Total, subtotals and delivery cost correct 
* All links functional

### Checkout 

* When logged in form is prefilled
* Order summary correct
* All links 
* **name not prefilled**

### Profile 

* Shopping cart persisting after user logging out/in.
* Updating profile functional 

## DEPLOYMENT

The project developed and hosted on Gitpod with a live Version on Heroku.

Note: for Cloud9 users prefix the git command with "sudo"

### To deplay this project locally:

Follow this [link](https://github.com/andershup/usupplement) to my Github repository.

Click clone or download

Copy

Create virtual enviroment.
  
  Python 3 needs to be installed on your machine, alongside PIP. 
  
  To allow you to access all functionality on the site locally, ensure you have created free accounts with the following services: - Stripe - AWS and set up an S3 bucket - Gmail.
  
Open Git Bash.

    $ git clone (paste the copied url).
    $ touch requirements.txt
    $ pip3 install -r requirements.txt 
    $ touch env<span></span>.py

 Add your enviroment variables to env<span>.py 
  
(STRIPE_PUBLIC_KEY is added for consistency only)

     import os
     os.environ.("STRIPE_PUBLIC_KEY", "secret key here")
     os.environ.("STRIPE_SECRET_KEY", "secret key here") 
     os.environ.("DATABASE_URL", "secret key here") 
     os.environ.("SECRET_KEY", "secret key here") 
     os.environ.("AWS_ACCESS_KEY_ID", "secret key here") 
     os.environ.("AWS_SECRET_ACCESS_KEY", "secret key here")

   In settings<span></span>.py add your variables.
   
       $ touch .gitignore
       
 Add your env<span></span>.py to .gitignore file.

    $ python3 manage.py makemigrations --dry-run
    $ python3 manage.py migrate --plan 
    $ python3 manage.py migrate 
    $ python3 manage.py makemigrations
    $ python3 manage.py createsuperuser (follow instructions)
    $ python3 manage.py runserver

To run the app

    $python3 manage.py runserver

To login as superuser add /admin to your URL 


### TO deploy to Heroku

 
If the Heroku command line interface is not already installed in your enviroment then use the folow commands:

        $ curl https://cli-assets.heroku.com/install.sh | sh 
        $ heroku login

All instalation instructions available online. 

    $ pip3 install psycopg2 
    $ pip3 insatll gunicorn
    $ pip3 freeze --local > requirements.txt
    
Ensure you are logged in then create your application

    $ heroku app:create <name of your app>

If not in the USA use --region eu (for europe)

    $ heroku apps

Verify your app is in the list.

Heroku has now set up a git repository. we will use this to deploy to Heroku.

To see your remote URLS

    $ git remote -v 

The heroku (push) destination can now be used with the following command

    $ git push heroku master

The origin (push) destination can now be used with the following command

    $ git push origin master

To connect the the database URL go to the Heroku Web UI resources tab and searching "postgres" and select Heroku Postgres

Note: To use MySql select "Clear DB"

Select plan then click "provision"

To verify:

    $ heroku addons 

In order to connect the remote database 

    $ pip3 install dj_database_url

Repeat the command 

    pip3 install freeze --local > requirements.txt

To get your Heroku remote 

    $ heroku config

Copy the DATABASE_URL 

Go to Heroku setting then config vars and add

|   KEY    |    VALUE    
|:------------|:-------------: | 
| DATABASE_URL |  <your_app_database_url>                      
| ALLOWED_HOSTS | https://<your_app_name>.heroku.com 

In setting<span></span>.py 

Comment out the current database settings and add the following below

    DATABASES = {
         'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }

import dj_database_url at the top of setting.<span>.py 

then add

    ALLOWED_HOSTS = os.environ.get('HEROKU_HOSTNAME')]
    SECRET_KEY = os.environ.get('SECRET_KEY')

If there is not one already create a .gitignore file in your enviroment being careful to include the "."

In .gitignore add

    core.Microsoft*
    env.py
    __pycache__/
    *.py[cod]
    *.sqlite3
    *.pyc

If one does not already exist create a Procfile in your envirement being careful to use a capital "P"

In Procfile add 

    web: gunicorn django_todo.wsgi:applicaton

then

    $ python3 manage.py migrate

Then 

    $ git add .
    $ git commit -m "your commit message"
    $ git push origin master
    $ heroku config:set DISABLE_COLLECTSTATIC=1
    $ git push heroku master

In case of any error messages

    $ heroku logs --tail

Go to the Heroku web ui, then deploy tab

Under deployment method select Github (ensure you are logged in) 

Search for your repo name and click "Connect"

Click "Enable automatic Deploys"

From this point on all "git push" commands will automatically deploy to Heroku

In Amazon AWS/S3 create bucket
    
    $ pip3 install django-storages
    $ pip3 insatll boto3
    $ touch custom_storage.py
    $ python3 manage.py collect static.

-- ---------

## NOTES

## ATTRIBUTION 
 
All text from example blogs were copied from [Vitaminbuddy.co.uk](https://www.vitaminbuddy.co.uk/)

## DISCLAIMER

All content is for educational purposes only. 

## ACKNOWLEDGEMENTS

Tutor support at Code Institute 

Brian Macharia - My mentor

Stack Overflow

YouTube

Me :-)
