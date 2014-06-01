# coding: utf-8
from django.test import TestCase
from subscriptions.forms import SubscriptionForm

from subscriptions.models import Subscription


class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        ''' GET /inscricao/ must return status code 200
        '''
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        ''' Response should be a rendered template
        '''
        self.assertTemplateUsed(
            self.response,
            'subscriptions/subscription_form.html'
        )

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        ''' Context must have the subscription form
        '''
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(
            name='Marco Rougeth',
            cpf='1234567890',
            email='marco@rougeth.com',
            phone='1234567890'
        )
        self.response = self.client.post('/inscricao/', data)

    def test_post(self):
        ''' Valid POST should redirect to /inscricao/1/
        '''
        self.assertEqual(302, self.response.status_code)

    def test_save(self):
        ''' Valid POST must be saved
        '''
        self.assertTrue(Subscription.objects.exists())


class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(
            name='Marco Rougeth',
            cpf='000000000001',
            email='marco@rougeth.com',
            phone='1234567890'
        )
        self.reponse = self.client.post('/inscricao/', data)

    def test_post(self):
        self.assertEqual(200, self.reponse.status_code)

    def test_form_errors(self):
        self.assertTrue(self.reponse.context['form'].errors)

    def test_dont_save(self):
        self.assertFalse(Subscription.objects.exists())
