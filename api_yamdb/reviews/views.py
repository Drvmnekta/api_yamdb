"""Module with views of reviews app."""

from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.serializers import ModelSerializer

from api.permissions import IsAuthorOrAdminOrModerator
from reviews.models import Review
from reviews.serializers import CommentsSerializer, ReviewSerializer
from titles.models import Title


class ReviewViewSet(viewsets.ModelViewSet):
    """Viewset for reviews."""

    serializer_class = ReviewSerializer
    permission_classes = [IsAuthorOrAdminOrModerator]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer: ModelSerializer) -> None:
        """Review creation."""
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)

    def get_queryset(self) -> QuerySet:
        """Get reviews as queryset for viewset."""
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()


class CommentsViewSet(viewsets.ModelViewSet):
    """Viewset for comments."""

    serializer_class = CommentsSerializer
    permission_classes = [IsAuthorOrAdminOrModerator]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer: ModelSerializer) -> None:
        """Comment creation."""
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(
            Review,
            pk=review_id,
            title__id=title_id,
        )
        serializer.save(author=self.request.user, review=review)

    def get_queryset(self) -> QuerySet:
        """Get comments as queryset for viewset."""
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(
            Review,
            pk=review_id,
            title__id=title_id,
        )
        return review.comments.all()
