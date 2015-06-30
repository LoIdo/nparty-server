import zope.interface


class IPlan(zope.interface.Interface):
    """
    interface of party plan
    """

    description = zope.interface.Attribute('party description')
    ''' description of party theme '''

    members = zope.interface.Attribute('party members')
    ''' should provide interface.member.IMembers '''

    plan_time = zope.interface.Attribute('party plan for time')
    ''' should provide interface.coordinate.ITime '''

    plan_place = zope.interface.Attribute('party plan for place')
    ''' should provide interface.coordinate.IPlace '''


class IParty(zope.interface.Interface):
    """
    interface of party
    """

    #  id = zope.interface.Attribute('party id')

    status = zope.interface.Attribute('party status')
    ''' status of party '''

    description = zope.interface.Attribute('party description')
    ''' description of party theme '''

    group = zope.interface.Attribute('party members')
    ''' should provide interface.organization.IGroup '''

    period_time = zope.interface.Attribute('period time of party')
    ''' should provide interface.technical.ITimePeriod '''

    area_place = zope.interface.Attribute('place held for party')
    ''' should provide interface.technical.IAreaCircle '''

