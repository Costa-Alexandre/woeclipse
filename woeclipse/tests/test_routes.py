

def test_index_get(test_client):
    # mimic a browser: 'GET /', as if you visit the site
    response = test_client.get('/')

    # check that the HTTP response is a success
    assert response.status_code == 200

    # Store the contents of the html response in a local variable.
    # This should be a string with the same content as the file index.html
    html_content = response.data.decode()

    assert "<html>" in html_content
    assert "Warriors of Eclipse" in html_content
    assert '<header>' in html_content
    assert '<footer>' in html_content

def test_index_post(test_client):
    # mimic a browser: 'GET /', as if you visit the site
    response = test_client.post('/')

    # check that the HTTP por method is not allowed
    assert response.status_code == 405

    # Store the contents of the html response in a local variable.
    # This should be a string with the same content as the file index.html
    html_content = response.data.decode()

    assert "Warriors of Eclipse" not in html_content

def test_signup_post(test_client):
    # mimic a browser: 'GET /', as if you visit the site
    response = test_client.post('/signup')

    # check that the HTTP response is a success
    assert response.status_code == 200

    # Store the contents of the html response in a local variable.
    # This should be a string with the same content as the file index.html
    html_content = response.data.decode()

    assert "<h1>Signup</h1>" in html_content

def test_signup_get(test_client):
    # mimic a browser: 'GET /', as if you visit the site
    response = test_client.get('/signup')

    # check that the HTTP response is a success
    assert response.status_code == 200

    # Store the contents of the html response in a local variable.
    # This should be a string with the same content as the file index.html
    html_content = response.data.decode()

    assert "<h1>Signup</h1>" in html_content

def test_signin_post(test_client):
    # mimic a browser: 'GET /', as if you visit the site
    response = test_client.post('/signin')

    # check that the HTTP response is a success
    assert response.status_code == 200

    # Store the contents of the html response in a local variable.
    # This should be a string with the same content as the file index.html
    html_content = response.data.decode()

    assert "</form>" in html_content

def test_signin_get(test_client):
    # mimic a browser: 'GET /', as if you visit the site
    response = test_client.get('/signin')

    # check that the HTTP response is a success
    assert response.status_code == 200

    # Store the contents of the html response in a local variable.
    # This should be a string with the same content as the file index.html
    html_content = response.data.decode()

    assert "</form>" in html_content

def test_edit_profile(test_client):
    # mimic a browser: 'GET /', as if you visit the site
    response = test_client.get('/edit_profile')

    # check that the HTTP response is a success
    assert response.status_code == 302

    # Store the contents of the html response in a local variable.
    # This should be a string with the same content as the file index.html
    html_content = response.data.decode()

    assert "Redirecting..." in html_content
