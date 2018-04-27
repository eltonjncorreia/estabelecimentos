from django.core.validators import RegexValidator
from django.test import TestCase
from conceptus.core.forms import StoreModelForm


class StoreFormCreateTest(TestCase):
    def test_form_tem_field(self):
        form = StoreModelForm()
        expect = ['ramo_atuacao', 'nome', 'slug', 'descricao', 'contato']
        self.assertSequenceEqual(expect, list(form.fields))

    def test_contato_valida(self):
        form = self.validar_form(contato='ABDC23455')
        self.assertFormErrorMessage(form, 'contato', 'Informe um valor válido.')

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def validar_form(self, **kwargs):
        valid = dict(ramo_atuacao="Variedade",
                     nome="Americana",
                     slug="americana-variedades",
                     descricao='Loja de variedades',
                     contato='1235662445')

        data = dict(valid, **kwargs)
        form = StoreModelForm(data)
        form.is_valid()
        return form