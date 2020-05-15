import os
from flask import Flask
from extensions import database, commands

app = Flask(__name__)
# setup with the configuration provided by the user / environment
app.config.from_object(os.environ['APP_SETTINGS'])

# setup all our dependencies
database.init_app(app)
commands.init_app(app)

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run()
