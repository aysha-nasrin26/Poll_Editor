from django.contrib import admin

from .models import Question,Choice

admin.site.site_header="pollster Admin"
admin.site.site_title="pollster Admin Area"
admin.site.index_title="Welcome to the pollster admin area"

class choiceinline(admin.TabularInline):
    model=Choice
    extra=3
    
class questionadmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question_text']}),
                  ('Date Information',{'fields':['pub_date'],'classes':['collapse']}),]
    inlines = [choiceinline]

#admin.site.register(question)
#admin.site.register(choice)

admin.site.register(Question,questionadmin)