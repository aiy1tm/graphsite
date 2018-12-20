from django import forms
from decimal import Decimal

class NumberForm(forms.Form):
    interest_rate = forms.DecimalField(label = "Interest Rate [%]", 
    	min_value = 0.009, max_value = 99.9, initial = Decimal(4.5))
    hoa_monthly = forms.DecimalField(label = "Monthly HOA Payment [$]", 
    	min_value = 0, max_value = 1999.99, initial = Decimal(0))
    property_tax = forms.DecimalField(label = "Property Tax Annual [%]", 
    	min_value = 0, max_value = 99.99, initial = Decimal(0.5))
    down_pct = forms.DecimalField(label = "Down Payment [%]", 
    	min_value = 0, max_value = 99.99, initial = Decimal(20))
    loan_term = forms.DecimalField(label = "Loan Term [years]", 
    	min_value = 0, max_value = 100, initial = Decimal(30))