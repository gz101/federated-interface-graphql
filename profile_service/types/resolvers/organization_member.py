from ariadne import ObjectType

organization_member = ObjectType("OrganizationMember")

@organization_member.field("id")
def resolve_id(obj, info):
    return obj["id"]

@organization_member.field("email")
def resolve_email(obj, info):
    return obj["email"]

@organization_member.field("organizationId")
def resolve_organization_id(obj, info):
    return "ORG-67890"
