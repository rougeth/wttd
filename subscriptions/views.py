from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

from subscriptions.models import Subscription
from subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        return subscribe_create(request)
    else:
        return subscribe_new(request)

def subscribe_new(request):
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()})

def subscribe_create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html',
                      {'form': form})

    obj = form.save()
    return HttpResponseRedirect('/inscricao/%d' % obj.pk)


def detail(request, pk):
    subscription = Subscription.objects.get(pk=pk)
    return render(request, 'subscriptions/subscription_detail.html',
                  {'subscription': subscription})
