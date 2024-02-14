
from django.contrib import admin
from django.urls import path

from blog.views import frontpage, post_detail
#frontpage関数がどこにあるのかを教える役割


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", frontpage),
    path("<slug:slug>/", post_detail, name="post_detail")
]
