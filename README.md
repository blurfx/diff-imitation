# diff

A tiny clone of unix `diff`

## Installation

Install requirements
```sh
pip install -r requirements.txt
```


Install as a package (for user)
```sh
python setup.py build
python setup.py install
```

## Run unit tests

Run unit tests with `pytest`
```
pytest -v
```

## Run demo application

First, Install package (see **Installation** section above)
```bash

# make sure you are in "exmaple" directory
cd example

# demo application requires "colored" package for colored output
pip install -r requirements.txt  

python app.py [file_path1] [file_path2]

# e.g.
# python app.py original.txt changed.txt
```