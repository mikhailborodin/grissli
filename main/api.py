from tastypie import fields
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS, ALL
from .models import Url, Result


class UrlResource(ModelResource):
    class Meta:
        queryset = Url.objects.all()

        filtering = {
            'id': ALL,
        }


class ResultResource(ModelResource):
    url = fields.ForeignKey(UrlResource, 'url', full=True)

    class Meta:
        queryset = Result.objects.all()

        filtering = {
            'url': ALL_WITH_RELATIONS,
        }
