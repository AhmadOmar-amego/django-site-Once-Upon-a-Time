from django import forms
from .models import Medicine,Patientrating,Descriptionofmed,CommentReview,Comment,Test1,BookingSystem

from django.contrib.auth.models import User


class MedicineForm(forms.ModelForm):

    class Meta:
        model = Medicine
        fields = ['medicine_title', 'description_medicine','genre','place_of_medicine','logo_medicine','company','language_of_book' ,'date_of_launch_book','email_user','author','simple_desciption']


class PatientratingForm(forms.ModelForm):

    class Meta:
        model = Patientrating
        fields = [ 'review','rating']


class DescriptionofmedForm(forms.ModelForm):

    class Meta:
        model = Descriptionofmed
        fields = ['Indications']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



class CommentReviewForm(forms.ModelForm):

    class Meta:
        model = CommentReview
        fields = ['review' ,'rating']
class Comment_term1_form(forms.ModelForm):

    class Meta:
        model = Medicine
        fields = ['medicine_title', 'comment_term1']
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text']

class Test1Form(forms.ModelForm):

    class Meta:
        model = Test1
        fields = ['text']
class MedicineForm_b(forms.ModelForm):

    class Meta:
        model = Medicine
        fields = ['medicine_title','is_booker']

