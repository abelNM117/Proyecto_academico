from django.urls import path
from . import views


urlpatterns = [
    path('actualizacionEstudiante/<id>', views.actualizacionEstudiante, name= 'actualizacionEstudiante'),
    path('agregarEST/', views.add_est, name = 'add_est'),
    path('modiest/<str:id>', views.modificar_est, name= 'modiest'),
    path('matricula/<id>', views.matri_cula, name = 'matricula'),
    path('agg_matri/', views.agg_matri, name= 'agg_matri'),
    path('notasm_m/<id>', views.notasm_m, name= 'notasm_m'),


    
]