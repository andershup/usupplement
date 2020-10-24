<h1 align="center">Usupplements<br>
Milestone project 4: e-commerce web application</h1>

## UX

## USER/OWNER STORIES

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

### UI

See wireframes. 

## FEATURES

### Will do:
* Navbar with the following features:
    * Dropdown menu for mobile view
    * Home button/link 
    * search bar 
    * dropdown category menu
    * account login/sign-up
    * shopping basket
    * possible checkput button
* Clearly displayed product images on a scrollable homepage
* Product images will be links to the option to "add to order".
* Full user authentication system including email confirmations and user profiless.
* Live fully functioning payment system.
* postgres relational database.
* User interaction, with validation, that allow for the creation and editing of models in the backend.
 


### Stretch goals:
* Special offers in Navbar (buy two, get one free etc)
* Product size options.
* Sort selection by rating/price etc.
* Company Logo.
* Full Stock Check for all products and sizes.
* Bootstrap toasts messages. 
* Google sign-in option.
* Connected company instagram account. 
* A “return to top” button is the product list becomes extensive enough.
* A nootropics product range added.

## DATA
### ITEMS
### MODELS

## colour schemes

## TECHNOLOGIES USED

### Programming Languages

* HTML5 - Structure 
* CSS3 - Styling
* JavaScript - Frontend functionality
* Python - Database backend management

### Frameworks, Libraries and tools used

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

### Databases

* PostgreSQL 
* Sqlite3 - backup and early development database

### Other 

* Google Fonts
* Font Awesome - Icons
* Git and Gitpod - development and version control


## TESTING

* Google Chrome developer tools was used throughout this project. 


## DEPLOYMENT

The project developed and hosted on Gitpod with a live Version on Heroku.

To deplay this project locally:

  1. Follow this [link](https://github.com/andershup/usupplement) to my Github repository.
  2. Click clone or download
  3. Copy
  4. Create virtual enviroment.
  5. Open Git Bash.
  6. $ git clone (paste the copied url).
  7. $ touch requirements.txt
  8. $ pip3 install -r requirements.txt (use sudo pip for cloud9)
  9. $ touch env<span></span>.py
  10. Add your enviroment variables. 
  
      (STRIPE_PUBLIC_KEY is added for consistency only)

     import os
     os.environ.("STRIPE_PUBLIC_KEY", "secret key here")
     os.environ.("STRIPE_SECRET_KEY", "secret key here") 
     os.environ.("DATABASE_URL", "secret key here") 
     os.environ.("SECRET_KEY", "secret key here") 
     os.environ.("AWS_ACCESS_KEY_ID", "secret key here") 
     os.environ.("AWS_SECRET_ACCESS_KEY", "secret key here")

   11. In settings<span></span>.py add your variables.
   12. $ touch .gitignore
   13. Add your env<span></span>.py to .gitignore file.
   14. $ python3 manage<span></span>.py makemigrations --dry-run
   15. $ python3 manage<span></span>.py makemigrations
   16. $ python3 manage<span></span>.py migrate --plan 
   17. $ python3 manage<span></span>.py migrate 
   18. $ python3 manage<span></span>.py createsuperuser (follow instructions)
   19. $ python3 manage<span></span>.py runserver
   20. To login as superuser add /admin to your URL 


-- ----------






TO deploy to Heroku
1. Create a new heroku project, set the env vars as listed above
2. In Heroku/deploy, link your enviroment.
3. From settings copy the value of the DATABASE_URL and add to your env<span></span>.py
   
   Note, your config vars in Heroku/settings should be set as follows

|   KEY    |    VALUE    
|:------------|:-------------:
| AWS_ACCESS_KEY_ID | *your key here*
| AWS_SECRET_ACCESS_KEY | *your key here*
| DATABASE_URL |   *your key here*                 |                |
| STRIPE_PUBLIC_KEY | *your key here*
| STRIPE_SECRET_KEY | *your key here*
| STRIPE_WH_SECRET | *your key here*
| DISABLE_COLLECTSTATIC | *your key here* 

4. Create a Procfile in your enviroment containing: gunicorn django_app.wsgi:application
5. $ pip3 install dj_database_url (sudo pip for Cloud9)
6. $ pip3 install psycopg2 (sudo pip for Cloud9)
7. $ pip3 freeze > requirements.txt
8. $ python3 manage<span></span>.py makemigrations --dry-run
9. $ python3 manage<span></span>.py makemigrations
10. $ python3 manage<span></span>.py migrate --plan 
11. $ python3 manage<span></span>.py migrate 
12. $ python3 manage<span></span>.py createsuperuser (follow instructions)
13. $ python3 manage<span></span>.py createsuperuser
14. $ In Amazon AWS/S3 create bucket
15. $ pip3 install django-storages 
16. $ pip3 insatll boto3
17. $ touch custom_storage.py (populate is in cloned enviroment)
18. $ python3 manage<span></span>.py collect static. 
19. (TO BE COMPLETED)



### NOTES
Stripe js script included in the base template to allow all fraud detection feature to work throughout the project.

## ATTRIBUTION 

(TO BE COMPLETED)
The basic framework of settings.py copied from django

## DISCLAIMER

All content is for educational purposes only. 

## ACKNOWLEDGEMENTS

Tutor support at Code Institute 

Brian Macharia - My mentor

Stack Overflow

YouTube

Me :-)
