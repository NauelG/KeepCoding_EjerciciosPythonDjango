from django.shortcuts import render
from ads.models import Ad


def home(request):
    # 1) Obtener los anuncios de la BBDD
    ads_list = Ad.objects.filter(status=Ad.PUBLISHED)

    # 2) Pasar los anuncios a la plantilla para que los renderize en HTML
    contex = {'ads': ads_list}
    return render(request, 'ads/home.html', contex)
