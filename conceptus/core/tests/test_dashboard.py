from django.test import TestCase


class DashboadTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)


    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/dashboard.html')