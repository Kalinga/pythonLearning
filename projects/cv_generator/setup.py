try:
    from setuptools import setup
except ImportError:
    from distutils import setup

config = { 'name':'cv_creator',
           'author':'Kalinga',
           'author_email':'mail.kalinga@gmail.com',
           'version':'1.0',
           'description':'Python Utilities for CV creation',
           'install_requires':['django-pdfkit']
        }

setup(**config)