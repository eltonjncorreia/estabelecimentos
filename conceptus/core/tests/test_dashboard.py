from django.test import TestCase
from django.shortcuts import resolve_url as r

from conceptus.core.models import Store


class DashboadTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:dashboard'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/dashboard.html')

    def test_context_stores(self):
        store = self.resp.context['stores']
        self.assertTrue(self.resp, store)
