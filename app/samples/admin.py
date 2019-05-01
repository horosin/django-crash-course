from django.contrib import admin

from .models import SampleType, Sample


admin.site.site_header = 'Lab admin'

admin.site.register(Sample)
admin.site.register(SampleType)
