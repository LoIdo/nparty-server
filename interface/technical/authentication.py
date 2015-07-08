import zope.interface


class IAuth(zope.interface.Interface):
    """
    authentication
    """

#    id = zope.interface.Attribute('id of owner')

    password = zope.interface.Attribute('password to login')

    mobile = zope.interface.Attribute('binding mobile number')

    email = zope.interface.Attribute('binding email')


# class ICenter(zope.interface.Interface):
#     """
#     center of authentication
#     """
#
#     def add_auth(**kwargs):
#         """
#         add authentication
#         """
#
#     def del_auth(auth_id):
#         """
#         delete authentication by auth id
#         """
#
#     def get_auth(auth_id):
#         """
#         get authentication by auth id
#         """
#
#     def find_auths(**kwargs):
#         """
#         find authentications by conditions
#         """
#
#
# class ICenterFactory(zope.interface.Interface):
#     """
#     center factory
#     """
#
#     def __init__(bundle_factory):
#         """
#         :param bundle_factory:
#         :return:
#         """
#
#     def __call__(bundle):
#         """
#         :param bundle:
#         :return:
#         """