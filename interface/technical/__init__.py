"""
general interfaces
"""
import zope.interface


class ILocation(zope.interface.Interface):
    """
    interface of location
    """
    longitude = zope.interface.Attribute('longitude of location')

    latitude = zope.interface.Attribute('latitude of location')


class IAreaCircle(ILocation):
    """
    interface of circle area
    """
    radius = zope.interface.Attribute('distance of area radius')


class ITimePeriod(zope.interface.Interface):
    """
    interface of time period
    """

    time_start = zope.interface.Attribute('time to start')

    time_last = zope.interface.Attribute('time will last')