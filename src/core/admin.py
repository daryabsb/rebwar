from django.contrib import admin
from src.core.models import (Slide, Service, Journey, JourneyDetail, About,
                             Treatment, Condition, Procedure)
# Register your models here.


admin.site.register(Slide)
admin.site.register(Journey)
admin.site.register(JourneyDetail)
admin.site.register(About)

admin.site.register(Service)
admin.site.register(Treatment)
admin.site.register(Condition)
admin.site.register(Procedure)
