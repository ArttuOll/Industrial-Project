# Industrial-Project
UEF Industrial Project 2022 course Group 2 repository


## The database :
* MySQL database 
* Setting it up for your project :
    * if not already done, install MySQL and create a user : https://www.mysql.com/ 
    * connect to your MySQL in a command prompt : ``` mysql -u user -p ``` You can add ``` -P number ``` if the port MySQL is using isn't the default one (3306). The system will ask for your password.
    * create a database for the project : ``` CREATE DATABASE db_name ;```
    * connect to that database : ``` USE db_name ; ```
    * if you don't have one already, create a .env file at the root of the project and add it to the .gitignore file
    * add the following lines and change the values to match the configuration of the database you created :
        ```
        DATABASE_NAME=db_name
        DATABASE_USER=user
        DATABASE_PASS=mysupersecurepassword
        DATABASE_PORT=number
        ```
    * in your prompt/terminal, execute the following commands :
        ```
        python manage.py makemigrations 
        python manage.py migrate
        ```