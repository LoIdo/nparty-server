import zope.interface


class IPlan(zope.interface.Interface):
    """
    plan of party
    """

    id = zope.interface.Attribute('plan id')

    status = zope.interface.Attribute('plan status')

    description = zope.interface.Attribute('plan description')

    organizer = zope.interface.Attribute('organizer of party')

    attenders = zope.interface.Attribute('attenders of party')