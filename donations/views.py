from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import DonationForm
from .models import Donation
from django.conf import settings
from paystackapi.transaction import Transaction
from django.contrib.auth.decorators import login_required

@login_required
def make_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user
            donation.save()

            # Initialize transaction
            response = Transaction.initialize(
                reference=donation.reference,
                amount=int(donation.amount * 100),  # convert to kobo
                email=donation.email,
                callback_url = request.build_absolute_uri(reverse('donations:verify_donation'))
            )
            return redirect(response['data']['authorization_url'])

    else:
        form = DonationForm()

    return render(request, 'donations/donations.html', {
        'form': form
    })


@login_required
def verify_donation(request):
    reference = request.GET.get('reference')
    result = Transaction.verify(reference)
    if result['data']['status'] == 'success':
        donation = Donation.objects.get(reference=reference)
        donation.verified = True
        donation.save()
        return render(request, 'donations/donations_success.html', {'donation':donation})
    return render(request, 'donations/donations_failed.html')


