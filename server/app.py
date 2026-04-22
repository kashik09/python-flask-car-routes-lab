from flask import Flask

app = Flask(__name__)

existing_models = ["Corolla", "Civic", "Mustang", "Model S", "Camry", "Accord"]


@app.route('/')
def index():
    return "Welcome to Flatiron Cars"


@app.route('/<model>')
def get_model(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    return f"No models called {model} exists in our catalog"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
