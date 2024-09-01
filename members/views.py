from django.shortcuts import render
from .models import Member
from rest_framework import viewsets
from .serializers import MemberSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.views import APIView
from .serializers import MemberSerializer
# Create your views here.

class MemberViewSet2(viewsets.ViewSet):
    """
    Viewset --> is a class-based view which doesn't provide any method handlers
    for your request

    View --> is a python function or python class that accepts Http request and 
    returns and Http Response
    """
    
    def list(self, request):
        """This is a method instance:
        Returns a list of members"""
        members = Member.objects.all()

        #serialize and deserialize queryset
        serializer = MemberSerializer(members, many=True)
        """many=True returns a list of members"""
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        member = Member.objects.filter(pk=pk).first()
        if not member:
            message = {"detail": f"member with id {pk} is not found"}
        serializer = MemberSerializer(member)
        return Response(serializer.data)
    
    def create(self, request):
        queryset = Member.objects.create(**request.data)
        serializer = MemberSerializer(queryset)
        return Response(serializer.data)

    def update(self, request):
        pass

    def partial_update(self, request, pk):
        pass

    def destroy(self, request, pk):
        return Response(status=status.NO_CONTENT)

class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

class MyAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Only authenticated users can access this view"""
        return Response(
            {"message": "Hello authenticated user!"}
        )
    
class IsAdminOrReadOnly(BasePermission):
    """This is a custom permission class
    Allow read-only access to everyone, but requires the user to be admin (staff) for any write permissions"""
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return request.user.is_staff
    
class MyModelListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Only authenticated users can view the list of models"""
        queryset = Member.objects.all()
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data)
    
class MyModelCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        """Only admin users can create new model instances"""
        serializer = MemberSerializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)