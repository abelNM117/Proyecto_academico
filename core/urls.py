from django.urls import path,include
from . import views
from .views import exit
# from ESTUDIANTE.views import actualizacionEstudiante

urlpatterns = [
    path('', views.index, name= 'pagina_principal'),
    path('inicio/', views.inicio, name= 'inicio'),
    path('logout/', exit, name= 'exit'),

    ##################### user ####################
    path('usuario/', views.usuarios, name= 'usuario'),
    path('agregarUserA/', views.agregaruser, name= 'adduser'),
    path('editUserA', views.edituser, name= 'edituser'),
    path('update/<str:id>', views.update, name= 'update'),
    path('elimina-U/<id>/', views.eliminarU, name= 'eliminarU'),
    path('inactivoUsuario/', views.inactivoUsuario, name= 'inactivoUsuario'),
    path('activado-U/<id>/', views.activaU, name= 'activaU'),    
    ######################################################
    path('roles/', views.roles, name= 'roles'),
    path('roles1/', views.roles1, name= 'roles1'),
    path('editR', views.RU, name= 'editR'),
    path('roles2/<id>/', views.roles2, name= 'roles2'),
    ######################################################
    path('rolUser/', views.rolUser, name= 'rolUser'),
    path('ROUS/', views.designar, name= 'ROUS'),
    path('updaterolU/<str:id>', views.updaterolU, name= 'updaterolU'),
    path('eliminar-RolU/<id>/', views.eliminarRolU, name= 'eliminarRolU'),
    # path('delete/<str:id>', views.delete,name='delete'), 
    ##################################################curso
    path('curso_m/', views.curso_m, name= 'curso_m'),
    path('agregarcurso/', views.agregarcurso, name= 'addcurso'),
    path('editcurso', views.editcurso, name= 'editcurso'),
    path('updatecurso/<str:id>', views.updatecurso, name= 'updatecurso'),
    path('elimina-C/<id>/', views.eliminarcurso, name= 'eliminarcurso'),
    ##################################################Jornada
    path('jornada_m/', views.jornada_m, name= 'jornada_m'),
    path('agregarjornada/', views.agregarjornada, name= 'addjornada'),
    path('editjornada', views.editjornada, name= 'editjornada'),
    path('updatejornada/<str:id>', views.updatejornada, name= 'updatejornada'),
    path('elimina-J/<id>/', views.eliminarjornada, name= 'eliminarjornada'),
    ##################################################Paralelo
    path('paralelo_m/', views.paralelo_m, name= 'paralelo_m'),
    path('agregarparalelo/', views.agregarparalelo, name= 'addparalelo'),
    path('editparalelo', views.editparalelo, name= 'editparalelo'),
    path('updateparalelo/<str:id>', views.updateparalelo, name= 'updateparalelo'),
    path('elimina-P/<id>/', views.eliminarparalelo, name= 'eliminarparalelo'),
    ##################################################Periodo
    path('periodo_m/', views.periodo_m, name= 'periodo_m'),
    path('agregarperiodo/', views.agregarperiodo, name= 'addperiodo'),
    path('editperiodo', views.editperiodo, name= 'editperiodo'),
    path('inactivoUsuarioP/', views.inactivoUsuarioP, name= 'inactivoUsuarioP'),
    path('updateperiodo/<str:id>', views.updateperiodo, name= 'updateperiodo'),
    path('elimina-Pe/<id>/', views.eliminarperiodo, name= 'eliminarperiodo'),
    path('activado-P/<id>/', views.activaP, name= 'activaP'),    
    ##################################################TrimestreParcial
    path('trimestrep_m/', views.trimestrep_m, name= 'trimestrep_m'),
    path('agregartrimestrep/', views.agregartrimestrep, name= 'addtrimestrep'),
    path('edittrimestrep', views.edittrimestrep, name= 'edittrimestrep'),
    path('updatetrimestrep/<str:id>', views.updatetrimestrep, name= 'updatetrimestrep'),
    path('elimina-T/<id>/', views.eliminartrip, name= 'eliminartrip'),
    ##################################################Profesor
    path('profesor_m/', views.profesor_m, name= 'profesor_m'),
    # path('editprofesor', views.editprofesor, name= 'editprofesor'),
    # path('updateprofesor/<str:id>', views.updateprofesor, name= 'updateprofesor'),
    path('elimina-Profe/<id>/', views.eliminarprofesor, name= 'eliminarprofesor'),
    ##################################################Materia
    path('materia_m/', views.materia_m, name= 'materia_m'),
    path('agregarmateria/', views.agregarmateria, name= 'addmateria'),
    path('editmateria/', views.editmateria, name= 'editmateria'),
    path('updatemateria/<str:id>', views.updatemateria, name= 'updatemateria'),
    path('elimina-Materia/<id>/', views.eliminarmateria, name= 'eliminarmateria'),
    ##################################################pcm
    path('profecm_m/', views.profecm_m, name= 'profecm_m'),
    path('agregarprofecm/', views.agregarprofecm, name= 'addprofecm'),
    path('editprofecm/', views.editprofecm, name= 'editprofecm'),
    path('updateprofecm/<str:id>', views.updateprofecm, name= 'updateprofecm'),
    path('elimina-profecm/<id>/', views.eliminarprofecm, name= 'eliminarprofecm'),
    ##################################################estudiantes
    path('estudiantes_m/', views.estudiantes_m, name= 'estudiantes_m'),
    # path('updateestudiantes/<str:id>', views.updateestudiantes, name= 'updateestudiantes'),
    path('elimina-Estu/<id>/', views.eliminarestudiantes, name= 'eliminarestudiantes'),
    ##################################################estudiantes
    path('validarm_m/', views.validarm_m, name= 'validarm_m'),
    path('updatevalidarm/<str:id>', views.updatevalidarm, name= 'updatevalidarm'),
    path('elimina-Val/<id>/', views.eliminarvalidarm, name= 'eliminarvalidarm'),
   ########################
   path('notasm_mm/', views.notasm_m, name= 'notasm_mm'),
   
]   
