def check_grade(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    # Handle both JSON and URL-encoded form data
    request_json = request.get_json(silent=True)
    request_args = request.args
 
    number = None
    if request_args and 'number' in request_args:
        number = request_args['number']
    elif request_json and 'number' in request_json:
        number = request_json['number']
    if number is None:
        return 'Please enter your grade.'
    try:
        number = int(number)
    except ValueError:
        return 'enter a correct value.'
    if number < 0:
        return 'enter a correct value.'
    elif number > 100:
        return 'enter a correct value'
    elif number >= 90:
        return 'A'
    elif number >= 80:
        return 'B'
    elif number >= 70:
        return 'C'
    elif number >= 60:
        return 'D'
    elif number >= 50:
        return 'E'
    else:
        return 'F
