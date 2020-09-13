from django.contrib import admin
from .models import Post

admin.site.register(Post)
# 장고에서 기본적으로 제공
# admin = 관리자
# 기본 model Admin으로 등록(관리자..?)
# superuser 계정에 한해서만 접근 가능