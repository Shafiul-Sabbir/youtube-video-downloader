# python3 -m venv env
# source env/bin/activate

pip install -r requirements.txt
python3 manage.py collectstatic --no-input

# deactivate