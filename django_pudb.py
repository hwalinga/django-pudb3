# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import sys

from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed
from django.http import Http404

pudb = None  # Silence pyflakes


def err_print(*args, **kwargs):
    print('!! ERROR:', *args, file=sys.stderr, **kwargs)


class PudbMiddleware(object):
    def __init__(self, get_response=None):
        # django >= 1.10
        if get_response:
            self.get_response = get_response

        if not getattr(settings, 'DEBUG', False):
            raise MiddlewareNotUsed

        import sys
        if '--nothreading' not in sys.argv:
            err_print(
                'PudbMiddleware: Threading not (yet) supported, unloading myself.'
            )
            err_print('Please run with runserver --nothreading.')
            raise MiddlewareNotUsed

        try:
            global pudb
            import pudb
            assert pudb  # Silence pyflakes
        except ImportError:
            err_print('PudbMiddleware: Could not import pudb, unloading myself.')
            raise MiddlewareNotUsed

        print('PudbMiddleware: DEBUG enabled and pudb found, intercepting all uncaught exceptions.')

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            return
        print('PudbMiddleware: activating on "{0}"'.format(repr(exception)))
        pudb.post_mortem()
