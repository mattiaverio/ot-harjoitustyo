import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_saldon_lataaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20)

    def test_saldo_vahenee_oikein(self):
        result = self.maksukortti.ota_rahaa(200)
        self.assertEqual(self.maksukortti.saldo_euroina(), 8)
        self.assertTrue(result)

    def test_saldo_ei_muutu_jos_rahat_loppuu(self):
        result = self.maksukortti.ota_rahaa(1200)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)
        self.assertFalse(result)

    def test_str_tulostuu_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")