from django.shortcuts import render, get_object_or_404, redirect
from .models import Faculty, AcademicYear, Subject, Lecture
from django.db.models import Q 
# 1. الصفحة الرئيسية: تعرض قائمة الكليات
def home(request):
    faculties = Faculty.objects.all()
    context = {
        'faculties': faculties
    }
    return render(request, 'lectures/home.html', context)

# 2. صفحة تفاصيل الكلية: تعرض السنوات الدراسية داخل الكلية
def faculty_detail(request, faculty_id):
    # نبحث عن الكلية بالـ ID، إذا لم نجدها نظهر خطأ 404
    faculty = get_object_or_404(Faculty, id=faculty_id)
    # نجلب السنوات المرتبطة بهذه الكلية فقط
    years = faculty.years.all() 
    
    context = {
        'faculty': faculty,
        'years': years
    }
    return render(request, 'lectures/faculty_detail.html', context)

# 3. صفحة تفاصيل السنة: تعرض المواد داخل السنة
def year_detail(request, year_id):
    year = get_object_or_404(AcademicYear, id=year_id)
    subjects = year.subjects.all()
    
    context = {
        'year': year,
        'subjects': subjects
    }
    return render(request, 'lectures/year_detail.html', context)

# 4. صفحة تفاصيل المادة: تعرض المحاضرات
def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    lectures = subject.lectures.all()
    
    context = {
        'subject': subject,
        'lectures': lectures
    }
    return render(request, 'lectures/subject_detail.html', context)

# 5. دالة التحميل الذكي (Redirect)
def lecture_download(request, lecture_id):
    # نجلب المحاضرة
    lecture = get_object_or_404(Lecture, id=lecture_id)
    
    # هنا يمكننا مستقبلاً إضافة كود لعدّ مرات التحميل (Analytics)
    
    # توجيه مباشر لرابط الدرايف
    return redirect(lecture.drive_link)

def search(request):
    query = request.GET.get('q') # الكلمة التي كتبها المستخدم
    results = []
    
    if query:
        # البحث في عنوان المحاضرة أو وصفها أو اسم المادة
        results = Lecture.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(subject__name__icontains=query)
        )
    
    context = {
        'results': results,
        'query': query
    }
    return render(request, 'lectures/search_results.html', context)