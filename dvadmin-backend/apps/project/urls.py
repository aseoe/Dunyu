from django.urls import re_path
from rest_framework.routers import DefaultRouter

from project.views import ProjectModelViewSet

router = DefaultRouter()
router.register(r'project', ProjectModelViewSet)

urlpatterns = [
    # 导出岗位
    re_path('project/export/', ProjectModelViewSet.as_view({'get': 'export', })),
    # 用户导入模板下载及导入
    re_path('project/importTemplate/',
            ProjectModelViewSet.as_view({'get': 'importTemplate', 'post': 'importTemplate'})),
]

urlpatterns += router.urls