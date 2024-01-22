from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Rol,rol_user
from ESTUDIANTE.models import*
from PROFESOR.models import*
from ESTUDIANTE.models import trimestre as trimes, parcial as parc, curso as m_curso
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.

# def login(request):
#     return render(request,'login.html')

def index(request):
    return render(request,'index.html')

@login_required
def inicio(request):
    total_users = rol_user.objects.filter(estado=True).count()
    admin=rol_user.objects.filter(estado=True,rol__nombre='ADMINISTRADOR').count()
    estudiantes = rol_user.objects.filter(estado=True,rol__nombre='Estudiante').count()
    profesores = rol_user.objects.filter(estado=True,rol__nombre='Profesor').count()
    return render(request,'inicioAdmin.html', {'total_users': total_users, 'admin': admin,'estudiantes': estudiantes, 'profesores': profesores})

@login_required
def exit(request):
    logout(request)
    return redirect('pagina_principal')


################## Usuario ###################
@login_required
def usuarios(request):  
    objc = User.objects.filter(is_active=True)
    if request.method=="POST":
        username=request.POST.get('username')
        if username=='':
            print("1")
        else:
            print("2")
            objc= User.objects.filter(username=username)        
    return render(request, 'administrador/userRead.html',{'x':objc})
@login_required
def inactivoUsuario(request):
    objc = User.objects.filter(is_active=False)
    if request.method=="POST":
        username=request.POST.get('username')
        if username=='':
            print("1")
        else:
            print("2")
            objc= User.objects.filter(username=username) 

    return render(request,'administrador/inactivo.html',{'xx':objc})

@login_required
def activaU(request, id):
    objeto = User.objects.get(id=id)
    objeto.is_active=True
    objeto.save()
    messages.success(request,"Activado exitoso")
    return redirect('inactivoUsuario')




@login_required
def agregaruser (request):
    if request.method =="POST":
        first_name = request.POST.get('name')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')


        use = User(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username,
            password = make_password(password),
            is_superuser = False,
            is_staff = True
        )
        use.save()
        messages.success(request,"Agregado exitoso")
        return redirect("usuario")
    return render(request, 'administrador/userRead.html')

@login_required
def edituser(request):
    use = User.objects.all()
    context={
        'use':use,
    }
    return redirect(request,'administrador/userRead.html',{'x':context })

@login_required
def update(request, id):
    if request.method =="POST":
        first_name = request.POST.get('name1')
        last_name = request.POST.get('lastname1')
        email = request.POST.get('email1')
        username = request.POST.get('username1')
        password = request.POST.get('password1')


        use = User(
            id = id,
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username,
            password = make_password(password),
            is_superuser = True,
            is_staff = True
        )
        use.save()
        messages.success(request,"Actualización exitoso")
        return redirect('usuario')

    return redirect(request,'administrador/userRead.html')

@login_required
def eliminarU(request, id):
    objeto = User.objects.get(id=id)
    objeto.is_active=False
    objeto.save()
    messages.success(request,"Eliminado exitoso")
    return redirect('usuario')

########################################
@login_required
def roles(request):  
    objc = Rol.objects.all()
    if request.method=="POST":
        nombre=request.POST.get('nombre')
        if nombre=='':
            print("1")
        else:
            print("2")
            objc= Rol.objects.filter(nombre=nombre)        
    return render(request, 'administrador/roles.html',{'x':objc } )



@login_required
def roles1 (request):
    if request.method =="POST":
        nombre = request.POST.get('name')

        use = Rol(
            nombre = nombre,
            estado = True
        )
        use.save()
        messages.success(request,"Agregado exitoso")
        return redirect("roles")
    return render(request, 'administrador/roles.html')

@login_required
def RU(request):
    use = Rol.objects.all()
    context={
        'use':use,
    }
    return redirect(request,'administrador/roles.html',{'x':context })

