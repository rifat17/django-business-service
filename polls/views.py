from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication

class ProtectedDataView(APIView):
    authentication_classes = [JWTStatelessUserAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # request.user will be populated if the JWT is valid
        # You can access user data from the JWT payload:
        # print(request.user.id)
        # print(request.user.email) # Assuming email is in your JWT claims
        return Response({"message": f"Hello, {request.user.username}! This data is protected."})
    

# Example of a custom permission based on JWT claims (if you add custom claims)
# Assuming your JWT payload includes a 'role' claim
# class IsManager(BasePermission):
#     def has_permission(self, request, view):
#         return 'role' in request.user.token_payload and request.user.token_payload['role'] == 'manager'
#
# class ManagerView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated, IsManager]
#
#     def get(self, request):
#         return Response({"message": "Welcome, Manager!"})