import time
import datetime
from django.db import models
from django.utils.text import slugify
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=255,blank=True,null=True)
	#description=models.TextField(blank=True,null=True)
	description=RichTextUploadingField(blank=True,null=False)
	photo = models.ImageField(upload_to='mypics/%Y/%m/%d',null=True,blank=True)
	order=models.IntegerField(blank=True,null=True)
	Author=models.CharField(max_length=50,blank=True,null=True)
	publish_date = models.DateTimeField(default=datetime.datetime.now)
	def save(self):
		self.slug = slugify(self.title)
		super(Post,self).save()
	def __str__(self):
		return '%s' % self.title

