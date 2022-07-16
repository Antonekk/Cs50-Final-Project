from django.contrib import admin

# Register your models here.
from  .models import User, Poll, Option, Votes

admin.site.register(User)
admin.site.register(Poll)
admin.site.register(Option)
admin.site.register(Votes)