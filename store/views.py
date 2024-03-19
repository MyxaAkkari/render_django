from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializer import ProductSerializer
from rest_framework import status

@api_view(['GET'])
def index(req):
    return Response('hello')



@api_view(['GET','POST','PUT','DELETE'])
def products(req,id=-1):
    if req.method == 'GET':
        if id > -1:
            product = ProductSerializer(Product.objects.get(id=id), many=False).data
            return Response(product, status= status.HTTP_200_OK)
        allProducts = ProductSerializer(Product.objects.all(), many= True).data
        return Response(allProducts, status= status.HTTP_200_OK)
    

    elif req.method == 'POST':
        pro_serializer = ProductSerializer(data=req.data)
        if pro_serializer.is_valid():
            pro_serializer.save()
            return Response (status= status.HTTP_201_CREATED)
        else:
            
            return Response (pro_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    
    elif req.method =='DELETE':
        try:
            temp_task=Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response (status=status.HTTP_404_NOT_FOUND)    
       
        temp_task.delete()
        return Response (status= status.HTTP_202_ACCEPTED)

    elif req.method == 'PUT':
        temp_task = Product.objects.get(id=id)
        serializer = ProductSerializer(temp_task, data = req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)