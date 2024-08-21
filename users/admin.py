from django.contrib import admin

from .models import Profile, Skill, Special, Kafedra, Fakultet

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Special)
admin.site.register(Kafedra)
admin.site.register(Fakultet)