all: pack
	
deps:
	-rm -rf packages
	python -m pip install -r requirements.txt --target packages
	
zip:
	python pack.py

pyz:
	echo '#!/usr/bin/python3' > exe.pyz
	cat exe.zip >> exe.pyz
	chmod +x exe.pyz

pack: zip pyz
	@du -h exe.*
	
run:
	PYTHONPATH=packages python app/main.py

ec2-test: ec2-zip ec2-pyz

ec2-zip:
	scp exe.zip ec2-user@ec2-bots: 
	ssh ec2-bots python3 ./exe.zip
	ssh ec2-bots rm ./exe.zip

ec2-pyz:
	scp exe.pyz ec2-user@ec2-bots: 
	ssh ec2-bots ./exe.pyz
	ssh ec2-bots rm ./exe.pyz

ec2-zip:

clean:
	-rm *.pyz *.zip
