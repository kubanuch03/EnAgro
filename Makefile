.PHONY: install migrate createsuperuser runserver # make install


install:
	pip install -r requirement.txt
 
migrate:
	python manage.py makemigrations
	python manage.py migrate
 
createsuperuser:
	python manage.py createsuperuser
 
runserver:
	python manage.py runserver