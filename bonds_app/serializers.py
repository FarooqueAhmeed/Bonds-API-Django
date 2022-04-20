from rest_framework import serializers
from bonds_app.models import *
from django.contrib.auth.models import User



def Name_of_bond_length(value):
    if len(value) < 3:
        raise serializers.ValidationError("Bond name is too short! It must be greater than 3 alphanumeric . ")
    elif len(value) > 40:
        raise serializers.ValidationError("Bond name is too Long! It must be less than 40 alphanumeric . ")



class GetSellSerializer(serializers.ModelSerializer):
        seller = serializers.HyperlinkedRelatedField(many=False,read_only=True,view_name='view-seller')

        class Meta:
            fields = ('seller', 'Name_of_bond', 'Number_of_bonds_for_sale','Selling_price_of_the_total_number_of_bonds_for_sale','purchased')
            model = Sell


class PostSellSerializer(serializers.ModelSerializer):
    Name_of_bond = serializers.CharField(validators=[Name_of_bond_length])
    Number_of_bonds_for_sale = serializers.IntegerField(max_value=10000, min_value=1)
    Selling_price_of_the_total_number_of_bonds_for_sale = serializers.DecimalField(max_value=100000000,
                                                                                   min_value=0.0000,
                                                                                   max_digits=100000000,
                                                                                   decimal_places=4)

    class Meta:
        fields = ('seller', 'Name_of_bond', 'Number_of_bonds_for_sale', 'Selling_price_of_the_total_number_of_bonds_for_sale','purchased')
        model = Sell




class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('id', 'username')





class BuySerializer(serializers.ModelSerializer):

        class Meta:
            fields = ('id', 'bond', 'buyer',)
            model = Buy

