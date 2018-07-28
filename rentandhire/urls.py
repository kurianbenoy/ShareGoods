from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/users/',include('Accounts.api.urls'),),
    url(r'^api/products/',include('products.urls')),
    # url(r'^api-auth/', include('rest_framework.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
