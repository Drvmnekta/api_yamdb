"""Module with mixin classes."""

from rest_framework import mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination


class BaseViewSet(viewsets.ModelViewSet):
    """Base viewset mixin with pagination."""

    pagination_class = LimitOffsetPagination


class ListCreateViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """List create viewset."""

    pagination_class = LimitOffsetPagination


class ListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """List view viewset."""
    
    pagination_class = LimitOffsetPagination
