install_deps:
	pip install -r requirements.txt

run_dev_server:
	flask --app app --debug run

run_prod_server:
	gunicorn app:app
