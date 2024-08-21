from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete

class Skill(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class Fakultet(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    kode = models.CharField(max_length=50, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class Kafedra(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    kode = models.CharField(max_length=50, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    fakult = models.ForeignKey(Fakultet, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class Special(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    kode = models.CharField(max_length=50, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    kafedra = models.ForeignKey(Kafedra, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Profile(models.Model):
    USER_TYPES = (
        ('employee', 'Employee'),
        ('student', 'Student'),
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(
        null=True, blank=True, upload_to='profile_images', default="profile_images/default.jpg")
    skills = models.ManyToManyField(Skill, blank=True)
    # github = models.CharField(max_length=100, blank=True, null=True)
    # twitter = models.CharField(max_length=100, blank=True, null=True)
    # linkedin = models.CharField(max_length=100, blank=True, null=True)
    # youtube = models.CharField(max_length=100, blank=True, null=True)
    # website = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPES, blank=True, null=True, default='student')
    specials = models.ManyToManyField(Special, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['created']


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']