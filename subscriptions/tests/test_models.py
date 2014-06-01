from __future__ import unicode_literals
from datetime import datetime

from django.test import TestCase
from django.db import IntegrityError

from subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.subscription = Subscription(
            name='Marco Rougeth',
            cpf='1234567890',
            email='marco@rougeth.com',
            phone='1234567890'
        )

    def test_create(self):
        ''' Subscription must have name, cpf, email and phone
        '''
        self.subscription.save()
        self.assertEqual(1, self.subscription.pk)

    def test_has_created_at(self):
        ''' Subscription must have automatic created_at
        '''
        self.subscription.save()
        self.assertIsInstance(self.subscription.created_at, datetime)

    def test_str(self):
        '''
        '''
        self.assertEqual('Marco Rougeth', str(self.subscription))


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        Subscription.objects.create(
            name='Marco Rougeth',
            cpf='1234567890',
            email='marco@rougeth.com',
            phone='1234567890'
        )

    def test_cpf_unique(self):
        ''' CPF must be unique
        '''
        s = Subscription(
            name='Marco Rougeth',
            cpf='1234567890',
            email='marco@rougeth.com',
            phone='1234567890'
        )
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        ''' Email must be unique
        '''
        s = Subscription(
            name='Marco Rougeth',
            cpf='000000001',
            email='marco@rougeth.com',
            phone='1234567890'
        )
        self.assertRaises(IntegrityError, s.save)


