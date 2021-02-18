from django.contrib import admin
from .models import participants,historydonations,profile,event
from django.core.mail import send_mail
from django.contrib.auth.models import auth,User



admin.site.register(participants)
admin.site.register(historydonations)
admin.site.register(profile)
#admin.site.register(event)


def make_published(modeladmin, request, queryset):
    recievers = []
    for user in User.objects.all():
        recievers.append(user.email)
    send_mail("hello subscriber", "An event is going to be held in Graphic Era Hill University soon....", "lalitdungriyal5@gmail.com", recievers)
    print('bhej diye yrr')

class EventAdmin(admin.ModelAdmin):
    actions = [make_published]

admin.site.register(event, EventAdmin)