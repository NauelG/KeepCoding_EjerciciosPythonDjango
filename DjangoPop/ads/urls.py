from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from ads.api import AdViewSet
from ads.views import HomeView, AdDetailView, NewAddView

router = DefaultRouter()
router.register('ads', AdViewSet)

urlpatterns = [
    path('ads/<int:pk>', AdDetailView.as_view(), name='ad_detail'),
    path('ads/new', NewAddView.as_view(), name='new_ad'),
    path('', HomeView.as_view(), name='home'),

    # API
    path('api/1.0/', include(router.urls))
]
