from django import forms

class LocationCoods(forms.Form):
	lat = forms.FloatField()
	lng = forms.FloatField()