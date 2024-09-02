from django import forms # type: ignore
from .models import Post
#class based

class PostCreateForm(forms.ModelForm):
  class Meta:
         model=Post
         fields=['title','content','author','date_created']

