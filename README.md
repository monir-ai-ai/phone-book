# Phonebook

Phonebook is a Django application that allows users to store and manage their contacts. Users can create, update, delete, and search for contacts using this API.

## Features

•  Contacts are stored in a SQLite database using Django models and serializers.

•  Contacts have the following fields: first name, last name, phone number, address, and email.

•  Users can perform (create, update, delete) operations on contacts.

•  Users can search for contacts by any field using a query parameter or by specifying multiple parameters

•  Users can view the JSON response of the API using tool like Postman


## Installation

To install Phonebook, you need to have Python 3 and Django 4.2 installed on your system. You can use pip to install Django:


pip install django==4.2


Then, you need to clone this repository or download the zip file and extract it. Navigate to the project directory and run the following commands to set up the database and start the server:


python manage.py makemigrations
python manage.py migrate
python manage.py runserver


The server will run on http://127.0.0.1:8000/ by default. You can access the web interface by visiting http://127.0.0.1:8000/phonebook/

## Usage

To use the API, you can send HTTP requests to the following endpoints:

•  post http://127.0.0.1:8000/phonebook/insert/ to create a new contact. You need to provide the contact data in JSON format in the request body. For example:

{
"first_name": "Ali",
"last_name": "Elahi",
"phone_number": "012345678922",
"address": "123 moshir Street",
"email": "ali@gmail.com"
}


•  PUT http://127.0.0.1:8000/phonebook/update/<pk>/ to update an existing contact. You need to provide the contact ID in the URL and the updated data in JSON format in the request body. You can use the partial=True option to update only some fields. For example:



{
"phone_number": "0987654321",
"email": "Aliali@gmail.com"
}


•  DELETE PUT http://127.0.0.1:8000/phonebook/delete/<pk>/ to delete an existing contact. You need to provide the contact ID in the URL.


•  GET PUT http://127.0.0.1:8000/phonebook/search/ to get a list of all contacts. You can also use a query parameter to search for contacts by any field. For example:



http://127.0.0.1:8000/phonebook/search/?query=Ali
http://127.0.0.1:8000/phonebook/search/?param1=Ali&param2=Elahi


You can use a web browser or a tool like Postman to view the JSON response of the API.