from django.urls import path
from . import uis_pdf, views , scsr, mssat
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('auth_login', views.auth_login, name='auth_login'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('<str:hospno>/get_patient_enctr/',views.get_patient_enctr,name='get_patient_enctr'),
    path('<str:hospno>/<str:code>/<str:toecode>/add_uis/', views.add_uis, name='add_uis'),
    path('uis_list', views.uis_list, name='uis_list'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('<str:uis>/update_uis', views.update_uis, name='update_uis'),
    path('<str:uis>/process_update_uis', views.process_update_uis, name='process_update_uis'),
    path('<str:uis>/add_scsr', views.add_scsr, name='add_scsr'),
    path('<str:uis>/add_mssat', views.add_mssat, name='add_mssat'),
    path('mss_tool_list', views.mss_tool_list, name='mss_tool_list'),
    path('scsr_list', views.scsr_list, name='scsr_list'),
    path('<str:uis>/uis_pdf', uis_pdf.uis_pdf, name='uis_pdf'),
    path('<str:uis>/scsr_pdf', scsr.scsr_pdf, name='scsr_pdf'),
    path('<str:uis>/mssat_pdf', mssat.mssat_pdf, name='mssat_pdf'),
    path('<str:uis_id>/<str:reccom_id>/del_reccom', views.del_reccom, name='del_reccom'),
    path('<str:uis_id>/<str:osof_id>/del_famcom_osof', views.del_famcom_osof, name='del_famcom_osof'),
    path('<str:uis_id>/<str:famcom_id>/del_famcom', views.del_famcom, name='del_famcom'),
    path('<str:mssat>/update_msstool', views.update_msstool, name='update_msstool'),
    path('<str:mssat>/process_update_mssat', views.process_update_mssat, name='process_update_mssat'),
    path('<str:scsr>/update_scsr', views.update_scsr, name='update_scsr'),
    path('<str:scsr>/process_update_scsr', views.process_update_scsr, name='process_update_scsr'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)