@login_required
def roles2(request, id):
    if request.method =="POST":
        nombre = request.POST.get('name1')

        use = Rol(
            id = id,
            nombre = nombre,
            estado = True
        )
        
        use.save()
        messages.success(request,"Actualización exitoso")
        return redirect('roles')

    return redirect(request,'administrador/roles.html')

########################################
@login_required
def rolUser(request):
    ro = Rol.objects.filter(estado=True)
    users = User.objects.filter(is_active=True)
    objc = rol_user.objects.filter(estado=True)
    
    if request.method == "POST":
        user = request.POST.get('user')
        if user:
            objc = objc.filter(user=user)

    return render(request, 'administrador/usuario_rol.html', {'x': objc, 'users': users, 'ro':ro})



@login_required
def designar (request):
    if request.method =="POST":
        user = request.POST.get('user')
        rol = request.POST.get('rol')


        ru = rol_user(
            user_id = user,
            rol_id = rol,
            estado = True
        )
        ru.save()
        messages.success(request,"Agregado exitoso")
        return redirect('rolUser')
    return render(request, 'administrador/usuario_rol.html')


@login_required
def updaterolU(request, id):
    if request.method =="POST":
        user = request.POST.get('user1')
        rol = request.POST.get('rol1')


        ru = rol_user(
            id=id,
            user_id = user,
            rol_id = rol,
           
        )
        ru.save()
        messages.success(request,"Actualización exitoso")
        return redirect('rolUser')

    return redirect(request,'administrador/usuario_rol.html')



@login_required
def eliminarRolU(request, id):
    objeto = rol_user.objects.get(id=id)
    objeto.estado = False
    objeto.save()
    messages.success(request,"Eliminado exitoso")
    return redirect('rolUser')



####################################Curso
@login_required
def curso_m (request):  
    objc = curso.objects.filter(estado=True)
    if request.method=="POST":
        nombre_curso=request.POST.get('nombre_curso')
        if nombre_curso=='':
            print("1")
        else:
            print("2")
            objc= curso.objects.filter(nombre_curso=nombre_curso)        
    return render(request, 'administrador/Curso.html',{'x':objc})


@login_required
def agregarcurso(request):
    if request.method =="POST":
        nombre_curso = request.POST.get('name')
    


        cur = curso(
            nombre_curso = nombre_curso,
        )
        cur.save()
        messages.success(request,"Agregado exitoso")
        return redirect("curso_m")
    return render(request, 'administrador/Curso.html')

@login_required
def editcurso(request):
    cur = curso.objects.all()
    context={
        'cur':cur,
    }
    return redirect(request,'administrador/Curso.html',{'x':context })

@login_required
def updatecurso(request, id):
    if request.method =="POST":
        nombre_curso = request.POST.get('name1')



        cur = curso(
            id = id,
            nombre_curso = nombre_curso,

        )
        cur.save()
        messages.success(request,"Actualización exitoso")
        return redirect('curso_m')

    return redirect(request,'administrador/Curso.html')



@login_required
def eliminarcurso(request, id):
    objeto = curso.objects.get(id=id)
    objeto.estado = False
    objeto.save()
    messages.success(request,"Eliminado exitoso")
    return redirect('curso_m')


#####################Jornada
@login_required
def jornada_m (request):  
    objc = jornada.objects.filter(estado=True)
    if request.method=="POST":
        nombre_jornada=request.POST.get('nombre_jornada')
        if nombre_jornada=='':
            print("1")
        else:
            print("2")
            objc= jornada.objects.filter(nombre_jornada=nombre_jornada)        
    return render(request, 'administrador/Jornada.html',{'x':objc})


@login_required
def agregarjornada(request):
    if request.method =="POST":
        nombre_jornada = request.POST.get('name')
    


        cur = jornada(
            nombre_jornada = nombre_jornada,
        )
        cur.save()
        messages.success(request,"Agregado exitoso")
        return redirect("jornada_m")
    return render(request, 'administrador/Jornada.html')

@login_required
def editjornada(request):
    cur = jornada.objects.all()
    context={
        'cur':cur,
    }
    return redirect(request,'administrador/Jornada.html',{'x':context })

