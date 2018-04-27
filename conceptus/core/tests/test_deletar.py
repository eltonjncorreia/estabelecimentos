from django.test import TestCase
from django.shortcuts import resolve_url as r
from conceptus.core.models import Store


class DeletarTest(TestCase):
    def setUp(self):
        self.obj = Store.objects.create(nome='Americana',
                                        descricao='loja americana de variedades',
                                        slug='loja-americana',
                                        contato=1235444554,
                                        ramo_atuacao='Variedade')

        self.resp = self.client.get(r('core:deletar', self.obj.slug))

    def test_get(self):
        self.assertEqual(302, self.resp.status_code)

    def test_object_exist(self):
        self.assertTrue(Store.objects.exists)