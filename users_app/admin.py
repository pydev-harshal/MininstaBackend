from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'following':
            kwargs["queryset"] = db_field.remote_field.model.objects.exclude(id=request.user.id)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Profile, ProfileAdmin)
