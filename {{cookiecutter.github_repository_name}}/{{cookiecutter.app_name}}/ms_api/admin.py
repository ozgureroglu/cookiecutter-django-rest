from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
{%for n in cookiecutter.models.name %}
from .models import {{n}}
{% endfor %}

{%for n in cookiecutter.models.name %}
@admin.register({{n}})
class {{n}}Admin(admin.ModelAdmin):
    pass


{% endfor %}


