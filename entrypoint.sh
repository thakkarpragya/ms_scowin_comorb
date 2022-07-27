#!/bin/bash


python manage.py runserver 0.0.0.0:8086 &
python consumer.py