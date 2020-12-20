from unittest import TestCase

from guid import GUID
from uuid import uuid4
from guid import uuid_to_guid
from guid import guid_to_uuid


class TestGUID(TestCase):
	def test_0(self):
		u1 = uuid4()
		g = uuid_to_guid(u1)
		u2 = guid_to_uuid(g)
		self.assertEqual(u1, u2)

	def test_1(self):
		g1 = GUID()
		u = guid_to_uuid(g1)
		g2 = uuid_to_guid(u)
		self.assertEqual(g1, g2)
