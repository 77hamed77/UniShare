from django.db import models

# 1. جدول الكليات
class Faculty(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الكلية")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "كلية"
        verbose_name_plural = "الكليات"

# 2. جدول السنوات الدراسية (مرتبط بالكلية)
class AcademicYear(models.Model):
    name = models.CharField(max_length=50, verbose_name="السنة الدراسية")
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='years', verbose_name="الكلية")

    def __str__(self):
        return f"{self.name} - {self.faculty.name}"

    class Meta:
        verbose_name = "سنة دراسية"
        verbose_name_plural = "السنوات الدراسية"

# 3. جدول المواد (مرتبط بالسنة الدراسية)
class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم المادة")
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='subjects', verbose_name="السنة الدراسية")

    def __str__(self):
        return f"{self.name} ({self.academic_year.name})"

    class Meta:
        verbose_name = "مادة"
        verbose_name_plural = "المواد"

# 4. جدول المحاضرات (يحتوي الرابط)
class Lecture(models.Model):
    # خيارات نوع الملف
    FILE_TYPE_CHOICES = [
        ('PDF', 'ملف PDF'),
        ('IMG', 'صورة'),
    ]

    title = models.CharField(max_length=200, verbose_name="عنوان المحاضرة")
    description = models.TextField(blank=True, null=True, verbose_name="وصف المحاضرة")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lectures', verbose_name="المادة")
    
    # هنا الفكرة الذكية: رابط نصي بدلاً من رفع ملف
    drive_link = models.URLField(verbose_name="رابط التحميل (Drive/Mega)")
    
    file_type = models.CharField(max_length=3, choices=FILE_TYPE_CHOICES, default='PDF', verbose_name="نوع الملف")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "محاضرة"
        verbose_name_plural = "المحاضرات"
        ordering = ['-created_at'] # ترتيب المحاضرات من الأحدث للأقدم