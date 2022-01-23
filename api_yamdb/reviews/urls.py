from django.urls import path, include
from rest_framework import routers

from .views import ReviewViewSet, CommentsViewSet


router = routers.DefaultRouter()
router.register(
    r'^titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='review'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet,
    basename='comments'
)

app_name = 'reviews'
urlpatterns = [
    path('v1/', include(router.urls))
]
