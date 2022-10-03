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

<details>
<summary><b>Deploy directly to Heroku on one click</b></summary><br>
The fastest way to deploy and test the application on Heroku is by clicking the following link:<br>

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Pascal273/Python-OC-Lettings)

Log into your heroku account, enter a name for the application and click deploy.<br>
All the required environment variables will be taken from this repo automatically.<br>
After the process is completed you will be able to visit and test the web application.
</details>

<details>
<summary><b>Deploy the app from your system to Heroku</b></summary><br>
<ul>
  <li>
    If you haven't already, log in to your Heroku account typing <code>heroku login</code>
  </li>
  <li>
    Create a new app on either using the web UI (to pick an available name) <br>
    or typing <code>heroku create</code> (wich will create the app with a random name)
  </li>
  <li>
    Add the SECRET_KEY environment variable using web UI:<br>
    app > Settings > Config Vars > Reveal Config Vars > Add <br>
    KEY: <code>SECRET_KEY</code> VALUE: <code>SOME_SECRET_VALUE</code><br>
    Or using cli: <code>heroku config:set SECRET_KEY=SOME_SECRET_VALUE -a HEROKU_APP_NAME</code>
  </li>
  <li>
    Open the cli and navigate to the Python-OC-Lettings folder<br>
  </li>
  <li>
    Initialize a git repository in a new or existing directory:<br>
    <ul>
      <li>initialize git: <code>git init</code></li>
      <li>add heroku remote: <code>heroku git:remote -a HEROKU_APP_NAME</code></li>
    </ul>
  </li>
  <li>
    Commit your code to the repository and deploy it to Heroku using Git:
    <ul>
      <li>add files: <code>git add .</code></li>
      <li>commit added files: <code>git commit -am "commit message"</code></li>
      <li>deploy on heroku: <code>git push heroku master</code></li>
    </ul>
  </li>
</ul>

</details>
