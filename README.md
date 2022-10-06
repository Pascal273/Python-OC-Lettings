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

Changes to the master branch also trigger a containerization job that will:
- Build a docker image of that application inside a container
- Push that image to the dockerhub repository

As well as a Deployment job that will:
- 

<details>
<summary><b>Deploy directly to Heroku on one click</b></summary><br>
The fastest way to deploy and test the application on Heroku is by clicking the following link:<br>

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Pascal273/Python-OC-Lettings)

Log into your heroku account, enter a name for the application and click deploy.<br>
All the required environment variables will be taken from this repo automatically.<br>
After the process is completed you will be able to visit and test the web application.
</details>

