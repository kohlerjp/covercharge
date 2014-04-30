from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	media = models.CharField(default='link',max_length=15)
	location = models.CharField(max_length=200)
	genre = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title
	def score(self):
		return self.upvotes - self.downvotes
	def get_id(self):
		if self.media == 'youtube':
			return self.location.split('=')[1].split('&')[0]

class Comment(models.Model):
	post = models.ForeignKey(Post)
	content = models.CharField(max_length=140)

	def __unicode__(self):
		return self.content