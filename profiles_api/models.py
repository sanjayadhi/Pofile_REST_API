from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name for user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email













































# from django.db import models
# # Create your models here.
# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.models import BaseUserManager


# class userProfileManager(BaseUserManager):

# 	"""manager for userprofile"""
# 	 def create_user(self,email,name,password=None):
# 	 	"""create a new user profile"""
# 	 	if not email:
# 	 		"""if email is null"""
#  		raise ValueError('email adress is needed')
# 	 	"""we do normalization"""
# 	 	email = self.normalize_email(email)
# 	 	user = self.model(email=email,name=name)	
# 		"""this line create their our model detabase palce for the value user creditionals"""
# 	 	user.set_password(password) # encript pass
# 	 	user.save(using=self._db)
# 	 	return user
# 	 def create_superuser(self, email, name, password):
# 	 	"""to create a super user eith the same kind of credintionals"""
# 	 	user = self.create_user(email, name, password)
# 	 	"""self is automatic for any class function"""
# 	 	user.is_superuser = True
# 	 	user.is_staff = True
# 		user.save(useing=self._db)
# 	 	return user

                                                      
# class UserProfile(AbstractBaseUser,PermissionsMixin): #inheritance
# 	"""dabate madel for user in the system"""
# 	email = models.EmailField(max_length=255,unique=True)
# 	name = models.CharField(max_length=255)
# 	is_active = models.BooleanField(default=True)
# 	is_staff = models.BooleanField(default=False)

# 	objects = userProfileManager() #classto manage the models above

# 	USERNAME_FIELD = 'email'	#user need to provide email address and pass
# 	REQUIRED_FIELD = ['name']

# 	def get_full_name(self):
# 		""" retrive fullname of user """
# 		return self.name

# 	def get_short_name(self):
# 		"""retrive short name of user""" 
# 		return self.name

# 	def __srt__(self):
# 		"""	return string representation of our user"""
# 		return self.email
