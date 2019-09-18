from django.db import models


class Users(models.Model):
	FirstName = models.CharField(max_length=50)
	LastName  = models.CharField(max_length=50)
	NickName  = models.CharField(max_length=50)

	Sex       = models.CharField(max_length=1)

	password   = models.TextField()
	email   = models.TextField()

	bYear     = models.IntegerField()
	bMonth    = models.IntegerField()
	bDay      = models.IntegerField()

	dateReg   = models.DateTimeField()

	def __str__(self):
		return self.NickName
