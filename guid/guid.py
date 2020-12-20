from uuid import UUID
from uuid import uuid4
from base64 import urlsafe_b64decode
from base64 import urlsafe_b64encode


def uuid_to_slug(uuid):
    return urlsafe_b64encode(uuid.bytes).rstrip(b'=').decode()


def slug_to_uuid(slug):
    return UUID(bytes=urlsafe_b64decode(slug + '=='))


def guid_to_uuid(guid):
    return slug_to_uuid(guid.slug)


class GUID():
    def __init__(self):
        self.slug = uuid_to_slug(uuid4())

    def to_uuid(self):
        return guid_to_uuid(self)

    def __repr__(self):
        return self.slug

    def __str__(self):
        return self.slug

    def __json__(self):
        return self.slug
