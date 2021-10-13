from flask import Flask, jsonify, request, Response
from flask_sqlalchemy import SQLAlchemy
from dna import dna_check


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lxUF6sI9UN:D616Y21ss4@remotemysql.com:3306/lxUF6sI9UN'

db = SQLAlchemy()
db.init_app(app)

# db.drop_all()
# db.create_all()

class DNA_test(db.Model):
    test_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    test_code = db.Column(db.String(255), primary_key=True)
    test_result = db.Column(db.Boolean, default=False)

    def __init__(self, test_code, test_result):
        self.test_code = test_code
        self.test_result = test_result


def DNA_insert_sample(code, result):
    try:
        new_row = DNA_test(str(code), result)
        db.session.add(new_row)
        db.session.commit()
    except:
        pass


@app.route("/", methods=['GET'])
def index():
    return """
        <div>
            <h1>Welcome!</h1><br>
            <p>This site was released according to a test related with xmen and MELI.</p>
            <p>V2</p>
        </div>
    """


@app.route('/stats/', methods=['GET'])
def stats():
    try:
        count_mutant = DNA_test.query.filter_by(test_result=1).count()
        count_human = DNA_test.query.filter_by(test_result=0).count()
        ratio = count_mutant / (0 if count_human + count_mutant == 0 else count_human + count_mutant)
    except:
        count_mutant = 0
        count_human = 0
        ratio = 0
    return jsonify({'count_mutant_dna':count_mutant, 'count_human_dna': count_human, 'ratio':ratio})


@app.route('/mutant/', methods=['POST'])
def mutant():
    try:
        dna_code = request.get_json(force=True)['dna']
        dna_result = dna_check(dna_code)
        DNA_insert_sample(dna_code, dna_result)
        if dna_result:
            return Response(status=200)
        else:
            return Response(status=403)
    except:
        return Response(status=403)

if __name__ == "__main__":
    # app.run()
    app.run(threaded=True)
