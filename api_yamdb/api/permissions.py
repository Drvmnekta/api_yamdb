"""Module with permissions."""

from rest_framework import permissions

MODERATOR_METHODS = ('PATCH', 'DELETE')


class IsAdmin(permissions.BasePermission):
    """Is admin permission.
    
    Returns true if user is admin, else forbidden.
    """

    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and (request.user.is_admin))


class IsAdminOrReadOnly(permissions.BasePermission):
    """Is admin or read only permission.
    
    Returns true if user is admin, else read only.
    """

    def has_permission(self, request, view):
        return ((request.method in permissions.SAFE_METHODS)
                or (request.user.is_authenticated
                and request.user.is_admin)
                or (request.user.is_superuser))

    def has_object_permission(self, request, view, obj):
        return ((request.method in permissions.SAFE_METHODS)
                or ((request.user.is_authenticated)
                and (request.user.is_admin))
                or (request.user.is_superuser))


class IsAuthorOrModerator(permissions.BasePermission):
    """Is author or moderator permission.
    
    Returns true if user is author or moderator, else forbidden.
    """

    def has_permission(self, request, view):
        return ((request.method in permissions.SAFE_METHODS)
                or (request.user.is_authenticated))

    def has_object_permission(self, request, view, obj):
        return (((request.method in MODERATOR_METHODS)
                and (request.user.is_moderator))
                or (obj.author == request.user))


class OwnResourcePermission(permissions.BasePermission):
    """Own resource permission.
    
    Returns true if admin or moderator patches or deletes,
    else forbidden.
    """

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if (request.user.is_authenticated
           and request.method in ['PATCH', 'DELETE']):
            return (obj.author == request.user
                    or request.user.is_admin
                    or request.user.is_moderator)
        return False


class IsAuthorOrAdminOrModerator(permissions.BasePermission):
    """Is admin or author or moderator permission.
    
    Returns true if user is author, admin or moderator,
    else forbidden.
    """

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if (request.user.is_staff
                    or request.user.is_admin
                    or request.user.is_moderator
                    or obj.author == request.user
                    or request.method == 'POST'):
                return True
        if request.method in permissions.SAFE_METHODS:
            return True


class AdminOrReadOnly(permissions.BasePermission):
# if not used - delete
    def has_permission(self, request, view):
        return (
            (request.method in permissions.SAFE_METHODS)
            or (request.user.is_authenticated
                and (request.user.is_admin)
                )
        )
