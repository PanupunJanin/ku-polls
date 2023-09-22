[![Unit tests](https://github.com/PanupunJanin/ku-polls/actions/workflows/django.yml/badge.svg)](https://github.com/PanupunJanin/ku-polls/actions/workflows/django.yml)

# Web Polls for Kasetsart University

An application for conducting a poll or survey with multiple-choice questions, written in Python using Django. It is based on the [Django tutorial project][django-tutorial], and adds additional functionality.

A polls application for [Individual Software Process](https://cpske.github.io/ISP) course at [Kasetsart University](https://ku.ac.th).

## Requirements

Requires Python 3.8 or newer.  Required Python packages are listed in [requirements.txt](./requirements.txt). 

## Install and Running the Application

Firstly, clone this repository using this command in your terminal to your selected directory.
```
git clone https://github.com/PanupunJanin/ku-polls.git
```

Then, you need to install all the dependencies in the [virtual environment](https://docs.python.org/3/library/venv.html)
with these simple steps:

1. Create your own virtual environment:
   ```
   python -m venv venv
   ```
2. Activate created virtual environment:
   ```
   venv\Scripts\activate
   ```
3. Install dependencies to that virtual environment from requirements.txt:
   ```
   pip install -r requirements.txt
   ```

Lastly, run the server locally to run this web application using this command:
```
python manage.py runserver
```
When the server is running successfully, you can visit 
<http://localhost:8000> to see the application.

To stop the server, press CTRL-C in the terminal window. Exit the virtual environment by closing the window or by typing:
   ```
   deactivate
   ```

For more detailed steps, you can go and visit 
[Guide to installation of this application](./Installation.md)


## Demo User Accounts

| Username | Password |
|----------|----------|
| harry    | h477y123 |
| potter   | p011e722 |


## Project Documents

All project-related documents are in the [Project Wiki](https://github.com/PanupunJanin/ku-polls/wiki)

- [Vision Statement](https://github.com/PanupunJanin/ku-polls/wiki/Vision-Statement)
- [Requirements](https://github.com/PanupunJanin/ku-polls/wiki/Requirements)
- [Development Plan](https://github.com/PanupunJanin/ku-polls/wiki/Development-Plan)
- [Iteration 1 Plan](https://github.com/PanupunJanin/ku-polls/wiki/Iteration-1-Plan) and [Task Board](https://github.com/users/PanupunJanin/projects/1)
- [Iteration 2 Plan](https://github.com/PanupunJanin/ku-polls/wiki/Iteration-2-Plan) and [Task Board](https://github.com/users/PanupunJanin/projects/2)
- [Iteration 3 Plan](https://github.com/PanupunJanin/ku-polls/wiki/Iteration-3-Plan) and [Task Board](https://github.com/users/PanupunJanin/projects/3)
- [Iteration 4 Plan](https://github.com/PanupunJanin/ku-polls/wiki/Iteration-4-Plan) and [Task Board](https://github.com/users/PanupunJanin/projects/4)

[django-tutorial]: https://docs.djangoproject.com/en/3.1/intro/tutorial01/
