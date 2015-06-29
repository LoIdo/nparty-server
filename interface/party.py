import zope.interface


class IParty(zope.interface.Interface):
    """
    interface of party
    """

    """
    basic
    """

    id = zope.interface.Attribute('party id')

    """
    when
    """

    time_plan = zope.interface.Attribute('party plan time')

    time_start = zope.interface.Attribute('party start time')
    ''' agreed start time of party '''

    time_end = zope.interface.Attribute('party end time')
    ''' approximate end time of party '''

    """
    where
    """

    address = zope.interface.Attribute('party address')

    location = zope.interface.Attribute('party location')
    ''' should provide interface.technical.ILocation interface '''
