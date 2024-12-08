# main/context_processors.py

def example_context(request):
    """
    Example context processor that adds some data to the template context.
    """
    return {
        'example_variable': 'This is an example context variable',
        'user_is_authenticated': request.user.is_authenticated,
    }
