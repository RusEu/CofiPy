from django import forms

class IdeaForm(forms.Form):
	idea = forms.CharField(widget=forms.Textarea(
                                attrs={'id': 'idea',
                                        'class': 'form-control',
                                        'placeholder': 'Enter Text Here',
                                        'rows':'3',
                                        'cols':'30',}),
                                max_length=100,
                                label=("Idea"))