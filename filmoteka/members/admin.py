from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ("nazev", "zanr", "rok",)


admin.site.register(Member, MemberAdmin)