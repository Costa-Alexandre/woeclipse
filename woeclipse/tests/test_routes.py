# from woeclipse.website import create_app
# import pytest

# @pytest.fixture(scope='module')
# def test_client():
#     app = create_app()

#     # Create a test client using the Flask application configured for testing
#     with app.test_client() as testing_client:
#         # Establish an application context
#         with app.app_context():
#             yield testing_client  # this is where the testing happens!

# def test_index():
#     app = create_app()
    
#     # create a version of our website that we can use for testing
#     with app.test_client() as test_client:
#         # mimic a browser: 'GET /', as if you visit the site
#         response = test_client.get('/')

#         # check that the HTTP response is a success
#         assert response.status_code == 200

#         # Store the contents of the html response in a local variable.
#         # This should be a string with the same content as the file index.html
#         html_content = response.data.decode()

#         assert "<html>" in html_content

# def test_index_fixture(test_client):
#     # mimic a browser: 'GET /', as if you visit the site
#     response = test_client.get('/')

#     # check that the HTTP response is a success
#     assert response.status_code == 200

#     # Store the contents of the html response in a local variable.
#     # This should be a string with the same content as the file index.html
#     html_content = response.data.decode()

#     assert "<html>" in html_content
