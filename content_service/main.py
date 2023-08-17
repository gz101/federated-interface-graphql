from fastapi import FastAPI
from ariadne import load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL

# Load GraphQL schemas
user_schema = load_schema_from_path("content_service/types/schemas/user.graphql")
user_query_schema = load_schema_from_path("content_service/queries/schemas/user.graphql")
base_query_schema = load_schema_from_path("content_service/queries/schemas/query.graphql")

# Combine schemas
type_defs = "\n".join([base_query_schema, user_schema, user_query_schema])

# Resolvers imports
from content_service.types.resolvers.user import user
from content_service.queries.resolvers.user import user_query

# Create executable schema
schema = make_executable_schema(type_defs, user, user_query)

# FastAPI setup
app = FastAPI()
app.add_route("/graphql", GraphQL(schema, debug=True))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8081)  # Make sure to use a different port than profile_service
