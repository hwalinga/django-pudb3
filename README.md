# NOTA BENE

The old django-pudb you find in pip is old and broken. I edited it so that
it works on new versions of Python and Django. If you want to use this:

```bash
git clone https://github.com/hwalinga/django-pudb3
cd django-pudb3
pip install -e .
```


django-pudb
===========

Old project this derives from: <https://github.com/akanouras/django-pudb>

Installing
----------

1. Install as per above.
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

0.1.0 (2014-05-06)

- Initial version.
  Just the middleware; zero magic.

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
