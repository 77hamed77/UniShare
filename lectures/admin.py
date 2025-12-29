from django.contrib import admin
from .models import Faculty, AcademicYear, Subject, Lecture

# تخصيص واجهة الكلية
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# تخصيص واجهة السنة الدراسية
@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty')
    list_filter = ('faculty',) # إضافة فلتر جانبي حسب الكلية

# تخصيص واجهة المواد
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'academic_year')
    list_filter = ('academic_year__faculty', 'academic_year') # فلترة ذكية
    search_fields = ('name',)

# تخصيص واجهة المحاضرات (الأهم)
@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'file_type', 'created_at')
    list_filter = ('subject__academic_year__faculty', 'subject', 'file_type')
    search_fields = ('title', 'description')
    list_per_page = 20 # عدد العناصر في الصفحة الواحدة

    # تغيير عنوان الهيدر في لوحة التحكم
    admin.site.site_header = "إدارة منصة UniShare"
    admin.site.site_title = "UniShare Admin"
    admin.site.index_title = "لوحة التحكم الرئيسية"