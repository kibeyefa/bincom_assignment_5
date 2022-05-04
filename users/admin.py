from django.contrib import admin
from users.models import Profile, FriendRequest

# Register your models here.
admin.site.register([Profile, FriendRequest])
