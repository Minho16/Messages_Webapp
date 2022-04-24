# Messages_Webapp

This is a web application where both users and non-users can see other users' messages and upload in case of registered ones.


## (1) Home Page
![alt text](https://github.com/Minho16/Messages_Webapp/blob/main/image1.PNG?raw=true)

## (2) Registration Page
![alt text](https://github.com/Minho16/Messages_Webapp/blob/main/image2.PNG?raw=true)

## (3) User Page (when visiting user's page as owner) 
![alt text](https://github.com/Minho16/Messages_Webapp/blob/main/image3.PNG?raw=true)

## (4) User Page (when visiting other user's page)
![alt text](https://github.com/Minho16/Messages_Webapp/blob/main/image4.PNG?raw=true)

# How to setup

## 1. Select a folder where you want to clone the code

## 2. Clone the code https://github.com/Minho16/Messages_Webapp.git

  ```sh
  git clone https://github.com/Minho16/Messages_Webapp.git
  ```

## 3. Set virtualenv in the same directory and activate it

```sh
  virtualenv env
  ```

```sh
  cd env/Scripts
  ```

```sh
  . activate
  ```

## 4. Install Django 

```sh
  pip install django
  ```

## 5. Go to the directory "your folder"/Messages_Webapp/prueba_tecnica and run server (a directory where "manage.py" is located)

```sh
  python manage.py runserver
  ```


## 6. Now the app is already running at localhost (ex: 127.0.0.1:8000)

You can access to other pages by clicking buttons or through the following urls:

Home page => 127.0.0.1:8000/
Register	=> 127.0.0.1:8000/register
Login		  => 127.0.0.1:8000/login
Logout		=> 127.0.0.1:8000/logout
User page => 127.0.0.1:8000/user/<username>
  

# Need to be improved: 

1. MessageSaveForm => Not saving data correctly even applying cleaned_data
	=> I had to save the Message manually with the class Message

2. userid and username => how to reduce

3. tests.py => It would be nice to have unit tests (future)

