"""strogonov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from lodge.views import LodgeViewSet, PriceViewSet, SpecialPriceViewSet
from order.views import OrderViewSet, Order_lodgeViewSet, ServiceViewSet, UslugiViewSet, ProductViewSet
from feedback.views import CommentViewSet
from .views import IndexView
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'order', OrderViewSet)
router.register(r'lodge', LodgeViewSet)
router.register(r'orderlodge', Order_lodgeViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'uslugi', UslugiViewSet)
router.register(r'product', ProductViewSet)
router.register(r'specialPrice', SpecialPriceViewSet)
router.register(r'price', PriceViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = [
    path('',IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+[
    re_path('.*',TemplateView.as_view(template_name='index.html')),
]