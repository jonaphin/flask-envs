"""
Flask-Env
---------

Environment tools and configuration for Flask applications.
This package is built on top of its original "Flask Environments" package
which is not maintained any longer.
Flask-Env was built to make it easy for developers to use Flask Environments
in Python 3

Resources
`````````

- `Documentation <http://packages.python.org/Flask-Env/>`_
- `Issue Tracker <http://github.com/mattupstate/flask-environments/issues>`_
- `Code <http://github.com/mattupstate/flask-environments/>`_
- `Development Version
  <http://github.com/mattupstate/flask-environments/zipball/develop#egg=Flask-RQ-dev>`_

"""
from setuptools import setup

setup(
    name='Flask-Env',
    version='0.1',
    url='http://packages.python.org/flask-env/',
    license='MIT',
    author='Jonathan Lancar',
    author_email='jonaphin@gmail.com',
    orginal_author="Matthew Wright",
    description='Environment tools and configuration for Flask applications',
    long_description=__doc__,
    py_modules=['flask_env'],
    zip_safe=False,
    platforms='any',
    install_requires=['Flask', 'pyyaml'],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
