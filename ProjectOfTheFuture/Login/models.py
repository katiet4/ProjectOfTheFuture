from django.db import models
from datetime import datetime  

class Users(models.Model):
	FirstName = models.CharField(max_length=50)
	LastName  = models.CharField(max_length=50)
	NickName  = models.CharField(max_length=50)

	email     = models.TextField()
	password  = models.TextField()

	Sex       = models.CharField(max_length=1)

	bYear     = models.IntegerField()
	bMonth    = models.IntegerField()
	bDay      = models.IntegerField()

	dateReg   = models.DateTimeField(default=datetime.now(), blank=True)

	#profile
	status = models.TextField(default = "0")
	rank =  models.TextField(default = '1')
	title = models.TextField(default = 'NoNe')
	language =  models.TextField(default = 'NoNe')
	country =  models.TextField(default = 'NoNe')
	city =  models.TextField(default = 'NoNe')
	telephone =  models.TextField(default = '0')
	groups =  models.TextField(default = 'user')
	def __str__(self):
		return self.NickName
