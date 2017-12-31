""" http://flask.pocoo.org/snippets/53/ """

from flask import g


def teardown_after_this_request(func):
    """
    Usage:
    >>> def invalidate_username_cache():
    >>> @teardown_after_this_request
    >>> def delete_username_cookie(response):
    >>>     response.delete_cookie('username')
    >>>     return response
    :param func:
    :return:
    """
    if not hasattr(g, 'teardown_after_request'):
        g.teardown_after_request = []
    g.teardown_after_request.append(func)
    return func
# end def


# @app.after_request  # use load_teardown_after_this_request(app)
def per_request_teardowns(response):
    for func in getattr(g, 'teardown_after_request', ()):
        response = func(response)
    return response
# end def


def load_teardown_after_this_request(app):
    app.teardown_request(per_request_teardowns)
    app.teardown_after_this_request = teardown_after_this_request
    return app
# end def
