# Installation
This file contains the instructions about installing this application.

## Clone this repository
Firstly, clone this repository using this command in your terminal to your selected directory.
```
git clone https://github.com/PanupunJanin/ku-polls.git
```

## Create a virtual environment
1. Create a virtual environment in your directory by executing this command:
   * For Windows:
      ```
      python -m venv \[path]\
      # Example: python -m venv env
      ```
   * For MacOS:
      ```
      python3 -m venv /[path]/
      ```
   
2. Activate the virtual environment by executing this command:
    * For Windows:
        ```
        [path]\Scripts\activate
        # for example: env\Scripts\activate
        ```
    * For MacOS:
        ```
        /[path]/bin/activate
        ```
## Installing the dependencies
   Install everything inside `requirements.txt` file into the created virtual environment.
   * For Windows:
      ```
      pip install -r requirements.txt
      ```
   * For MacOS:
      ```
      pip3 install -r requirements.txt
      ```

More details about virtual environment :
* [Offcial Python Document](https://docs.python.org/3/library/venv.html)
* [For Linux](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)

## Set values for environment variables
    
All the essential externalized variables have this structure which are provided in [sample.env](sample.env)
```
SECRET_KEY=secret-key-value
DEBUG=False
ALLOWED_HOSTS='*.ku.th, localhost, 127.0.0.1, ::1, testserver'
TIME_ZONE=Asia/Bangkok
```

## Run migrations to set up the database

* For Windows
    ```
    python manage.py migrate
    ```
* For MacOS
    ```
    python3 manage.py migrate
    ```
    
## Install data from the existed database
Install all provided polls data which include questions, choices, and users.
* To install polls data
    ```
    python manage.py loaddata data/polls.json
    ```
* To install user data
    ```
    python manage.py loaddata data/users.json
    ```