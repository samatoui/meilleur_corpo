.PHONY: requirements migrate_database

requirements:
	pip3 install --upgrade -r config/requirements.txt

migrate_database:
	python3 manage_api.py makemigrations meilleur_corpo
	python3 manage_api.py migrate
	python3 manage_api.py migrate_estate_adverts data/dataset_annonces.csv


