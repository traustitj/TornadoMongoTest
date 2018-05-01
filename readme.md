Please add virtualenv

virtualenv env

Windows :
env\scripts\activate.bat

Linux:
source env/bin/activate

Then run

pip install -r requirements.txt

to run

python Webserver/Webserver/server --port=8000 --debug=1