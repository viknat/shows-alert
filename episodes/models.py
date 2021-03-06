from django.db import models

# Create your models here.
class Users(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=8)

	def __unicode__(self):
		return self.name + self.email

class TvShows(models.Model):
	"""docstring foTvShowsme"""
	show_name = models.CharField(max_length=100)
	show_link = models.URLField(max_length=200)
	name_list = models.ManyToManyField(Users)
	
	def __unicode__(self):
		return self.show_name
