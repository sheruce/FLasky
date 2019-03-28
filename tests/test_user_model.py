import unittest
from app.models import User


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password='qsy')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='qsy')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='qsy')
        self.assertTrue(u.verify_password('qsy'))
        self.assertFalse(u.verify_password('my'))

    def test_password_salts_are_random(self):
        u = User(password='qsy')
        u2 = User(password='my')
        self.assertTrue(u.password_hash != u2.password_hash)
