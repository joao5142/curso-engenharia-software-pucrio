from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_cors import CORS

from schemas import *

from model import Session, Client

from logger import logger

######################
#openapi 

info = Info(title="Sprint 1 API", version="1.0.0")
app = OpenAPI(__name__, info=info)

# handle openapi cors 
CORS(app)

# documentation tags definition
openapi_documentation_tag = Tag(name="Documentation", description="Documentação da API do projeto Sprint 1")
openapi_client_tag = Tag(name="Client", description="Crud de Clientes")

#######################
# routes

# documentation route redirect to OpenAPI UI
@app.get('/', tags=[openapi_documentation_tag])
def home():
    return redirect('/openapi')

# client routes
@app.post('/clients', tags=[openapi_client_tag],
          responses={"201": CreateClientSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_client(form: CreateClientSchema):
    """Adiciona um cliente à base de dados

    """
    client = Client(
        name=form.name,
        email=form.email,
        phone=form.phone,
        document=form.document)
    
    try:
        session = Session()
        session.add(client)
        session.commit()

        logger.debug(f"Adicionado cliente: '{client.name}'")
        
        
        return {
            "id": client.id,
            "name": client.name,
            "email": client.email,
            "document": client.document,
        }, 201

    except Exception as e:
        logger.warning(f"Tracing  {e}")
        error_msg = "Error ao adicionar cliente"
        logger.warning(f"Erro ao adicionar cliente '{client.name}', {error_msg}")
        return {"mesage": error_msg}, 400
