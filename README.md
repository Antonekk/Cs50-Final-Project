# Cs50-Final-Project
My final project for Cs50: Web Programming with Python and JavaScript

## Distinctiveness and Complexity:
This project was very challanging for me. For the first time, I created a project completely from scratch and by myself.
When creating Pollapp, I used almost everything I learned during the course, and even more. 
In the project, in addition to the previously known python, django, javascript, html, css, I also used: Django REST framework which helped me create an API, Bulma which helped me make the website look good and Chart.js which helped me make graphs for polls

## What’s contained in each file:

#### - views.py: all the backend logic behind rendering templates
#### - urls.py: all the paths on the website
#### - serializers.py: converting database results to json responce
#### - models.py: is where all the sql django models are
#### - templates folder : there are all the html files that Pollapp uses
#### - static folder : there are all the .js and .css and images files that are use within Pollapp
#### - Rest of the files are just basic, unchanged django files that are create while starting django project

## How to run Pollapp on your device

#### 1. Clone Pollapp github repository
#### 2. After opening it with your terminal use this command: "cd final"
#### 3. Next run "python manage.py runserver"
#### 4. Open your browser and go to "http://127.0.0.1:8000" and you sould be able to use Pollapp
##### If you want to use admin panel you can run this command: "python manage.py createsuperuser" 

## Tools used while creating Pollapp

#### - Python | Used as backend programming language
#### - Django | Python based framework I used to create backend for Pollapp
###### -     Django REST framework | Used to create Pollapp API's 
#### - Javascript | Used to create frontend features
###### -     Charts.js | Used to create pie charts of number of votes each option had in poll
#### - HTML | Standard markup language for Web pages
#### - CSS | Used to style HTML
###### -     Bulma | Used to make frontend design look good
###### -     Fontawesome | Used to get access to many icons