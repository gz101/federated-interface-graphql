from ariadne import ObjectType

user = ObjectType("User")

@user.field("id")
def resolve_id(obj, info):
    return obj["id"]

@user.field("contentMessage")
def resolve_content_message(obj, info):
    return obj["contentMessage"]
