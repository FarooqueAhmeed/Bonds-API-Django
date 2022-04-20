from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from bonds_app.serializers import *
from django.contrib.auth.models import User




@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def add_and_view_bonds(request):

    if request.method == 'GET':
        sell = Sell.objects.filter(purchased=False)
        serializer = GetSellSerializer(sell, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSellSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_seller(request,pk):
    seller = User.objects.get(pk=pk)
    serializer = UserSerializer(seller, many=False)
    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_sold_bonds(request):
    sold = Buy.objects.all()
    serializer = BuySerializer(sold, many=True)
    return Response(serializer.data)





@api_view(['POST'])
@permission_classes([IsAuthenticated])
def buy_bond_view(request):

    if Buy.objects.filter(**request.data).exists():
            raise serializers.ValidationError('operation is invalid')

    if request.method == 'POST':
        serializer = BuySerializer(data=request.data)

        serializer.is_valid()
        validatedData = serializer.validated_data
        bond = validatedData.get('bond')

        bond.purchased = True

        bond.save()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response(eror={"Failure": "error"}, status=status.HTTP_404_NOT_FOUND)
