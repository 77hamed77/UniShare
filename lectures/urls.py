from django.urls import path
from . import views

# اسم التطبيق (مهم جداً للروابط داخل القوالب لاحقاً)
app_name = 'lectures'

urlpatterns = [
    # الصفحة الرئيسية (قائمة الكليات)
    path('', views.home, name='home'),
    
    # صفحة الكلية (تعرض السنوات)
    # <int:faculty_id> تعني أن هذا الجزء متغير ورقمي، وسنمرره للدالة
    path('faculty/<int:faculty_id>/', views.faculty_detail, name='faculty_detail'),
    
    # صفحة السنة (تعرض المواد)
    path('year/<int:year_id>/', views.year_detail, name='year_detail'),
    
    # صفحة المادة (تعرض المحاضرات)
    path('subject/<int:subject_id>/', views.subject_detail, name='subject_detail'),
    
    # رابط التحميل (التوجيه)
    path('download/<int:lecture_id>/', views.lecture_download, name='lecture_download'),
]