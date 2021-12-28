.PYTHON: dump

dump:
	 mitmdump -s DumpMan/script.py -p 8888


push:
	git add -A
	git commit -am "commit"
	git push