from ariadne import ObjectType

user_query = ObjectType("Query")

@user_query.field("user")
def resolve_user(_, info, id):
    return {"id": id, "contentMessage": "Sample Content Message for User"}
