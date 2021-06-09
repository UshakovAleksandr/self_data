from api import ma
from api.models.loan import LoanModel


class LoanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LoanModel


loan_schema = LoanSchema()
loan_schemas = LoanSchema(many=True)
