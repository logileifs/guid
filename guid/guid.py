from uuid import UUID
from uuid import uuid4
from base64 import urlsafe_b64decode
from base64 import urlsafe_b64encode


def uuid_to_guid(uuid):
    return urlsafe_b64encode(uuid.bytes).rstrip(b'=').decode()


def guid_to_uuid(slug):
    return UUID(bytes=urlsafe_b64decode(slug + '=='))


class GUID():
    def __new__(self):
        return uuid_to_guid(uuid4())
