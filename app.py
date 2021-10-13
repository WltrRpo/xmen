from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.main import main as main_blueprint


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lxUF6sI9UN:D616Y21ss4@remotemysql.com:3306/lxUF6sI9UN'

db = SQLAlchemy()
db.init_app(app)

# db.drop_all()
# db.create_all()

# @app.route("/")
# def index():
#     return """
#         <div>
#             <h1>Welcome!</h1><br>
#             <p>This site was released according to a test related with xmen and MELI.</p>
#         </div>
#     """

app.register_blueprint(main_blueprint)

if __name__ == "__main__":
    app.run()
    # app.run(threaded=True)
