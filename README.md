# Storage monitoring console

This script uses the Django framework to display data about storage visitors from the sample database.

### How to run

To run the script, type:
```
python manage.py runserver 0.0.0.0:8000
```
The server will run on [localhost:8000](http://localhost:8000)

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
Create a file `.env` and put your database parameters in it as database url:
```
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
```
You can turn debug messages on and off with the `DEBUG` option.  

Debug ON:  `DEBUG=true`  
Debug OFF: `DEBUG=false` or omit this option.

Also, the `SECRET_KEY` and `ALLOWED_HOSTS` must be set in the environment parameters.   
`SECRET_KEY='<youre_secret_key>'` - a secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.  
`ALLOWED_HOSTS=127.0.0.1, localhost` - a list of strings representing the host/domain names that this Django site can serve. 


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
