# Task 7 - Web report of Monaco 2018 Racing

```bash
pipenv install
pipenv shell

export FLASK_APP=monaco_table.py
export DATA_PATH=/home/alex/foxminded/task_7/Data
```
In this project was added file ```.env``` contains that variables. 

So everything from the command line should work without manual export.

In the PyCharm may be need add this variables manually to the ```Settings>Terminal>Environment Variables``` in the format: 
```FLASK_APP=monaco_table.py;DATA_PATH=/home/alex/foxminded/task_7/Data```

For the checking Shell Variables use:
```bash
printenv FLASK_APP
printenv DATA_PATH
```



After that you can run flask app:
```bash
flask run
```