from django import forms
from decimal import Decimal

class MortgageNumberForm(forms.Form):
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


class RetirementNumberForm(forms.Form):
    expected_cagr = forms.DecimalField(label = "Expected Annual Real Return [%]", 
    	min_value = 0.009, max_value = 99.9, initial = Decimal(5.5))

    expected_spend = forms.DecimalField(label = "Retirement Spend [$]", 
    	min_value = 1000, max_value = 1000000, initial = Decimal(35000))

    current_nest = forms.DecimalField(label = "Current Nest Egg [$]", 
    	min_value = -1000000, max_value = 1000000, initial = Decimal(5500))

    annual_savings = forms.DecimalField(label = "Investing per Year [$]", 
    	min_value = 0, max_value = 1000000, initial = Decimal(5500))

    withdrawal_rate = forms.DecimalField(label = "Withdrawal Rate [%]", 
    	min_value = 0.009, max_value = 99.9, initial = Decimal(4))