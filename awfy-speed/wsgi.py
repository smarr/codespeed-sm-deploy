# -*- coding: utf-8 -*-

"""
WSGI config
"""

import os
import sys
import django

codespeed_dir = current_dir = os.path.abspath(os.path.dirname(__file__).replace('\\','/'))

dirs = current_dir.split(os.path.sep)
parent_folder = dirs[-1]
del(dirs[-1])
project_dir = os.path.sep.join(dirs)

sys.path.append(project_dir)
sys.path.append(codespeed_dir)

# os.environ['DJANGO_SETTINGS_MODULE'] = parent_folder + '.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

django.setup()

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

