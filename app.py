from flask import Flask, render_template


app = Flask(__name__)
@app.route("/")
def index():
    return """
        <div>
            <h1>Welcome!</h1><br>
            <p>This site was released according to a test.</p>
        </div>
    """


if __name__ == "__main__":
    app.run()
