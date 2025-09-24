# Wagtail
my trial project from fourlanes

## Steps to run.
* download the code as a zip from the repository
* extract the file and open the extracted file.
* right click on the fourlanes_trial folder and open with terminal.
* to avoid errors it'd be better to delete the enc folder in the directory which is the virtual environment I created.
* now on the terminal, we create our new virtual environment: python -m venv env
* then we activate it with the prompt .\env\Scripts\activate
* now we install packages that we need, first; pip install django, then; pip install wagtail
* we now change directory with the prompt; cd fourlanes_trial
* enter the prompt; python manage.py runserver
* once the server is running, go to your browser and enter the url: http://127.0.0.1:8000/admin/
* you'll be led to the wagtail admin login page, use the credentials username: timothy and password: admin
* 
