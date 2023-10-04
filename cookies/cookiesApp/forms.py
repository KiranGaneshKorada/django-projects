from django import forms

class CartItem(forms.Form):
    itemName=forms.CharField(max_length=20)
    quantity=forms.IntegerField()