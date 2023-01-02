from django.test import TestCase
from django.core import mail
from core import forms

class TestarForm(TestCase):
    def testar_form_fale_conosco_corretamente_preenchido(self):
        formulario = forms.FaleConoscoForm(
            {
                'nome': 'michael jackson',
                'email_origem': 'michale@gmail.com',
                'mensagem': 'testando a funcionalidade do formulario'
            }
        )
        self.assertTrue(formulario.is_valid())
        formulario.enviar_mensagem_por_email()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'FALE_CONOSCO: mensagem recebida.')

    def testar_formulario_fale_conosco_invalido(self):
        formulario = forms.FaleConoscoForm(
            {
            'mensagem': 'Testando a funcionalidade do formulario fale conosco'
            }
        )
        self.assertFalse(formulario.is_valid())
