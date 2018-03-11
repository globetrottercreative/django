import requests, json
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import EditProfileForm, CreateUserForm
from dashboard.models import UserProfile

def home(request):
    #Create User and User Proflie Objects
    user = request.user
    profile = UserProfile.objects.get(base_user=user)

    #Payload for HTTPRequest URL
    payload = {}
    
    #Build the HTTPRequest URL
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
  
    #Make HTTP Request
    r = requests.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms=' + val + '&tsyms=' + profile.base_fiat, params=payload)
    
    #Store Response
    raw = json.loads(r.content)

    #Make Coin Data Dictionary From Response
    coin_data = {}
    for r in raw:
        coin_data.update({r: raw[r][profile.base_fiat]})

    #Make Base Currency Flag URI From Profile Data
    currency_url = ''
    if profile.base_fiat == 'NZD':
        currency_url = 'nz512.png'
    elif profile.base_fiat == 'USD':
        currency_url = 'us512.png'
    elif profile.base_fiat == 'AUD':
        currency_url = 'au512.png'
    else:
        currency_url = 'nz512.png'

    #Make HTML Data Package
    data = {
        'flag_url': currency_url,
        'timestamp': datetime.now(),
        'coins': coin_data,
        'user': request.user,
        'profile': profile,
    }

    #Return View
    return render(request, 'dashboard/home.html', data)

def newuser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
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
        print(form)
        if form.is_valid():
            form.save()
            
            return redirect('/home/')
        else:
            print('BAD FORM')
    else:
        profile = UserProfile.objects.get(base_user=request.user)
        form = EditProfileForm(initial={
            'base_fiat': profile.base_fiat,
            'first_name': profile.base_user.first_name,
            'last_name': profile.base_user.last_name,
            'email': profile.base_user.email,
            'cc_ETH': profile.cc_ETH,
            'cc_BTC': profile.cc_BTC,
            'cc_LTC': profile.cc_LTC,
            'cc_XRP': profile.cc_XRP,
            'cc_BCH': profile.cc_BCH,
            'cc_ETC': profile.cc_ETC,
            'cc_TRX': profile.cc_TRX,
            'cc_EOS': profile.cc_EOS,
            'cc_NEO': profile.cc_NEO,
            'cc_XMR': profile.cc_XMR,
            })
        data = {
            'form': form,
            'user': request.user
        }
        return render(request, 'dashboard/editprofile.html', data)