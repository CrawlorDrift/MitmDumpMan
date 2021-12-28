.PYTHON: dump

dump:
	supervisord -c supervisord.conf


push:
	git add -A
	git commit -am "commit"
	git push