import unittest
from unittest.mock import Mock, patch
from kassapaate import Kassapaate, HINTA
from maksukortti import Maksukortti

""" # someone tell me how to override methods for these tests

@patch.object(Kassapaate, 'osta_lounas')
def minun_osta_lounas(self, kortti: Maksukortti):
    if kortti.saldo >= HINTA:
        kortti.osta(HINTA)
        self.myytyja_lounaita += 1

"""


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Mock(wraps=Kassapaate())

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        maksukortti_mock = Mock(wraps=Maksukortti(10))
        maksukortti_mock.saldo = 10

        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        maksukortti_mock = Mock(wraps=Maksukortti(4))
        maksukortti_mock.saldo = 4

        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_not_called()
