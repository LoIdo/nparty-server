import zope.interface


class IAttender(zope.interface.Interface):
    """
    member of party
    """
    user = zope.interface.Attribute('user')
    ''' should provide interface.user.IUser '''

    priority = zope.interface.Attribute('priority of user in group')

    list_time = zope.interface.Attribute('time of schedule')
    ''' user schedule for party '''

    list_area = zope.interface.Attribute('list of place')
    ''' user recommend places for party '''


class IGroup(zope.interface.Interface):
    """
    members in party
    """
    organizer = zope.interface.Attribute('organizer of party')

    invitees = zope.interface.Attribute('invitees of party')
    ''' list of interface.user.IUser '''

    attenders = zope.interface.Attribute('attenders of party')
    ''' list of IAttender '''