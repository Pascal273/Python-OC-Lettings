## Summary

Orange County Lettings Website

## Local development

### Prerequisites

- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher

In the rest of the local development documentation, it is assumed the command `python` in 
your OS shell runs the above Python interpreter (unless a virtual environment is activated).

### macOS / Linux

#### Clone the repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings.git`

#### Create the virtual environment

- `cd /path/to/Python-OC-Lettings`
- `python -m venv venv`
- `apt-get install python3-venv` (If previous step errors with package not found on Ubuntu)
- Activate the environment `source venv/bin/activate`
- Confirm the command `python` now runs the Python interpreter in the virtual environment,
`which python`
- Confirm the version of the Python interpreter is 3.6 or higher `python --version`
- Confirm the command `pip` runs the pip executable in the virtual environment, `which pip`
- To deactivate the environment, `deactivate`

#### Run the site

- `cd /path/to/Python-OC-Lettings`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Go to `http://localhost:8000` in a browser.
- Confirm the site is running and can be navigated (you should see several profiles and lettings).

#### Linting

- `cd /path/to/Python-OC-Lettings`
- `source venv/bin/activate`
- `flake8`

#### Unit tests

- `cd /path/to/Python-OC-Lettings`
- `source venv/bin/activate`
- `pytest`

#### Database

- `cd /path/to/Python-OC-Lettings`
- Open a shell session `sqlite3`
- Connect to the database `.open oc-lettings-site.sqlite3`
- Display tables in the database `.tables`
- Display columns in the profiles table, `pragma table_info(Python-OC-Lettings_profile);`
- Run a query on the profiles table, `select user_id, favorite_city from
  Python-OC-Lettings_profile where favorite_city like 'B%';`
- `.quit` to exit

#### Admin panel

- Go to `http://localhost:8000/admin`
- Login with user `admin`, password `Abc1234!`

### Windows

Using PowerShell, as above except:

- To activate the virtual environment, `.\venv\Scripts\Activate.ps1` 
- Replace `which <my-command>` with `(Get-Command <my-command>).Path`

## Deployment

### How the deployment works

This application is configured to be connected to a circleci pipeline.

Everytime a code change is pushed to the git repository on any branch, it triggers a build and test job that is configured to:
- build an image of that application inside a container
- run a flake8 check
- run a set of unittests

Only changes to the master branch will additionally trigger:
- A containerization job that will:
  - Only execute after the test job was successful!
  - Build a docker image of that application inside a container
  - Push that image to the dockerhub repository

- A Deployment job that will:
  - Only execute after the containerization was a success!
  - Push and deploy that docker image to heroku.

### Required configuration

#### SECRET_KEY

The Django secret key is used to provide cryptographic signing.
This key is mostly used to sign session cookies. If one were to have this key, 
they would be able to modify the cookies sent by the application.

Generate secret key for the application:
- You can visit https://djecrety.ir/ to generate a secret key.
- Or use the get_random_secret_key() function present in django.core.management.utils:
  - to do that run: `python manage.py shell` or and enter the following lines:
    ```
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
    ```
- Copy and save the generated secret key!

#### Accounts for the following platforms:

1. A Github account with a repo in which this application was cloned to.


2. A Docker account, to push the container image to.


3. A Sentry account to log uncaught errors and crashes of the application:

  - After log in, go to `Projects` and click `Create Project`
  - Select the platform: <b>DJANGO</b>
  - Setup your default alert settings
  - Enter a Project name
  - Click on `Create Project`
  - copy and save the value of the <b>dsn</b> variable > without quotation marks!

4. A Heroku account for deployment:

- Environment:
  - After log in, click on `new` > `create a new app`
  - Inside that app click on `Settings` > `Reveal Config Vars`
  - Add the following <b>KEY | VALUE</b> pairs:
    - SECRET_KEY | -your generated secret key-
    - SENTRY_DSN | -your sentry dsn-


- If you don't have an API Key for heroku already, generate your HEROKU_API_KEY:
  - click on `Account` > `Account Settings`
  - inside the account tab scroll down to API Key
  - click on `Generate API Key`
  

5. A Circleci account to that connects to the git repo of this project:
- Inside your project go to: `Project Settings` > `Environment Variables`
- click on `Add Environment Variable`
- add the following <b>KEY | VALUE</b> pairs to your environment:
  - DOCKER_LOGIN | -your docker profile name-
  - DOCKER_PASSWORD | -your docker password-
  - DOCKER_REPO | -your docker repository-
  - HEROKU_API_KEY | -your heroku api key-
  - HEROKU_APP_NAME | -your heroku app name-


<details>
<summary><b>You can Deploy it to Heroku on one click to check it out</b></summary><br>
The fastest way to deploy and test the application on Heroku is by clicking the following link:<br>

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Pascal273/Python-OC-Lettings)

Log into your heroku account, enter a name for the application and click deploy.<br>
All the required environment variables will be taken from this repo automatically.<br>
After the process is completed you will be able to visit and test the web application.
</details>

