from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class userProfileManager(BaseUserManager):
	"""manager for userprofile"""
	def Create_user(self,email,name,password=None):
		"""create a new user profile"""
		if not email:
			"""if email is null"""
			raise ValueError('email adress is needed')

		"""we do normalization"""
		email = self.normalize_email(email)
		user = self.model(email=email,name=name)	
		"""this line create their our model detabase palce for the value user creditionals"""
		user.set_password(password) # encript pass
		user.save(using=self._db)
		return user
	def Create_superuser(self,email,name,password):
		"""to create a super user eith the same kind of credintionals"""
		user = self.create_user(email,user,password)
		"""self is automatic for any class function"""
		user.is_superuser = True
		user.is_staff = True
		user.save(user=self._db)
		return user


class UserProfile(AbstractBaseUser,PermissionsMixin): #inheritance
	"""dabate madel for user in the system"""
	email = models.EmailField(max_length=255,unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = userProfileManager() #classto manage the models above

	USERNAME_FIELD = 'email'	#user need to provide email address and pass
	REQUIRED_FIELD = ['name']

	def get_full_name(self):
		""" retrive fullname of user """
		return self.name

	def get_short_name(self):
		"""retrive short name of user""" 
		return self.name

	def __srt__(self):
		"""	return string representation of our user"""
		return self.email
