# in blog app, users can write an article, delete and article, modify an article, and an article includes author, content and pub_date
from django.db import models
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse

class Tag(models.Model):
	tag_name = models.CharField(max_length=30)
	tag_time = models.DateTimeField(blank=True)
	def __unicode__(self):
		return self.tag_name
# class Tag defines tags, includes tag's name and published date

class Classification(models.Model):
	class_name = models.CharField(max_length=30)
	def __unicode__(self):
		return self.class_name
#class Classification defines the class which articles belongs to, includes the class's name

class Author(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(blank=True)
	website = models.URLField(blank=True)
	def __unicode__(self):
		return u'%s'%(self.name)
#class author defines the information about the author, includes author's name, email and website	

class Articles(models.Model): 
	title = models.CharField(max_length=100)
	content = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(Author)
	tags = models.ManyToManyField(Tag, blank=True)
	classification = models.ForeignKey(Classification)
	caption = models.CharField(max_length=30,blank=True)
	subcaption = models.CharField(max_length=50, blank=True)
	def get_absolute_url(self):
		path = reverse('detail',kwargs={'id':self.id})
		return "http://127.0.0.1:8000%s" % path

# this class defines the contents of an article
