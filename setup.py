try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Wordcount',
    'author': 'Prez Cannady',
    'url': 'https://github.com/OCExercise/wordcount-python34',
    'download_url': 'https://github.com/OCExercise/wordcount-python34/archive/master.zip',
    'author_email': 'revprez@opencorrelate.org',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['wordcount'],
    'scripts': [],
    'name': 'wordcount'
}

setup(**config)