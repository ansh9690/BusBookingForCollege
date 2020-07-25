from import_export import resources
from .models import BusInfo


class BusInfoResources(resources.ModelResource):
    class meta:
        model = BusInfo
