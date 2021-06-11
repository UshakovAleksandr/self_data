import jsonschema
from api import app, Response


@app.errorhandler(jsonschema.ValidationError)
def validation_error(e):
    return Response("Validation error: " + str(e), 400)
