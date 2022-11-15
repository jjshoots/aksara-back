from rest_framework import serializers
from .models import MetaJson, KKMNowJSON, CatalogJson

class MetaSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = MetaJson
        fields = ['dashboard_name', 'dashboard_meta']

class KKMSerializer(serializers.ModelSerializer) :
    class KKM : 
        model = KKMNowJSON
        fields = ['dashboard_name', 'chart_name', 'chart_type', 'chart_data']

class CatalogSerializer(serializers.ModelSerializer) :
    class Catalog : 
        model = CatalogJson
        fields = ["id", "catalog_meta", "catalog_name", "catalog_category", "time_range", "geographic", "dataset_range", "data_source", "catalog_data"]