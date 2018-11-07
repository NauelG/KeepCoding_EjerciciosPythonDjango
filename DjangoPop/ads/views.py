from django.http.response import HttpResponse
from django.shortcuts import render
from ads.models import Ad


def home(request):
    # 1) Obtener los anuncios de la BBDD
    published_ads = Ad.objects.filter(status=Ad.PUBLISHED).order_by('-last_modification')
    ads_list = published_ads[:4]
    # 2) Pasar los anuncios a la plantilla para que los renderize en HTML
    contex = {'ads': ads_list}
    return render(request, 'ads/home.html', contex)


def ad_detail(request, ad_id):
    # 1) Obtener el ad de la BBDD
    try:
        ad = Ad.objects.get(id=ad_id)
        context = {'ad': ad}
        return render(request, 'ads/ad_detail.html', context)
    except Ad.DoesNotExist:
        return HttpResponse('Ad not found', status=404)
