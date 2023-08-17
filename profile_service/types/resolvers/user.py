from ariadne import ObjectType

user = ObjectType("User")

@user.field("id")
def resolve_id(obj, info):
    return obj["id"]

@user.field("email")
def resolve_email(obj, info):
    return obj["email"]

@user.field("individualId")
def resolve_individual_id(obj, info):
    return obj["individualId"]
