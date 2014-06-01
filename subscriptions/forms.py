from django import forms
from django.utils.translation import ugettext as _

from subscriptions.models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
