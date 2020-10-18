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
In the Windows 10 (I use a Powershell 7)
for the the checking Shell Variables use:
```bash
 $Env:data_path
```
For the set variable use:
```bash
$Env:data_path = 'C:\Users\Alex\foxmind\task_7\Data'
```
[Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7)
.

After that you can run flask app:
```bash
flask run
```

For Linux and Mac:

```bash
$ export FLASK_APP=race_table
$ export FLASK_ENV=development
$ flask run
```
For Windows cmd, use set instead of export:
```bash
> set FLASK_APP=race_table
> set FLASK_ENV=development
> flask run
```
For Windows PowerShell, use $env: instead of export:
```bash
> $env:FLASK_APP = "race_table"
> $env:FLASK_ENV = "development"
> flask run
```
