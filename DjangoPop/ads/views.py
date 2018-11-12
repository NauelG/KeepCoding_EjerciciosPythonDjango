from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render

from ads.forms import AdForm
from ads.models import Ad


def home(request):
    # 1) Obtener los anuncios de la BBDD
    published_ads = Ad.objects.select_related('owner').filter(status=Ad.PUBLISHED).order_by('-last_modification')
    ads_list = published_ads[:4]
    # 2) Pasar los anuncios a la plantilla para que los renderize en HTML
    contex = {'ads': ads_list}
    return render(request, 'ads/home.html', contex)


def ad_detail(request, ad_pk):
    # 1) Obtener el ad de la BBDD
    try:
        ad = Ad.objects.select_related('owner').get(pk=ad_pk)
        context = {'ad': ad}
        return render(request, 'ads/ad_detail.html', context)
    except Ad.DoesNotExist:
        return HttpResponse('Ad not found', status=404)

@login_required
def new_ad(request):

    if request.method == 'POST':
        new_ad = Ad(owner=request.user)
        form = AdForm(request.POST, request.FILES, instance=new_ad)
        if form.is_valid():
            new_ad = form.save()
            messages.success(request, 'Ad {0} created successfully'.format(new_ad.name))
            form = AdForm()
    else:
        form = AdForm()
    return render(request, 'ads/new_ad.html', {'form': form})
