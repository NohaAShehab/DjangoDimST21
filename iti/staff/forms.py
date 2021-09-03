from django import forms
from staff.models import Departments
from staff.models import Staff



class StaffForm(forms.Form):
    name = forms.CharField(label="Staff name", min_length=3)
    email = forms.EmailField(label="Email")
    image = forms.CharField(label="Image")
    gender = forms.ChoiceField(choices=[
        ("m", "male"),
        ("f", "female")
    ])
    dept = forms.ModelChoiceField(Departments.objects.all())
    #
    # def clean_name(self):
    #     if len(self.name) < 3:
    #         raise NameError("plz select another name ")


# create form that maps the model
class StaffModelForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ["name", "image", "masters", "gender", "email", "dept"]
