all: pack
	
deps:
	python -m pip install -r requirements.txt --target packages
	
pack:
	python pack.py
	
run:
	PYTHONPATH=packages python app/main.py