@login_required
def updatejornada(request, id):
    if request.method =="POST":
        nombre_jornada = request.POST.get('name1')



        cur = jornada(
            id = id,
            nombre_jornada = nombre_jornada,

        )
        cur.save()
        messages.success(request,"Actualización exitoso")
        return redirect('jornada_m')

    return redirect(request,'administrador/Jornada.html')




@login_required
def eliminarjornada(request, id):
    objeto = jornada.objects.get(id=id)
    objeto.estado = False
    objeto.save()
    messages.success(request,"Eliminado exitoso")
    return redirect('jornada_m')


#####################Paralelo
@login_required
def paralelo_m (request):  
    objc = paralelo.objects.filter(estado=True)
    if request.method=="POST":
        nombre_paralelo=request.POST.get('nombre_paralelo')
        if nombre_paralelo=='':
            print("1")
        else:
            print("2")
            objc= paralelo.objects.filter(nombre_paralelo=nombre_paralelo)        
    return render(request, 'administrador/Paralelo.html',{'x':objc})


@login_required
def agregarparalelo(request):
    if request.method =="POST":
        nombre_paralelo = request.POST.get('name')
    


        cur = paralelo(
            nombre_paralelo = nombre_paralelo,
        )
        cur.save()
        messages.success(request,"Agregado exitoso")
        return redirect("paralelo_m")
    return render(request, 'administrador/Paralelo.html')

@login_required
def editparalelo(request):
    cur = paralelo.objects.all()
    context={
        'cur':cur,
    }
    return redirect(request,'administrador/Paralelo.html',{'x':context })

@login_required
def updateparalelo(request, id):
    if request.method =="POST":
        nombre_paralelo = request.POST.get('name1')



        cur = paralelo(
            id = id,
            nombre_paralelo = nombre_paralelo,

        )
        cur.save()
        messages.success(request,"Actualización exitoso")
        return redirect('paralelo_m')

    return redirect(request,'administrador/Paralelo.html')


@login_required
def eliminarparalelo(request, id):
    objeto = paralelo.objects.get(id=id)
    objeto.estado = False
    objeto.save()
    messages.success(request,"Eliminado exitoso")
    return redirect('paralelo_m')


#####################Periodo
@login_required
def periodo_m (request):  
    objc = periodo.objects.filter(estado=True)
    if request.method=="POST":
        nombre_periodo=request.POST.get('nombre_periodo')
        if nombre_periodo=='':
            print("1")
        else:
            print("2")
            objc= periodo.objects.filter(nombre_periodo=nombre_periodo)        
    return render(request, 'administrador/Periodo.html',{'x':objc})

@login_required
def inactivoUsuarioP(request):
    objc = periodo.objects.filter(estado=False)
    if request.method=="POST":
        nombre_periodo=request.POST.get('nombre_periodo')
        if nombre_periodo=='':
            print("1")
        else:
            print("2")
            objc= periodo.objects.filter(nombre_periodo=nombre_periodo)        
    return render(request, 'administrador/inactivop.html',{'x':objc})



@login_required
def agregarperiodo(request):
    if request.method =="POST":
        nombre_periodo = request.POST.get('name')
    


        cur = periodo(
            nombre_periodo = nombre_periodo,
        )
        cur.save()
        messages.success(request,"Agregado exitoso")
        return redirect("periodo_m")
    return render(request, 'administrador/Periodo.html')

@login_required
def editperiodo(request):
    cur = periodo.objects.all()
    context={
        'cur':cur,
    }
    return redirect(request,'administrador/Perido.html',{'x':context })

@login_required
def updateperiodo(request, id):
    if request.method =="POST":
        nombre_periodo = request.POST.get('name1')



        cur = periodo(
            id = id,
            nombre_periodo = nombre_periodo,

        )
        cur.save()
        messages.success(request,"Actualización exitoso")
        return redirect('periodo_m')

    return redirect(request,'administrador/Periodo.html')


