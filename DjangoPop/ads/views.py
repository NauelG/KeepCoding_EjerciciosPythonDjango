from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.views.generic.detail import DetailView

from ads.forms import AdForm
from ads.models import Ad

class HomeView(View):

    def get(self, request):
        # 1) Obtener los anuncios de la BBDD
        published_ads = Ad.objects.select_related('owner').filter(status=Ad.PUBLISHED).order_by('-last_modification')
        ads_list = published_ads[:4]
        # 2) Pasar los anuncios a la plantilla para que los renderize en HTML
        contex = {'ads': ads_list}
        return render(request, 'ads/home.html', contex)


class AdDetailView(DetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'



class NewAddView(View):

    def get(self, request):
        form = AdForm()
        return render(request, 'ads/new_ad.html', {'form': form})


    @method_decorator(login_required)
    def post(self, request):
        new_ad = Ad(owner=request.user)
        form = AdForm(request.POST, request.FILES, instance=new_ad)
        if form.is_valid():
            new_ad = form.save()
            messages.success(request, 'Ad {0} created successfully'.format(new_ad.name))
            form = AdForm()
        return render(request, 'ads/new_ad.html', {'form': form})
