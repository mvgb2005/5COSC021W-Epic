from django.contrib import admin
from .models import Department, Team, Membership, Repository, Dependency, ContactChannel, AuditLog

# Register your models here.
admin.site.register(Department)
admin.site.register(Team)
admin.site.register(Membership)
admin.site.register(Repository)
admin.site.register(Dependency)
admin.site.register(ContactChannel)
admin.site.register(AuditLog)