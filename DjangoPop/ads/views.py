from django.shortcuts import render
from ads.models import Ad


def home(request):
    # 1) Obtener los anuncios de la BBDD
    published_ads = Ad.objects.filter(status=Ad.PUBLISHED).order_by('-last_modification')
    ads_list = published_ads[:4]
    # 2) Pasar los anuncios a la plantilla para que los renderize en HTML
    contex = {'ads': ads_list}
    return render(request, 'ads/home.html', contex)
