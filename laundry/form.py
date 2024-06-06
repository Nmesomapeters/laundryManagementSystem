from django import forms
from .models import Service, Cart, Checkout, ServiceCart, Product

class AddServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'price']


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['num_shirts', 'num_pants', 'num_suits', 'num_skirts', 'num_dresses', 'num_others', 'special_requests', 'pickup_date']
        widgets = {
            'pickup_date': forms.SelectDateWidget(),
        }

    def clean(self):
        cleaned_data = super().clean()
        total_clothes = (
            cleaned_data.get('num_shirts', 0) +
            cleaned_data.get('num_pants', 0) +
            cleaned_data.get('num_suits', 0) +
            cleaned_data.get('num_skirts', 0) +
            cleaned_data.get('num_dresses', 0) +
            cleaned_data.get('num_others', 0)
        )
        if total_clothes == 0:
            raise forms.ValidationError('You must add at least one piece of clothing.')
        return cleaned_data


class AddServiceToCartForm(forms.ModelForm):
    class Meta:
        model = ServiceCart
        fields = ['service',]
        

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['full_name', 'email_id', 'delivery_address', 'phone_number', 'payment_method']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category']