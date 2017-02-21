from django.contrib import admin
from django.contrib import messages
from django import forms
from daterange_filter.filter import DateRangeFilter

from ecwsp.attendance.models import StudentAttendance, CourseAttendance, AttendanceLog, AttendanceStatus

from ajax_select import make_ajax_form

class StudentAttendanceAdmin(admin.ModelAdmin):
    form = make_ajax_form(StudentAttendance, dict(student='attendance_quick_view_student'))
    list_display = ['student', 'date', 'status', 'notes', 'time']
    list_filter = [
        ('date', DateRangeFilter),
        'status'
        ]
    list_editable = ['status', 'notes']
    search_fields = ['student__fname', 'student__lname', 'notes', 'status__name']
    def save_model(self, request, obj, form, change):
        #HACK to work around bug 13091
        try:
            obj.full_clean()
            obj.save()
        except forms.ValidationError:
            messages.warning(request, 'Could not save %s' % (obj,))

    def lookup_allowed(self, lookup, *args, **kwargs):
        if lookup in ('student','student__id__exact',):
            return True
        return super(StudentAttendanceAdmin, self).lookup_allowed(lookup, *args, **kwargs)

admin.site.register(StudentAttendance, StudentAttendanceAdmin)

class CourseAttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'course', 'course_period', 'status', 'notes']
    list_filter = [
        ('date', DateRangeFilter),
        'status'
        ]
    search_fields = ['student__fname', 'student__lname', 'notes', 'status__name']

    def lookup_allowed(self, lookup, *args, **kwargs):
        if lookup in ('student','student__id__exact',):
            return True
        return super(StudentAttendanceAdmin, self).lookup_allowed(lookup, *args, **kwargs)
admin.site.register(CourseAttendance, CourseAttendanceAdmin)

admin.site.register(AttendanceLog)

class AttendanceStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'excused', 'absent', 'tardy', 'half']
admin.site.register(AttendanceStatus,AttendanceStatusAdmin)
