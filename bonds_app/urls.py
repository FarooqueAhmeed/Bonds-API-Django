from bonds_app.views import *
from django.urls import path


urlpatterns = [
    path('add_view/', add_and_view_bonds, name='add-and-view-bonds'),
    path('seller/<int:pk>/', view_seller, name='view-seller'),
    path('sold/', view_sold_bonds, name='view-sold-bonds'),
    path('buy/', buy_bond_view, name='buy-bond'),
]




