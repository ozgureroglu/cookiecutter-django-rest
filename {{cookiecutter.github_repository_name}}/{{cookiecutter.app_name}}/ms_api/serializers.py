{%for n in cookiecutter.models.name %}from .models import {{n}}
{% endfor %}
from rest_framework import serializers

{%for n in cookiecutter.models.name %}
class {{n}}Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = {{n}}
        fields = ['name', ]

{% endfor %}

