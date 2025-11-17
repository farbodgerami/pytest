pytest .

### more specific:
pytest ./gist/test_gist.py -v

 
### run with a specific mark:
pytest ./gist/test_gist.py -v -p no:warnings -m slow

### exclude a specific mark:
pytest ./gist/test_gist.py -v -p no:warnings -m "not slow"


pytest ./gist/test_gist.py -v -p no:warnings -s