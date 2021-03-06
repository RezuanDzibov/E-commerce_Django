from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/v1/carts/', include('src.cart.urls', namespace='cart')),
    path('api/v1/products/', include('src.product.urls', namespace='product')),
    path('api/v1/orders/', include('src.order.urls', namespace='order')),
]

urlpatterns += doc_urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
