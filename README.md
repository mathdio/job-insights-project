# 💼 Job Insights
A set of analysis solutions for job real data, developed as a [Trybe](https://www.betrybe.com) Project

## 💻 About this project
This application has analysis implementations incorporated to a web job opportunity application developed in Flask. The implemented functions are focused in search and filter of jobs.

Some files have been provided by [Trybe](https://www.betrybe.com) to accelerate the application development start (as the mock files for tests) or in order to be tested.

## 🛠️ Built with
<a href="https://flask.palletsprojects.com/en/2.3.x/" target="_blank" rel="noreferrer"><img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" /></a>
<a href="https://docs.python.org/3/" target="_blank" rel="noreferrer"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" /></a>

## 🎯 Used skills
- Python interactive terminal usage;
- Python conditional statements and loop sctructures usage;
- Python built-in functions usage;
- Exception handling;
- File import and handling;
- Function writing;
- Module writing, export and import;
- Software testing with Pytest.

## 🏁 Getting started
### 🐍 Installing Python 3
You will need Python 3 in order to run the application. You can see how to install it [here](https://wiki.python.org/moin/BeginnersGuide/Download).
Once Python 3 is installed, you can follow the next steps to create a virtual enviroment and install the dependencies in it.

### 🌱 Creating virtual enviroment and installing dependencies
To create the virtual enviroment, run:
```
python3 -m venv .venv
```
To activate the virtual enviroment in a shell enviroment, run:
```
source .venv/bin/activate
```
To deactivate the virtual enviroment, you can simply run the command `deactivate`.

To install the dependencies in virtual enviroment, run:
```
python3 -m pip install -r dev-requirements.txt
```
### 🏃‍♀️ Running the application
In virtual enviroment, run:
```
flask run
```
Now you can access the application front-end layer `http://localhost:5000/jobs` endpoint and use the solutions implemented.

## 🧪 Testing
To execute all tests, in virtual enviroment run:
```
python3 -m pytest
```
If some issue occurs, you can alternatively run `python3 -m pytest -s -vv`.

To execute one specifict test file, you can run the command with the file path. Example:
```
python3 -m pytest tests/file_path/file_name.py
```
To execute one specific test function, you can run the command with the flag `-k` and the function. Example:
```
python3 -m pytest -k function_name
```
