from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.views import index, post_list, post_detail
from blog.viewsets import PostViewSet, UserViewSet

# from blog.viewsets import PostList, PostDetail

router = DefaultRouter()
router.register("posts", PostViewSet)
router.register("users", UserViewSet)

urlpatterns = [
    path("home/", index),
    path('post/', post_list),
    path('post_detail/<int:id>/', post_detail),
    # path('postlist/', PostList.as_view()),
    # path('postdetail/<int:id>/', PostDetail.as_view()),
    path("", include(router.urls))
]