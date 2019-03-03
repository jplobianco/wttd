from django.core import mail
from django.test import TestCase

class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='João Paulo Lobianco', cpf='30030030030',
                    email="joaopaulolobianco1@gmail.com", phone="(62)98176-2899")
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'joaopaulolobianco1@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['João Paulo Lobianco', '30030030030', 'joaopaulolobianco1@gmail.com', '(62)98176-2899']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)