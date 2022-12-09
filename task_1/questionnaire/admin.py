from django.contrib import admin
from questionnaire.models import *

from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError

from nested_admin import NestedTabularInline, NestedModelAdmin


class AnswerInlineFormSet(BaseInlineFormSet):

    def clean(self):
        super(AnswerInlineFormSet, self).clean()

        total_checked = 0

        forms_number = len(self.forms) 
        if forms_number == 1:
            raise ValidationError("There must be more than one answers")

        for form in self.forms:
            if not form.is_valid():
                return
            if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                if form.cleaned_data['correct']:
                    total_checked += 1


        if total_checked < 1:
            raise ValidationError("There must be at least 1 correct answer")


        if total_checked == forms_number:
            raise ValidationError("All the answers cannot be correct")



class AnswersInLine(NestedTabularInline):
    formset = AnswerInlineFormSet
    model = Answer
    extra = 0


class TestsInLine(NestedTabularInline):
    model = Question
    inlines = [AnswersInLine]
    extra = 0


class SuiteAdmin(NestedModelAdmin):
    inlines = [TestsInLine]


admin.site.register(Test, SuiteAdmin)
admin.site.register(UserAnswer)
