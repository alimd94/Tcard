from rest_framework import generics #, permissions, mixins
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
from .models import Product
# from django.contrib.auth.models import User
#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer #set user serializer 
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data) #get data
        serializer.is_valid(raise_exception=True) #if its valid countinue
        user = serializer.save() #save
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })
#use generic django rest api for crud
class ProductDeleteApi(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,) #handeling authentication with this attribute
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductReadApi(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateApi(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer