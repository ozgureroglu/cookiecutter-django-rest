from django.db import models

{% for n in cookiecutter.models.name %}
class {{n}}(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

{% endfor %}

