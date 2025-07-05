from flask_openapi3 import OpenAPI, Info

from flask_cors import CORS

info = Info(title="Sprint 1 API", version="1.0.0")
app = OpenAPI(__name__, info=info)

CORS(app)

