from django import forms

class LabelForm(forms.Form):
    label_text = forms.CharField(max_length=200)

    def clean_renew_data(self):
        data = self.cleaned_data['label_text']
        return data

        
