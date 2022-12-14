# DTEK Schedule based on Django app

## Description

Django app to notify user via SMS about DTEK schedule using Twilio SMS.
For Scheduling the message using Django, I use django-celery with redis as the backend.

### Technologies

- Python3
- Django
- Redis
- Celery
- Twilio

#### INSTALL

```shell
mkdir django_schedule

cd django_schedule
```

#### Linux

```shell 
python3 -m venv .venv source .venv/bin/activate
```

#### Mac OS
```shell
python3 -m venv .venv source .venv/bin/activate
```
#### Windows
```shell
py -3 -m venv .venv .venv\scripts\activate
```
#### Installing all dependecies from requirements.txt
```shell
pip install -r requirements.txt
```

You will need data like the Account SID, Auth Token and Twilio numbers to interact with the Twilio API.
These environment variables should be kept private, so you should not put their values in the code.
Instead, you can store them in a .env file.
A .env file can be used whenever there are environment variables you need to make available to your operating system.

Next, open the .env file in your favorite text editor and add the following lines, replacing the random string placeholder values with your values:

```env
TWILIO_ACCOUNT_SID = YOUR TWILIO ACCOUNT SID
TWILIO_TOKEN = YOUR TWILIO ACCOUNT TOKEN
TWILIO_NUMBER = YOUR TWILIO NUMBER
RECEIVER_NUMBER = NUMBER YOU WANT TO SEND SMS TO
```

_For the phone numbers above, make sure you have entered them in E.164 format._
