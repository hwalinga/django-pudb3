django-pudb
===========

Django middleware to view exceptions in PuDB <https://github.com/hwalinga/django-pudb3>

What is this
------------

This is Django middleware that will intercept exceptions and puts you in PuDB.

Note that you can already use PuDB with Django without this using `import pudb; pu.db`
or by running `pudb3 manage.py runserver` (however the latter is a bit clumsy). This piece of middleware is purely to intercept exceptions.

Installing
----------

NB. You should have PuDB installed already.

1. `pip install django-pudb3`
2. In your ``settings.py``:
   - Add ``'django_pudb.PudbMiddleware'`` at/near the end of your ``MIDDLEWARE_CLASSES``
   - Set ``DEBUG_PROPAGATE_EXCEPTIONS = True``
3. Run ``./manage.py runserver --nothreading``

Now you should see PuDB pop up in your console window whenever a view 
raises an exception.

Notes
-----

- This package has zero requirements on purpose, so that you can install it 
  (system|user)-wide, and still get to install Django in your virtualenvs.
- As PuDB doesn't support threading (yet, hopefully), django-pudb doesn't either.

Changelog
---------

0.2.0 (2020-10-23)

- Updated to work with newer versions of Django and Python.

0.1.0 (2014-05-06)

- Initial version.
  Just the middleware; zero magic.

Supports
--------

Minimal Django version is 1.10.

Despite the name, also still works in Python2.7 last time I checked.

Original project
----------------

This is an updated version of https://github.com/akanouras/django-pudb

Licence (MIT)
-------------

Copyright (C) 2014 Antonis Kanouras <antonis@metadosis.eu> Hielke Walinga <hielkewalinga@gmail.com>


Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the "Software"), to deal 
in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in 
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
IN THE SOFTWARE.
