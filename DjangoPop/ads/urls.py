from django.urls import path

from ads.views import HomeView, AdDetailView, NewAddView

urlpatterns = [
    path('ads/<int:pk>', AdDetailView.as_view(), name='ad_detail'),
    path('ads/new', NewAddView.as_view(), name='new_ad'),
    path('', HomeView.as_view(), name='home')
]
