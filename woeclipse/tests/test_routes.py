

def test_index_fixture(test_client):
    # mimic a browser: 'GET /', as if you visit the site
    response = test_client.get('/')

    # check that the HTTP response is a success
    assert response.status_code == 200

    # Store the contents of the html response in a local variable.
    # This should be a string with the same content as the file index.html
    html_content = response.data.decode()

    assert "<html>" in html_content
