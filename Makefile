install_dependencies:
	pip install --requirement requirements.txt

run_unit_tests:
	pytest

build_dev_server:
	docker image build --tag benvelie-backend --file Dockerfile.dev .

run_dev_server:
	docker run --publish 5000:5000 --detach benvelie-backend
