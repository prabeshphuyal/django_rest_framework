from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):#This method is responsible for determining whether a user has permission to perform a certain action on an object.
        if request.method in permissions.SAFE_METHODS: #Safe methods are read-only operations that do not modify the object's state.
            return True #If the request method is one of the safe methods, the method returns True
        return obj.owner == request.user # if the owner of the object (obj) is the same as the user making the request (request.user). If the owner matches the user, it means they have permission to edit the object, so the method returns True. Otherwise, it returns False, denying permission to edit the object.