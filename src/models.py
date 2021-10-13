from . import db

class DNA_test(db.Model):
    test_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    test_code = db.Column(db.String(255), primary_key=True)
    test_result = db.Column(db.Boolean, default=False)

    def __init__(self, test_code, test_result):
        self.test_code = test_code
        self.test_result = test_result
