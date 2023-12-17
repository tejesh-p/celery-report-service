# run_server.py

from waitress import serve

from app.app import app  # Adjust the import path based on your project structure


def run():
    print("serving i guess")
    # Run the Flask app with Waitress
    serve(app, listen='*:5000')


if __name__ == "__main__":
    run()
