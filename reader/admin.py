from django.contrib import admin
from reader.models import *
# Register your models here.

class market_time_update_finally(admin.ModelAdmin):    
    list_display = ('sridevi_day_open','sridevi_day_close',
                    'time_bazar_open','time_bazar_close',
                    'madhur_day_open','madhur_day_close',
                    'milan_day_open','milan_day_close',
                    'rajdhani_day_open','rajdhani_day_close',
                    'superem_day_open', 'superem_day_close', 
                    'kalyan_day_open','kalyan_day_close',
                    
                    'sridevi_night_open','sridevi_night_close', 
                    'main_bazar_open', 'main_bazar_close',
                    'madhur_night_open','madhur_night_close', 
                    'milan_night_open', 'milan_night_close',
                    'rajdhani_night_open', 'rajdhani_night_close',
                    'superem_night_open', 'superem_night_close', 
                    'kalyan_night_open', 'kalyan_night_close')

admin.site.register(market_time_update, market_time_update_finally) 