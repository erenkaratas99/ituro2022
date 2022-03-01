from django.contrib import admin
from .models import *

class PhotoAdmin(admin.ModelAdmin):

    list_display = ['image','pub_date','isimSoyisim']
    list_display_links = ['image','pub_date']
    fields = ['isimSoyisim']
    list_filter = ['pub_date']
    search_fields = ['image']

    class Meta:
        model = PhotoModel

class OpinionAdmin(admin.ModelAdmin):

    list_display = ['isimSoyisim','opinion','pub_date']



    class Meta:
        model = Opinions


#***************************************************************************

class ScheduleThursdaytInlineAdmin(admin.TabularInline):
    model = ScheduleThursday
    extra = 0


class ScheduleThursdayAdmin(admin.ModelAdmin):
    list_display = ["title","created_at","related_with"]
    search_fields = ["title"]

class ScheduleThursdaysAdmin(admin.ModelAdmin):
    list_display = ['title','related_with']
    readonly_fields =  ['title','related_with','hour_slice']

    class Meta:

        model = ScheduleThursday
        verbose_name_plural = 'Perşembeler'


#***************************************************************************

class ScheduleFridayInlineAdmin(admin.TabularInline):
    model = ScheduleFriday
    extra = 0


class ScheduleFridayAdmin(admin.ModelAdmin):
    list_display = ["title","created_at","related_with"]
    search_fields = ["title"]

class ScheduleFridaysAdmin(admin.ModelAdmin):
    list_display = ['title','related_with']
    readonly_fields =  ['title','related_with','hour_slice']

    class Meta:

        model = ScheduleFriday
        verbose_name_plural = 'Cumalar'


#***************************************************************************

class ScheduleSaturdayInlineAdmin(admin.TabularInline):
    model = ScheduleSaturday
    extra = 0


class ScheduleSaturdayAdmin(admin.ModelAdmin):
    list_display = ["title","created_at","related_with"]
    search_fields = ["title"]

class ScheduleSaturdaysAdmin(admin.ModelAdmin):
    list_display = ['title','related_with']
    readonly_fields =  ['title','related_with','hour_slice']

    class Meta:

        model = ScheduleSaturday
        verbose_name_plural = 'Cumartesiler'


#***************************************************************************
class EventAdmin(admin.ModelAdmin):

    list_display = ['event']
    inlines = [ScheduleThursdaytInlineAdmin,ScheduleFridayInlineAdmin,ScheduleSaturdayInlineAdmin]

    class Meta:
        model = Event


admin.site.register(ScheduleThursday,ScheduleThursdaysAdmin)
admin.site.register(ScheduleFriday,ScheduleFridaysAdmin)
admin.site.register(ScheduleSaturday,ScheduleSaturdaysAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(PhotoModel,PhotoAdmin)
admin.site.register(Opinions,OpinionAdmin)
