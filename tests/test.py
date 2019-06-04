from unittest import TestCase

from guid import GUID


class TestGUID(TestCase):
	def test_1(self):
		guid = GUID()
		self.assertIsNotNone(guid.uuid)
		self.assertIsNotNone(guid.slug)
