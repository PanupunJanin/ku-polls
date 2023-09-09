from django.contrib import admin
from .models import Question, Choice


class ChoiceInlines(admin.TabularInline):
    model = Choice
    extra = 1


class AdminQuestion(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Data information', {'fields': ['pub_date', 'end_date']}),
    ]
    inlines = [ChoiceInlines]
    list_display = ('question_text', 'pub_date', 'end_date')
    list_filter = ['pub_date', 'end_date']
    search_fields = ['question_text']


admin.site.register(Question, AdminQuestion)
