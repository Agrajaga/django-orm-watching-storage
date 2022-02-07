# Storage monitoring console

This script uses the Django framework to display data about storage visitors from the sample database.

### How to run

To run the script, type:
```
$ python main.py
```

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
Create a file `.env` and put sample database parameters in it:
```
SC_DJANGO_HOST=<host>
SC_DJANGO_PORT=<port>
SC_DJANGO_NAME=<database_name>
SC_DJANGO_USER=<database_user>
SC_DJANGO_PASSWORD=<database_user_password>
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).