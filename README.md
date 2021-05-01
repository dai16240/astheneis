![logo](static/img/icon.png)
# Astheneis (Ασθενείς)

#### Simple Patients Management App

Astheneis (Ασθενείς) is an application that keeps track of patients' data, such as name, phone number etc.
Built with Flask/Python.

See it live [here](https://astheneis.herokuapp.com).

*Due to Heroku's ephemeral file system, any changes made to the sqlite database, are not being stored.

## Installation

Astheneis requires [Python](https://www.python.org/) 3 to run.
- Create a virtual environment.
- Install the dependencies from _requirements.txt_ and run the application using gunicorn.

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
gunicorn main:app
```