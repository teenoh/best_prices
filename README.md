# Best Prices 🔥🔥
## Description
Price monitoring tool

## Technologies
- Django >= 2.1
- Django Rest Framework
- Sqlite3(dev), Postgresql(production)
- Scrapy
- requests

## Setup Instructions
1. You need to have pipenv installed to continue with this. Pipenv can be installed with 
`pip install pipenv`

2. move into the cloned repository. Create a `.env` file and copy the content of `.env.example` into it.
 `touch .env && cp .env.example .env` (you might need to use a different set of commands to achieve this on windows)

3. Activate the virtualenvironment shell
`pipenv shell`

4. Install the necessary dependencies by running 
`pipenv install` 
(*Note* if you are on windows, you have to install scrapy manually first before running this command)

4. Run the necessary migrations and apply to the db that django will create
`python manage.py migrate`

5. Create a superuser to access the admin interface
`python manage.py createsuperuser`

4. Startup the server with `python manage.py runserver`

5. Open up `http://localhost:8000/` and login into the admin interface

6. Run the crawler to get items from jumia and update the db
`python manage.py run_crawler` (Note: 1. Your server has to still be running, so run this command in another tab.  2. Make sure your virtualenvironment is active)

7. Check your admin interface to see the scraped items