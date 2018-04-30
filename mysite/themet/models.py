from django.db import models

# Create your models here.
class Painting(models.Model):
	title = models.CharField(max_length=150)
	description = models.CharField(max_length=300)
	teaserText = models.CharField(max_length=300)
	url = models.CharField(max_length=300)
	image = models.URLField(max_length=300)
	regularImage = models.CharField(max_length=300)
	largeImage = models.CharField(max_length=300)
	date = models.CharField(max_length=100)
	medium = models.CharField(max_length=100)
	accessionNumber = models.CharField(max_length=20)
	galleryInformation = models.CharField(max_length=300)
	galleryURL = models.URLField(max_length=300, null=True)
	#tract = models.ForeignKey(IncomeTract, on_delete=models.CASCADE)#foreign key

	#string method, determines how django will reference this object in the admin
	#otherwise will be called SiteLocation Object
	def __str__(self):
		return str(self.pk)
