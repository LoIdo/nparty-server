import zope.interface


class IMobile(zope.interface.Interface):
    """
    mobile device interface
    """

    def send_sms(number, content):
        """
        :param number: mobile phone number
        :param content: message content
        :return: none
        """

    def send_voice(number, content):
        """
        :param number: mobile phone number
        :param content: voice content
        :return: none
        """


class IMobileFactory(zope.interface.Interface):
    """
    mobile factory
    """

    def __init__(bundle_factory):
        """
        initialize mobile factory
        """

    def __call__(bundle):
        """
        create object which provide sms center
        """

