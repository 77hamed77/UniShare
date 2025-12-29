from django.contrib import admin
from django.urls import path, include  # 1. أضفنا include هنا

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 2. توجيه كل الروابط إلى تطبيق lectures
    # تركنا السترينغ فارغاً '' لكي تفتح صفحة الكليات مباشرة عند فتح الموقع
    path('', include('lectures.urls')),
]