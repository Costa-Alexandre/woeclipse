from woeclipse.website import create_app  # noqa: F401


app = create_app()
# # Run the server
if __name__ == "__main__":
    app.run(debug=True)
