from django.contrib import admin

# Register your models here.
from django.contrib import admin
from.models import movie,category
# Register your models here.
class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,categoryadmin)

class movieadmin(admin.ModelAdmin):
    list_display = ['name','desc','date']
    list_per_page = 5
admin.site.register(movie,movieadmin)