@login_required
def activaP(request, id):
    objeto = periodo.objects.get(id=id)
    objeto.estado=True
    objeto.save()
    messages.success(request,"Activado exitoso")
    return redirect('inactivoUsuarioP')



@login_required
def eliminarperiodo(request, id):
    objeto = periodo.objects.get(id=id)
    objeto.estado = False
    objeto.save()
    messages.success(request,"Eliminado exitoso")
    return redirect('periodo_m')

#################Trimestre/Parcial
@login_required
def trimestrep_m (request):  
    objc = trimestre_parcial.objects.filter(estado=True)
    objc2 = trimes.objects.filter(estado=True)
    objc3 = parcial.objects.filter(estado=True)
    if request.method=="POST":
        trimestre=request.POST.get('trimestre')
        if trimestre=='':
            print("1")
        else:
            print("2")
            objc= trimestre_parcial.objects.filter(trimestre=trimestre)        
    return render(request, 'administrador/TrimestreParcial.html',{'x':objc, 'tri':objc2, 'par':objc3})



@login_required
def agregartrimestrep(request):
    if request.method =="POST":
        trimestre_id = request.POST.get('trimestre')
        trimestre= get_object_or_404(trimes, id=trimestre_id)
        parcial_id= request.POST.get('parcial')
        parcial= get_object_or_404(parc, id=parcial_id)
    


        cur = trimestre_parcial(
            trimestre = trimestre,
            parcial=parcial
        )
        cur.save()
        messages.success(request,"Agregado exitoso")
        return redirect("trimestrep_m")
    return render(request, 'administrador/TrimestreParcial.html')

@login_required
def edittrimestrep(request):
    cur = trimestre_parcial.objects.all()
    context={
        'cur':cur,
    }
    return redirect(request,'administrador/TrimestreParcial.html',{'x':context })

@login_required
def updatetrimestrep(request, id):
    if request.method =="POST":
        trimestre_id = request.POST.get('tri1')
        trimestre= get_object_or_404(trimes, id=trimestre_id)
        parcial_id= request.POST.get('parcial1')
        parcial= get_object_or_404(parc, id=parcial_id)



        cur = trimestre_parcial(
            id = id,
            trimestre = trimestre,
            parcial=parcial

        )
        cur.save()
        messages.success(request,"Actualización exitoso")
        return redirect('trimestrep_m')

    return redirect(request,'administrador/TrimestreParcial.html')


@login_required
def eliminartrip(request, id):
    objeto = trimestre_parcial.objects.get(id=id)
    objeto.estado = False
    objeto.save()
    messages.success(request,"Eliminado exitoso")
    return redirect('trimestrep_m')



######################################profesor
@login_required
def profesor_m (request):  
    objc = profesor.objects.filter(estado=True)
    if request.method=="POST":
        usuario_id=request.POST.get('usuario_id')
        if usuario_id=='':
            print("1")
        else:
            print("2")
            objc= profesor.objects.filter(usuario_id=usuario_id)        
    return render(request, 'administrador/profesores.html',{'x':objc })


# @login_required
# def updateprofesor(request, id):
#     if request.method =="POST":
#         usuario_ids=request.POST.get('usuario_id')
#         usuario_id= get_object_or_404(User, id=usuario_ids)
#         nombre = request.POST.get('name')
#         apellido= request.POST.get('apellido')
#         tipo_documentos=request.POST.get('usuario_id')
#         tipo_doc= get_object_or_404(tipo_documento, id=tipo_documentos)

#         tipo_documentos=request.POST.get('usuario_id')
#         tipo_doc= get_object_or_404(tipo_documento, id=tipo_documentos)
#         tipo_documentos=request.POST.get('usuario_id')
#         tipo_doc= get_object_or_404(tipo_documento, id=tipo_documentos)

#         cur = profesor(
#             id=id,
#             usuario_id = usuario_id,
#             nombre = nombre,
#             tipo_doc=tipo_doc,
#             apellido=apellido,
#             apellido=apellido

#         )
#         cur.save()
#         messages.success(request,"Modicado exitoso")
#         return redirect('profesor_m')

