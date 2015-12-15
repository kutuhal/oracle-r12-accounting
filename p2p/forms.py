from django import forms

class P2PForm(forms.Form):
    ITEM_TYPES = ( ('Expense','Expense'), ('Inventory','Inventory'))
    YES_OR_NO = ((True, 'Yes'), (False, 'No'))
    item_type = forms.CharField(max_length=20, widget = forms.Select(choices=ITEM_TYPES))
    period_end_accrual = forms.BooleanField(widget = forms.Select (choices= YES_OR_NO))
    allow_recon_accounting =  forms.BooleanField(widget = forms.Select(choices= YES_OR_NO))
