install_dependencies:
	pip install -r requirements.txt

run_unit_tests:
	pytest

build_server:
	docker image build -t benvelie-backend .

run_dev_server:
	docker run -p 5000:5000 -d benvelie-backend
