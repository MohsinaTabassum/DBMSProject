from django.contrib import admin

from core.models import School,Department,Faculty,CO,Course,CourseOutline,Enrollment,Evaluation,PLO,Programme,Question,Section,Student

# Register your models here.
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Faculty)

admin.site.register(CO)
admin.site.register(Course)
admin.site.register(CourseOutline)

admin.site.register(Enrollment)
admin.site.register(Evaluation)
admin.site.register(PLO)

admin.site.register(Programme)
admin.site.register(Question)
admin.site.register(Section)
admin.site.register(Student)