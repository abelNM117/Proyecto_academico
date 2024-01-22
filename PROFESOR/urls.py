from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('mostrarp/<id>', views.mostrarp, name= 'mostrarp'),
    path('savep/', views.savep, name= 'savep'),
    path('modipr/<str:id>', views.modificar_pr, name= 'modipr'),
    path('notaa/<str:id>', views.nota, name= 'notaa'),
    path('nota1/<str:id>', views.nota1, name= 'nota1'),
    path('notaagg/', views.AGG_NOTA, name= 'notaagg'),
    # path('con_nota/', views.CONSULTAR_NO, name= 'con_nota'),
    path('modificarN/', views.MODI_NOTA, name= 'modificarN'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
