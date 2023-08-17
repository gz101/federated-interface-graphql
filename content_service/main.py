from fastapi import FastAPI
from ariadne import load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL

from content_service.resolvers.query import query

content_service_app = FastAPI()

# Load schema from the local schemas directory
type_defs = load_schema_from_path("content_service/schemas/schema.graphql")

schema = make_executable_schema(type_defs, query)
content_service_app.add_route("/graphql", GraphQL(schema, debug=True))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(content_service_app, host="127.0.0.1", port=8001)
