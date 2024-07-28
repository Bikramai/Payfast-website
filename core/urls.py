import notifications.urls
from django.urls import re_path
from django.contrib.auth import views as auth_views
from dj_rest_auth.registration.views import VerifyEmailView
from django.views.static import serve

from src.accounts.views import GoogleLoginView, FacebookLoginView, CustomRegisterAccountView

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from .settings import DEBUG, STATIC_ROOT, MEDIA_ROOT, SERVER
from src.website.views import handler404

handler404 = handler404
urlpatterns = [

    # ADMIN/ROOT APPLICATION
    path('admin/', admin.site.urls),
    path('', include('src.website.urls', namespace='website')),

    path('admins/', include('src.admins.urls', namespace='admins')),
    path('staff/', include('src.staff.urls', namespace='staff')),
    path('customer/', include('src.customer.urls', namespace='customer')),
    path('accounts/', include('src.accounts.urls', namespace='accounts')),
    path('accounts/', include('allauth.urls')),

    path('payments/', include('src.payments.urls', namespace='payments')),
]

urlpatterns += [
    re_path('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
]

# if SERVER != 'server':
#     urlpatterns += [
#         path("__reload__/", include("django_browser_reload.urls"))
#     ]
