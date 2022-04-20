from django.db import models
from django.contrib.auth.models import User





class Sell(models.Model):
        seller = models.ForeignKey(User, on_delete=models.CASCADE)
        Name_of_bond = models.CharField(max_length=40,blank=True, null=True)
        Number_of_bonds_for_sale = models.IntegerField(blank=True, null=True)
        Selling_price_of_the_total_number_of_bonds_for_sale = models.DecimalField(max_digits=100000000, decimal_places=4,blank=True, null=True)
        purchased = models.BooleanField(default=False)

        def __str__(self):
            return self.Name_of_bond


class Buy(models.Model):
    bond = models.ForeignKey(Sell, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.buyer.username
