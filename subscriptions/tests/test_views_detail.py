# coding: utf-8
from django.test import TestCase
from subscriptions.models import Subscription


class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(
            name='Marco Rougeth',
            cpf='12345678901',
            email='marco@rougeth.com',
            phone='61-123456789'
        )
        self.response = self.client.get('/inscricao/{}/'.format(s.pk))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.response,
            'subscriptions/subscription_detail.html'
        )

    def test_context(self):
        subscription = self.response.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        self.assertContains(self.response, 'Marco Rougeth')
