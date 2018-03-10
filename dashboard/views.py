import requests, json
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EditProfileForm, CreateUserForm
from dashboard.models import UserProfile


# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/');

    user = request.user
    profile = UserProfile.objects.get(base_user=user)
    data = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'dashboard/home.html', data)

def refresh_crypto(request):
    user = request.user
    profile = UserProfile.objects.get(base_user=user)

    payload = {}
    
    crypto_url_payload = []
    if profile.cc_ETH:
        crypto_url_payload.append('ETH')
    if profile.cc_BTC:
        crypto_url_payload.append('BTC')
    if profile.cc_LTC:
        crypto_url_payload.append('LTC')
    if profile.cc_XRP:
        crypto_url_payload.append('XRP')
    if profile.cc_BCH:
        crypto_url_payload.append('BCH')
    if profile.cc_ETC:
        crypto_url_payload.append('ETC')
    if profile.cc_TRX:
        crypto_url_payload.append('TRX')
    if profile.cc_EOS:
        crypto_url_payload.append('EOS')
    if profile.cc_NEO:
        crypto_url_payload.append('NEO')
    if profile.cc_XMR:
        crypto_url_payload.append('XMR')
    
    val = ''
    for d in crypto_url_payload:
        val += (d+',')
  
    r = requests.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms=' + val + '&tsyms=' + profile.base_fiat, params=payload)
    raw = json.loads(r.content)
    
    print(raw['ETH']['NZD'])


    data = {
        'spots': raw['ETH']['NZD'],
        #'btc_spot': p['BTC'][profile.base_fiat],
        #'ltc_spot': p['LTC'][profile.base_fiat],
        #'xrp_spot': p['XRP'][profile.base_fiat],
        #'bch_spot': p['BCH'][profile.base_fiat],
        #'etc_spot': p['ETC'][profile.base_fiat],
        #'trx_spot': p['TRX'][profile.base_fiat],
        #'eos_spot': p['EOS'][profile.base_fiat],
        #'neo_spot': p['NEO'][profile.base_fiat],
        #'xmp_spot': p['XMR'][profile.base_fiat],
        'user': request.user,
        'profile': profile,
    }
    return render(request, 'dashboard/home.html', data)

def newuser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = CreateUserForm()
        data = {
            'form': form,
            'user': request.user,
        }
        return render(request, 'dashboard/newuser.html', data)

def editprofile(request):
    if not request.user.is_authenticated:
        return redirect('/');

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('../home/')
    else:
        profile = UserProfile.objects.get(base_user=request.user)
        form = EditProfileForm(initial={
            'base_crypto': profile.base_crypto,
            'base_fiat': profile.base_fiat,
            'first_name': profile.base_user.first_name,
            'last_name': profile.base_user.last_name,
            'email': profile.base_user.email,
            })
        data = {
            'form': form,
            'user': request.user
        }
        return render(request, 'dashboard/editprofile.html', data)