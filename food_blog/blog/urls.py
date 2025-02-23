from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("profile", views.profile, name="profile"),
    path("logout", views.logout, name='logout'),
    path("post", views.postLister, name="postLister"),
    path("post/<int:post_id>", views.post, name="post")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)