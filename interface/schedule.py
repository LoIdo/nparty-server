import zope.interface


class ISchedule(zope.interface.Interface):
    """
    schedule of user
    """

    list_party = zope.interface.Attribute('list of party to go')

    

