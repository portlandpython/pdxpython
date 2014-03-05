#!/bin/bash

source development.env
django-admin.py runserver --settings=settings.development --pythonpath=pdxpython
