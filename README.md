# Web report of Monaco 2018 Racing

Simple web application which uses Flask framework.

## Getting Started

This application is created with pipenv usage.
Also file ```.env``` was added.
This file contains variables ```FLASK_APP``` and ```DATA_PATH```. 
You need to change variable ```DATA_PATH``` according to your operation system.
More information of Shell Variables you can find 
[here](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/).

So for the starters you need to launch pipenv:
```bash
pipenv install
pipenv shell
```  

## Usage

```bash
flask run
```
Open the HTML link in the terminal to get the access to the program.
On the HTML page you can use either Hyperlinks or following addresses:

```
http://localhost:5000/report
http://localhost:5000/report/drivers/
http://localhost:5000/report/drivers/?driver_id=SVF
http://localhost:5000/report/drivers/?order=desc     
```  

## Running the tests

To run the tests you need to install ```develop``` packages:
```bash
pipenv install --dev
```
After that to run the tests you must write:
```bash 
pytest
coverage -m pytest
```
 