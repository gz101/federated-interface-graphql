from fastapi import FastAPI
from ariadne import gql, load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL

# Load GraphQL schemas
user_interface_schema = load_schema_from_path("profile_service/types/schemas/user_interface.graphql")
user_schema = load_schema_from_path("profile_service/types/schemas/user.graphql")
organization_member_schema = load_schema_from_path("profile_service/types/schemas/organization_member.graphql")
user_query_schema = load_schema_from_path("profile_service/queries/schemas/user.graphql")
organization_member_query_schema = load_schema_from_path("profile_service/queries/schemas/organization_member.graphql")
base_query_schema = load_schema_from_path("profile_service/queries/schemas/query.graphql")

# Combine schemas
type_defs = "\n".join(
    [
        base_query_schema,
        user_interface_schema,
        user_schema,
        organization_member_schema,
        user_query_schema,
        organization_member_query_schema,
    ]
)

# Resolvers imports
from profile_service.types.resolvers.user_interface import user_interface
from profile_service.types.resolvers.user import user
from profile_service.types.resolvers.organization_member import organization_member
from profile_service.queries.resolvers.query import query

# Create executable schema
schema = make_executable_schema(gql(type_defs), [user_interface, user, organization_member, query])

# FastAPI setup
app = FastAPI()
app.add_route("/graphql", GraphQL(schema, debug=True))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
