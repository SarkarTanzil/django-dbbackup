#!/usr/bin/env python

import os
import sys
import django
from django.conf import settings

here = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(here)
sys.path[0:0] = [here, parent]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'tests/media')
INSTALLED_APPS = (
    'testapp',
    'dbbackup',
)


settings.configure(
    MEDIA_ROOT=MEDIA_ROOT,
    MIDDLEWARE_CLASSES=(),
    # CACHES={'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}},
    INSTALLED_APPS=INSTALLED_APPS,
    DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}},
    ROOT_URLCONF='testapp.urls',
    SECRET_KEY="it's a secret to everyone",
    SITE_ID=1,
)


def main():
    if django.VERSION >= (1, 7):
        django.setup()
    from django.test.runner import DiscoverRunner
    runner = DiscoverRunner(failfast=True, verbosity=int(os.environ.get('DJANGO_DEBUG', 1)))
    failures = runner.run_tests(['dbbackup'], interactive=True)
    sys.exit(failures)

if __name__ == '__main__':
    main()