#     return redirect(request,'administrador/profesores.html')


@login_required
def eliminarprofesor(request, id):
    objeto = profesor.objects.get(id=id)
    objeto.estado = False
    objeto.save()
    messages.success(request,"Eliminado exitoso")
    return redirect('profesor_m')
#############################materia  
@login_required  
def materia_m (request):  
    objc = materia.objects.filter(estado=True)
    if request.method=="POST":
        nombre_materia=request.POST.get('nombre')
        if nombre_materia=='':
            print("1")
        else:
            print("2")
            objc= materia.objects.filter(nombre_materia=nombre_materia)        
    return render(request, 'administrador/materia.html',{'x':objc})


@login_required
def agregarmateria(request):
    if request.method =="POST":
        nombre_materia = request.POST.get('name')
    

        cur = materia(
            nombre_materia = nombre_materia,
        )
        cur.save()
        messages.success(request,"Agregado exitoso")
        return redirect("materia_m")
    return render(request, 'administrador/materia.html')

@login_required
def editmateria(request):
    cur = materia.objects.all()
    context={
        'cur':cur,
    }
    return redirect(request,'administrador/materia.html',{'x':context })

@login_required
def updatemateria(request, id):
    if request.method =="POST":
        nombre_materia = request.POST.get('name1')



        cur = materia(
            id = id,
            nombre_materia = nombre_materia,

        )
        cur.save()
        messages.success(request,"Actualización exitoso")
        return redirect('materia_m')

    return redirect(request,'administrador/materia.html')

@login_required
def eliminarmateria(request, id):
    objeto = materia.objects.get(id=id)
    objeto.estado = False
    objeto.save()
    messages.success(request,"Eliminado exitoso")
    return redirect('materia_m')

####################################Profesor/Curso/Materia
@login_required
def profecm_m (request):  
    objc = profesor_cur_materia.objects.filter(estado=True,periodo__estado=True)
    objc2 = curso_paralelo.objects.all()
    objc3 = materia.objects.all()
    objc4 = profesor.objects.all()
    obj5 = jornada.objects.all()
    obj6 = periodo.objects.filter(estado=True)
    if request.method=="POST":
        curso=request.POST.get('curso')
        if trimestre=='':
            print("1")
        else:
            print("2")
            objc= profesor_cur_materia.objects.filter(curso=curso)        
    return render(request, 'administrador/profeCM.html',{'x':objc, 'cupa':objc2, 'mat':objc3,'pr':objc4,'cinco':obj5,'seis':obj6})



@login_required
def agregarprofecm(request):
    if request.method =="POST":
        cupa_id = request.POST.get('curso')
        cursos= get_object_or_404(curso_paralelo, id=cupa_id)
        materia_id= request.POST.get('materia')
        mate= get_object_or_404(materia, id=materia_id)
        profesor_id= request.POST.get('profesor')
        profe= get_object_or_404(profesor, id=profesor_id)
        jornada_id= request.POST.get('jornada')
        jor= get_object_or_404(jornada, id=jornada_id)
        periodo_id= request.POST.get('periodo')
        per= get_object_or_404(periodo, id=periodo_id)
    

        cur = profesor_cur_materia(
            curso_paralelo = cursos,
            materia=mate,
            profesor=profe,
            jornada= jor,
            periodo= per
        )
        cur.save()
        messages.success(request,"Agregado exitoso")
        return redirect("profecm_m")
    return render(request, 'administrador/profeCM.html')

@login_required
def editprofecm(request):
    cur = profesor_cur_materia.objects.all()
    context={
        'cur':cur,
    }
    return redirect(request,'administrador/profeCM.html',{'x':context })

