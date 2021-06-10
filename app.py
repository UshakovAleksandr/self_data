from api import app, api
from config import Config
from api.resourses.loan import LoanResource
from api.resourses.client import ClientResourceList, ClientResource, ClientResponseResource

api.add_resource(ClientResourceList, "/client")
api.add_resource(ClientResource, "/client/<int:client_id>")
api.add_resource(LoanResource, "/client/<int:client_id>/loan", "/client/<int:client_id>/loan/<int:loan_id>")
api.add_resource(ClientResponseResource, "/self_bki/request")

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, host="0.0.0.0")
