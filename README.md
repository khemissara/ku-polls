# Online Polls for Kasetsart University

An application for conducting a poll or survey, written in Python using Django. It is based on the [Django Tutorial project](https://docs.djangoproject.com/en/4.1/intro/tutorial01/), with additional functionality.

This application is part of the Individual Software Process course at Kasetsart University.

How to Install and Run
--
1. Clone this project repository to your machine.
```
git clone https://github.com/khemissara/ku-polls.git
```
2. Get into the directory of this repository.
```
cd ku-polls
```
3. Create a virtual environment.
```
python -m venv venv
```
4. Activate the virtual environment.
```
. env/bin/activate
```
5. Install all required packages.
```pip install -r requirements.txt```
Create .env file in ku-polls
```
SECRET_KEY = 'django-insecure-)u=f_#17(&3%@q&1w@3c6f!^8ctf59(id3g2)%mkz*2b6-&$00'
DEBUG = True
TIME_ZONE = UTC
ALLOWED_HOSTS = localhost,127.0.0.1
```
6. Run this command to migrate the database and load the data.
```
python manage.py migrate
python manage.py loaddate data/*.json
```
7. Start running the server by this command.
```
python manage.py runserver
   ```

Project Documents
--
All project documents are in the [Project Wiki](https://github.com/khemissara/ku-polls/wiki)

[Vision Statement](https://github.com/khemissara/ku-polls/wiki/Vision-Statement)

[Requirements](https://github.com/khemissara/ku-polls/wiki/Requirement)

[Project Plan](https://github.com/khemissara/ku-polls/wiki/Software-Development-Plan)

[Iteration 1 Plan and Task Board](https://github.com/users/khemissara/projects/1/views/1)

[Iteration 2 Plan and Task Board](https://github.com/users/khemissara/projects/1/views/3)

[Iteration 3 Plan and Task Board](https://github.com/users/khemissara/projects/1/views/6)

| Username  | Password  |
|-----------|-----------|
|   username1   | password112345 |
|   username2   | password212345 |

[Iteration 4 Plan and Task Board](https://github.com/users/khemissara/projects/1/views/8?layout=board&filterQuery=iteration%3A4)
