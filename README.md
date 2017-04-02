# Installation Instructions 

### Prerequisites
python3  
pip

### Create a virtual environment and install python dependencies
```
python3 -m venv ~/.virtualenvs/flask-api-boilerplate
source ~/.virtualenvs/flask-api-boilerplate/bin/activate
pip install -r requirements.txt
```

### Run unittests
`python -m unittest discover`

### Run the app
Make sure venv is started (`source ~/.virtualenvs/flask-api-boilerplate/bin/activate`)  
```
python manage.py
```


### Swagger Documentation
Swagger json can be found at http://localhost:8000/swagger  
Swagger UI can be found at http://localhost:8000/swagger-ui
