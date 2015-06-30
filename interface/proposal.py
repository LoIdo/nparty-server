import zope.interface


class IProposal(zope.interface.Interface):
    """
    plan of party
    """

    id = zope.interface.Attribute('proposal id')

    status = zope.interface.Attribute('proposal status')

    description = zope.interface.Attribute('party description')

    def get_group():
        """
        get party group, which provide interface.IGroup
        """

    time_proposal = zope.interface.Attribute('proposal time')

    time_spend = zope.interface.Attribute('time spend of party')

    period_schedule = zope.interface.Attribute('schedule period')
    ''' should provide interface.technical.ITimePeriod '''