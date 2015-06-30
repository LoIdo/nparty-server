import zope.interface


class ITime(zope.interface.Interface):
    """
    plan for time
    """

    time_plan = zope.interface.Attribute('time of plan')

    time_last = zope.interface.Attribute('last time of party')

    period_party = zope.interface.Attribute('time period of party')
    ''' should provide interface.technical.ITimePeriod '''

    def add_member(member):
        """
        calculate time of party by members' schedule
        """


class IPlace(zope.interface.Interface):
    """
    plan for place
    """

    area = zope.interface.Attribute('plan place')
    ''' should provide interface.technical.IAreaCircle '''

    address = zope.interface.Attribute('address details of plan place')

    def add_member(member):
        """
        :param member:
        :return:
        """


# class ICenter(zope.interface.Interface):
#     """
#     coordinate center
#     """
#
#     def add_coordinate_time(**kwargs):
#         """
#         add coordinate for time
#         """
#
#     def add_coordinate_place(**kwargs):
#         """
#         add coordinate for place
#         """
#
#
# class ICenterFactory(zope.interface.Interface):
#     """
#     factory of coordinate center
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