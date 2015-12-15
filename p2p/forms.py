from django import forms

class P2PForm(forms.Form):
    ITEM_TYPES = ( ('Expense','Expense'), ('Inventory','Inventory'))
    YES_OR_NO = ((True, 'Yes'), (False, 'No'))
    item_type = forms.ChoiceField( label = 'Item Type' ,initial='Expense',choices=ITEM_TYPES, 
    		widget = forms.Select(  attrs={'class': 'form-control'}))
    period_end_accrual = forms.BooleanField(widget = forms.Select (choices= YES_OR_NO),
                                                        initial=False, required= False)
    allow_recon_accounting =  forms.BooleanField(widget = forms.Select(choices= YES_OR_NO),
                                                            initial=False, required= False)
