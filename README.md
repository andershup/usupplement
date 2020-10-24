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

### Frameworks

* Bootstrap - Framework.
* Django - Python framework.

### Libraries

* jQuery.js

### Databases

* PostgreSQL 
* Sqlite3 - backup and early development database

### Other 

* Google Fonts
* Font Awesome - Icons
* Git and Gitpod - development and version control


### TESTING
dpaste.com 
choose category showing on all pages

### DEPLOYMENT
To deplay this project locally:
* Clone the repository (or use git pull)
* Create your virtual enviroment
* Create "requirements.txt" file
* pip3 install -r requirements.txt (use sudo pip3 with Cloud9)
* create a  file.
* Add the above file to your .gitignore 
* Set:
    * os.environ["STRIPE_WH_SECRET"] = ""
    * os.environ["STRIPE_PUBLIC_KEY"] = "" - (added for consistancy)
    * os.environ["STRIPE_SECRET_KEY] = ""


The project developed and hosted on Gitpod with a live Version on Heroku.

TO deploy to Heroku
* Create a new heroku project, set the env vars as listed above
* In Heroku/deploy link your enviroment.
* Create a Procfile in your enviroment containing: gunicorn django_app.wsgi:application


### NOTES
Stripe js script included in the base template to allow all fraud detection feature to work throughout the project.

## ATTRIBUTION 
The basic framework of settings.py copied from django 
All content is for educational purposes only. 

## ACKNOWLEDGEMENTS

Tutor support at Code Institute 

Brian Macharia - My mentor

Stack Overflow

YouTube

Me :-)
