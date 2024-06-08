import webbrowser
from threading import Timer
from app import create_app
from app.model import load_and_train

app = create_app()

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    load_and_train()  # Ensure this is called
    # Set a timer to open the browser
    Timer(1, open_browser).start()
    app.run(debug=True)
