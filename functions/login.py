
def login (username, password):
    if username == 'admin' and password == 'password':
        authorised = True
    else:
        authorised = False

    return authorised
