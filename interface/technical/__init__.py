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
