from flask import Blueprint


main = Blueprint('main', __name__)

@main.route("/", methods=['GET'])
def index():
    return """
        <div>
            <h1>Welcome!</h1><br>
            <p>This site was released according to a test related with xmen and MELI.</p>
        </div>
    """