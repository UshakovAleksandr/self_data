from api import db
from api.models.client import ClientModel


class LoanModel(db.Model):
    __tablename__ = 'loans'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey(ClientModel.id))
    payment_rest = db.Column(db.Integer, unique=False)
    payment_rep_month = db.Column(db.Integer, unique=False)
    loans_active = db.Column(db.Boolean(), default=True, nullable=False)
    loan_delinquency = db.Column(db.Boolean(), default=False, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
