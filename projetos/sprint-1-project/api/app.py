from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_cors import CORS

info = Info(title="Sprint 1 API", version="1.0.0")
app = OpenAPI(__name__, info=info)

CORS(app)

openapi_documentation_tag = Tag(name="Projeto Sprint 1", description="Documentação da API do projeto Sprint 1")

@app.get('/', tags=[openapi_documentation_tag])
def home():
    return redirect('/openapi')