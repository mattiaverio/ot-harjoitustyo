import unittest
from entities.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Matti")

    def test_init(self):
        self.assertEqual(self.user.username, "Matti")
        self.assertEqual(self.user.elo, 1200)

    def test_init_custom(self):
        custom_user = User("Teppo", 1500)
        self.assertEqual(custom_user.elo, 1500)

    def test_str(self):
        self.assertEqual(str(self.user), "Matti (ELO: 1200)")