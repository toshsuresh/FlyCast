from app import create_app
from app.model import load_and_train

app = create_app()

if __name__ == '__main__':
    load_and_train()  # Ensure this is called
    app.run(debug=True)
