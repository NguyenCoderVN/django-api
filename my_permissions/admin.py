from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from .models import Message


class MessageAdmin(GuardedModelAdmin):
    pass


admin.site.register(Message, MessageAdmin)
