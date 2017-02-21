from django.contrib import admin

from ecwsp.sis.helper_functions import ReadPermissionModelAdmin
from ecwsp.benchmarks.models import Benchmark, MeasurementTopic, Department

class BenchmarkAdmin(ReadPermissionModelAdmin):
    list_display = ['number', 'name', 'display_measurement_topics']
    list_filter = ['measurement_topics','measurement_topics__department']
    search_fields = ['number', 'name','measurement_topics__name' ]
admin.site.register(Benchmark, BenchmarkAdmin)

class MeasurementTopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']
    list_filter = ['department']
    search_fields = ['department__name', 'name']
admin.site.register(MeasurementTopic,MeasurementTopicAdmin)

admin.site.register(Department)
