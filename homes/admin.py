from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Housing
from .models import kilidUser
from .models import Comment
from .models import Image
from .models import Bookmark
# from .models import dataUser



admin.site.register(Housing)
admin.site.register(kilidUser)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Bookmark)
# admin.site.register(dataUser)
