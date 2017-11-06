from django.contrib import admin

from .models import Elk_Member, Elk_Photos, Dues, Events, Elk_NewsLetter, Elk_Contact, Membership_Application

# Register your models here.

admin.site.register(Elk_Member)
admin.site.register(Elk_Photos)
admin.site.register(Dues)
admin.site.register(Events)
admin.site.register(Elk_NewsLetter)
admin.site.register(Elk_Contact)
admin.site.register(Membership_Application)
