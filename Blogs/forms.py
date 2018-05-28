from django.forms import ModelForm
from django.contrib import admin
#from ckeditor.widgets import CKEditorWidget

from Blogs.models import *

class PostAdminForm(ModelForm):
    #description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'