import zope.interface


class IMobile(zope.interface.Interface):
    """
    mobile device interface
    """

    def sendSMS(number, content):
        """
        :param number: mobile phone number
        :param content: message content
        :return: none
        """

    def sendVoice(number, content):
        """
        :param number: mobile phone number
        :param content: voice content
        :return: none
        """