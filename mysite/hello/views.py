from django.shortcuts import render
from django.http import HttpResponse


def myview(request):
    # Cookie handling
    print(request.COOKIES)
    oldval = request.COOKIES.get('zap', None)
    resp = HttpResponse('')  # Create an initial response object
    if oldval:
        resp.set_cookie('zap', int(oldval) + 1)  # Increment zap cookie value
    else:
        resp.set_cookie('zap', 42)  # Set zap cookie to 42 if not present

    # Set dj4e_cookie
    resp.set_cookie('dj4e_cookie', '6a54d83b', max_age=1000)

    # Session handling
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4:
        del(request.session['num_visits'])

    # Construct the response content
    response_content = f'In a view - the zap cookie value is {str(oldval)}<br>view count={str(num_visits)}'
    resp.content = response_content

    return resp
