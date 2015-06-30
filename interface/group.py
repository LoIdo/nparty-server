import zope.interface


class IGroup(zope.interface.Interface):
    """
    for people in the party
    """
    organizer = zope.interface.Attribute('organizer of group')

    invitees = zope.interface.Attribute('invitees of group')

    members = zope.interface.Attribute('members of group')