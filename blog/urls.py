from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.views import index, post_list, post_detail
from blog.viewsets import PostViewSet

router = DefaultRouter()
router.register("posts", PostViewSet)
urlpatterns = [
    path("home/", index),
    path('post/', post_list),
    path('post_detail/<int:id>/', post_detail),
    path("", include(router.urls))
]