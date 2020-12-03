pip3 install virtualenv
python -m venv myvenv
myvenv\Scripts\activate
pip3 install -r requirements.txt
cd webkaproject
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb
python manage.py runserver