@login_required
def updateprofecm(request, id):
    if request.method =="POST":
        cupa_id = request.POST.get('curso1')
        cursos= get_object_or_404(curso_paralelo, id=cupa_id)
        materia_id= request.POST.get('materia1')
        mate= get_object_or_404(materia, id=materia_id)
        profesor_id= request.POST.get('profesor1')
        profe= get_object_or_404(profesor, id=profesor_id)
        jornada_id= request.POST.get('jornada1')
        jor= get_object_or_404(jornada, id=jornada_id)
        periodo_id= request.POST.get('periodo1')
        per= get_object_or_404(periodo, id=periodo_id)
    

        cur = profesor_cur_materia(
            id = id,
            curso_paralelo = cursos,
            materia=mate,
            profesor=profe,
            jornada= jor,
            periodo= per
        )
        cur.save()
        messages.success(request,"Actualización exitoso")
        return redirect('profecm_m')

    return redirect(request,'administrador/profeCM.html')

@login_required
def eliminarprofecm(request, id):
    objeto = profesor_cur_materia.objects.get(id=id)
    objeto.estado = False
    objeto.save()
    messages.success(request,"Eliminado exitoso")
    return redirect('profecm_m')
######################################Estudiante
@login_required
def estudiantes_m (request):  
    objc = estudiantes.objects.filter(estado=True)
    if request.method=="POST":
        nombre=request.POST.get('nombre')
        if nombre=='':
            print("1")
        else:
            print("2")
            objc= estudiantes.objects.filter(nombre=nombre)        
    return render(request, 'administrador/estudiante.html',{'x':objc })


# @login_required
# def updateestudiantes(request, id):
#     if request.method =="POST":
#         usuario_ids=request.POST.get('usuario_id')
#         usuario_id= get_object_or_404(User, id=usuario_ids)
#         nombre = request.POST.get('name')
#         apellido= request.POST.get('apellido')



#         cur = profesor(
#             id=id,
#             usuario_id = usuario_id,
#             nombre = nombre,
#             apellido=apellido

#         )
#         cur.save()
#         messages.success(request,"Modicado exitoso")
#         return redirect('profesor_m')

#     return redirect(request,'administrador/profesores.html')


@login_required
def eliminarestudiantes(request, id):
    objeto = estudiantes.objects.get(id=id)
    objeto.estado = False
    objeto.save()
    messages.success(request,"Eliminado exitoso")
    return redirect('estudiantes_m')

#############################validar matri estu


@login_required
def validarm_m (request):  
    objc = matricula.objects.filter(estado=False)
    objc2 = periodo.objects.filter(estado=True)
    objc3 = jornada.objects.all()
    objc4 = curso_paralelo.objects.all()

    if request.method=="POST":
        estudiante=request.POST.get('estudiante')
        if estudiante=='':
            print("1")
        else:
            print("2")
            objc= matricula.objects.filter(estudiante=estudiante)        
    return render(request, 'administrador/validarMatri.html',{'x':objc,'x2':objc2,'x3':objc3 ,'x4':objc4 })

@login_required
def updatevalidarm(request, id):
    if request.method =="POST":
        estudi= request.POST.get('name1')
        estudiante= get_object_or_404(estudiantes, id=estudi)
        pe = request.POST.get('periodo')
        peri= get_object_or_404(periodo, id=pe)
        jor= request.POST.get('jornada')
        jorna= get_object_or_404(jornada, id=jor)
        cursp= request.POST.get('cursop')
        cursop= get_object_or_404(curso_paralelo, id=cursp)
        estado= request.POST.get('estado')
    

        cur = matricula(
            id = id,
            estudiante = estudiante,
            periodo=peri,
            jornada=jorna,
            curso_paralelo= cursop,
            estado=estado
        )
        cur.save()
        messages.success(request,"Actualización exitoso")
        return redirect('validarm_m')

    return redirect(request,'administrador/profeCM.html')

@login_required
def eliminarvalidarm(request, id):
    objeto = matricula.objects.get(id=id)
    objeto.estado = False
    objeto.save()
    messages.success(request,"Eliminado exitoso")
    return redirect('validarm_m')


#####mostrar notas estu
@login_required
def notasm_m (request): 
    objc = notas.objects.filter(estado=True)      
    return render(request, 'administrador/nota.html',{'x':objc })

