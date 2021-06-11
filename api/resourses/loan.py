from api.models.client import ClientModel
from api.models.loan import LoanModel
from api import Resource, abort, app
from flask import request
from api.schemas.loan import loan_schema


class LoanResource(Resource):

    @app.validate("loan", "loan")
    def post(self, client_id):
        try:
            client = ClientModel.query.get(client_id)
            if not client:
                return f"No client with id={client_id}"
            loan = LoanModel(client_id=client.id, **request.json)
            loan.save()
        except Exception as e:
            return {"message": str(e)}, 400
        return loan_schema.dump(loan), 201

    def delete(self, client_id, loan_id):
        try:
            client = ClientModel.query.get(client_id)
            if not client:
                return f"No client with id={client_id}"
            loan = LoanModel.query.get(loan_id)
            if not loan:
                return f"Client with id={client_id} has no loan with {loan_id}"
            loan.delete()
        except Exception as e:
            return {"message": str(e)}, 400
        return f"Loan with id={loan_id} by client with id={client_id} deleted", 200
