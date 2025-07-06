from flask import Flask
from routes import routes
from db import create_items_table

app = Flask(__name__)
app.register_blueprint(routes)

create_items_table()

if __name__ == "__main__":
    app.run(debug=True)
