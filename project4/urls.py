from django.contrib import admin
from django.urls import path, include
from products import views
from register.register_views import register_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from register.register_views import login_view
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('phones/', views.phones, name="phones"),
    path('accessories/', views.accessories, name="accessories"),
    path('search/', views.search, name='search'),
    path('cart/', views.show_cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
