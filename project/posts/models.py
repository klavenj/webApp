from django.db import models
from django.conf import settings 
from django.urls import reverse




# Create your models here.
class Post(models.Model):

	#properties of the class
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)
	image = models.ImageField(upload_to='posts')
	content = models.TextField()
	draft = models.BooleanField(default=False)
	updated = models.DateField(auto_now=True, auto_now_add=False)
	published = models.DateField(auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ['-published'] #This will pull the published and post in reverse order

	def __str__(self): #This is how a method is written with two underscores

		return self.title
	
	def __unicode__(self):

		return str(self.title)

	def get_absolute_url(self): #this will provide urls to posts. Redirects you to html within projects 
		return reverse('posts:detail_post', kwargs={'pk':self.pk})

	

