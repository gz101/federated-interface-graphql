from ariadne import InterfaceType

user_interface = InterfaceType("UserInterface")

@user_interface.type_resolver
def resolve_user_interface_type(obj, *_):
    return obj["type"]
