import webbrowser
from threading import Timer
from app import create_app
from app.model import load_and_train

app = create_app()

if __name__ == '__main__':
    load_and_train()  # Ensure this is called
    # Set a timer to open the browser
    app.run(debug=True)
