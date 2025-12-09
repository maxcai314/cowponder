rm -rf build dist cowponder.egg-info
python setup.py sdist bdist_wheel
twine upload --repository testpypi dist/*
# do not --skip-existing for testpypi, to allow overwriting existing versions