class Error(Exception):
    pass


class ClientError(Error):
    pass


class ServerError(Error):
    pass


class AuthenticationError(ClientError):
    pass


class CallbackRequiredError(Error):
    """Indicates a callback is required but was not present."""


class MessagesError(Error):
    """
    Indicates an error related to the Messages class which calls the Vonage Messages API.
    """


class PricingTypeError(Error):
    """A pricing type was specified that is not allowed."""


class RedactError(Error):
    """Error related to the Redact class or Redact API."""


class InvalidAuthenticationTypeError(Error):
    """An authentication method was specified that is not allowed"""


class MeetingsError(ClientError):
    """An error related to the Meetings class which calls the Vonage Meetings API."""


class Verify2Error(ClientError):
    """An error relating to the Verify (V2) API."""


class SubaccountsError(ClientError):
    """An error relating to the Subaccounts API."""


class ProactiveConnectError(ClientError):
    """An error relating to the Proactive Connect API."""


class VideoError(ClientError):
    """An error relating to the Video API."""


class UsersError(ClientError):
    """An error relating to the Users API."""


class InvalidRoleError(ClientError):
    """The specified role was invalid."""


class TokenExpiryError(ClientError):
    """The specified token expiry time was invalid."""


class SipError(ClientError):
    """Error related to usage of SIP calls."""


class NumberVerificationError(ClientError):
    """An error relating to the Number Verification API."""
