import zope.interface


class ITime(zope.interface.Interface):
    """
    plan for time
    """

    time_plan = zope.interface.Attribute('time of plan')

    time_spend = zope.interface.Attribute('spend time of party')

    period_party = zope.interface.Attribute('time period of party')
    ''' should provide interface.technical.ITimePeriod '''

    def calcTime(group):
        """
        calculate time of party by party group
        return list of time
        """


class IPlace(zope.interface.Interface):
    """
    plan for place
    """

    area = zope.interface.Attribute('plan place')
    ''' should provide interface.technical.IAreaCircle '''

    radius = zope.interface.Attribute('radius distance of plan place')
    ''' radius distance '''

    def calcPlace(group):
        """
        calculate place of party by party group
        return list of places
        """


# class ICenter(zope.interface.Interface):
#     """
#     coordinate center
#     """
#
#     def addCoordinateTime(**kwargs):
#         """
#         add coordinate for time
#         """
#
#     def add_coordinate_place(**kwargs):
#         """
#         add coordinate for place
#         """