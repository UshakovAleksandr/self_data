from api import ma
from api.models.client import ClientModel
from api.schemas.loan import LoanSchema


class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ClientModel

    loans = ma.Nested(LoanSchema(many=True))


client_schema = ClientSchema()
client_schemas = ClientSchema(many=True)
