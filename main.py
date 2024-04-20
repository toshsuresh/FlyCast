from app import create_app
from app.model import load_and_train

app = create_app()

# Ensure the model is trained and saved before starting the app
load_and_train()

if __name__ == '__main__':
    app.run(debug=True)