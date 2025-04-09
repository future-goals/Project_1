def authenticate(username, password):
    """
    Authenticate the user with the given username and password.
    Returns True if credentials are valid, otherwise False.
    """
    # Example credentials (replace with a database or secure storage in production)
    valid_username = "admin"
    valid_password = "password"


    return username == valid_username and password == valid_password