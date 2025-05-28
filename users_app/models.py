from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email address is required.')
        if not username:
            raise ValueError('Username is required.')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user)