from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from ESTUDIANTE.models import *
from .models import matricula 
from ESTUDIANTE.models import  matricula as matr
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.


@login_required
def mostrarp(request,id):
    try:
        profe= profesor.objects.get(usuario_id=id)
        obj1= tipo_documento.objects.all()
        obj2= genero.objects.all()
        obj3= etnia.objects.all()
        obj4= tipo_sangre.objects.all()
        return render(request,'update.html',{'pr':profe,'uno':obj1,'dos':obj2,'tres':obj3,'cuatro':obj4})
    
    except profesor.DoesNotExist:
        obj1= tipo_documento.objects.all()
        obj2= genero.objects.all()
        obj3= etnia.objects.all()
        obj4= tipo_sangre.objects.all()
        return render(request,'actualizar.html',{'uno':obj1,'dos':obj2,'tres':obj3,'cuatro':obj4})


@login_required
def savep(request):
    if request.method =="POST":
        usuarioo = request.POST.get('id_usuario')
        usuario= get_object_or_404(User, id=usuarioo)
        nombre= request.POST.get('nombre')
        apellido= request.POST.get('apellido')
        estado_civil= request.POST.get('estado_civil')
        documneto_id= request.POST.get('documento')
        tipo_document= get_object_or_404(tipo_documento, id=documneto_id)
        N_documento=request.POST.get('CI')
        genero_id= request.POST.get('genero')
        gener= get_object_or_404(genero, id=genero_id)
        nacionalidad= request.POST.get('nacionalidad')
        fecha_nacimiento=request.POST.get('fecha')
        etnia_id= request.POST.get('etnia')
        etni= get_object_or_404(etnia, id=etnia_id)
        sangre_id= request.POST.get('sangre')
        sangre= get_object_or_404(tipo_sangre, id=sangre_id)
        direccion= request.POST.get('direccion')
        correo= request.POST.get('correo')
        telefono= request.POST.get('telefono')
        especialidad= request.POST.get('especialidad')
        discapacidad= request.POST.get('discapacidad')
        tipo_dis=request.POST.get('tipo_dis')
        carnet=request.POST.get('carnet')
        imagenn= request.FILES.get('txt')

        pro = profesor(
            usuario_id = usuario,
            nombre = nombre,
            apellido=apellido,
            estado_civil= estado_civil,
            tipo_documento= tipo_document,
            N_documento= N_documento,
            genero= gener,
            nacionalidad= nacionalidad,
            nacimiento_fecha= fecha_nacimiento,
            etnia=etni,
            direccion= direccion,
            correo=correo,
            telefono=telefono,
            especialidad=especialidad,
            tipo_sangre= sangre,
            tiene_discapacidad= discapacidad,
            tipo_discapacidad= tipo_dis,
            carnet_discapacidad= carnet,
            imagen = imagenn
        )
        pro.save()
        messages.success(request,"Registro exitoso")
        return redirect('inicio')
    
@login_required
def modificar_pr(request, id):
    if request.method =="POST":
        usuarioo = request.POST.get('id_usuario')
        usuario= get_object_or_404(User, id=usuarioo)
        nombre= request.POST.get('nombre')
        apellido= request.POST.get('apellido')
        estado_civil= request.POST.get('estado_civil')
        documneto_id= request.POST.get('documento')
        tipo_document= get_object_or_404(tipo_documento, id=documneto_id)
        N_documento=request.POST.get('CI')
        genero_id= request.POST.get('genero')
        gener= get_object_or_404(genero, id=genero_id)
        nacionalidad= request.POST.get('nacionalidad')
        fecha_nacimiento=request.POST.get('fecha')
        etnia_id= request.POST.get('etnia')
        etni= get_object_or_404(etnia, id=etnia_id)
        sangre_id= request.POST.get('sangre')
        sangre= get_object_or_404(tipo_sangre, id=sangre_id)
        direccion= request.POST.get('direccion')
        correo= request.POST.get('correo')
        telefono= request.POST.get('telefono')
        especialidad= request.POST.get('especialidad')
        discapacidad= request.POST.get('discapacidad')
        tipo_dis=request.POST.get('tipo_dis')
        carnet=request.POST.get('carnet')
        imagenn= request.FILES.get('txt')

        pro = profesor(
            id=id,
            usuario_id = usuario,
            nombre = nombre,
            apellido=apellido,
            estado_civil= estado_civil,
            tipo_documento= tipo_document,
            N_documento= N_documento,
            genero= gener,
            nacionalidad= nacionalidad,
            nacimiento_fecha= fecha_nacimiento,
            etnia=etni,
            direccion= direccion,
            correo=correo,
            telefono=telefono,
            especialidad=especialidad,
            tipo_sangre= sangre,
            tiene_discapacidad= discapacidad,
            tipo_discapacidad= tipo_dis,
            carnet_discapacidad= carnet,
            imagen = imagenn
        )
        pro.save()
        messages.success(request,"Actualización exitoso")
        return redirect('inicio')
    



# def nota(request):
#     obj = curso_paralelo.objects.all()
#     obj2 = periodo.objects.all()
#     matricu = matricula.objects.all()
#     obj3 = trimestre_parcial.objects.all()
#     obj4= materia.objects.all()

#     buscar1 = request.GET.get('cp')
#     buscar2 = request.GET.get('pe')

#     if buscar1 and buscar2:
#         matricu = matricula.objects.filter(curso_paralelo=buscar1, periodo=buscar2)
#         print(buscar1,buscar2,"-------------------------------")

#     return render(request, 'notapro.html', {'cp': obj, 'pe': obj2, 'est': matricu,'tr':obj3,'ma':obj4})



# def AGG_NOTA(request):
#     if request.method == "POST":
#         est_ids = request.POST.get('est_ids').split(',')  
#         trimestre_parcial_id = request.POST.get('tp')
#         tri_par = get_object_or_404(trimestre_parcial, id=trimestre_parcial_id)
        
#         materia_id = request.POST.get('mat')
#         mater = get_object_or_404(materia, id=materia_id)
        
#         usuario = request.POST.get('usuario')
        
#         for est_id in est_ids:
#             matricula = get_object_or_404(matr, id=est_id)
#             nota = request.POST.get(f'notax_{est_id}')
            
#             notasds = notas(
#                 matricula=matricula,
#                 trimestre_parcial=tri_par,
#                 materia=mater,
#                 puntaje=nota,
#                 registro=usuario,
#             )
#             notasds.save()
        
#         messages.success(request, "Agregado exitoso")
#         return redirect('inicio')

# def CONSULTAR_NO(request):
#     obj = curso_paralelo.objects.all()
#     obj2 = periodo.objects.all()
#     obj3 = trimestre_parcial.objects.all()
#     obj4 = materia.objects.all()

#     buscar1 = request.GET.get('cp')
#     buscar2 = request.GET.get('pe')
#     buscar3 = request.GET.get('tp')
#     buscar4 = request.GET.get('mat')

#     notaaa = None

#     if buscar1 and buscar2 and buscar3 and buscar4:
#         matriculas = matricula.objects.filter(curso_paralelo_id=buscar1, periodo_id=buscar2)

#         if matriculas.exists():
#             matricula_ids = matriculas.values_list('id', flat=True)
#             notaaa = notas.objects.filter(matricula__in=matricula_ids, trimestre_parcial_id=buscar3, materia_id=buscar4)
#             return render(request, 'modificar_nota.html', {'not': notaaa})

#     return render(request, 'consulta_nota.html', {'cp': obj, 'pe': obj2, 'tr': obj3, 'ma': obj4})

# def modificarN(request, id):
#     if request.method =="POST":
#         matri_id=request.POST.get('matricula')
#         matri= get_object_or_404(matricula, id=matri_id)
#         tri_id=request.POST.get('trimestre')
#         tri= get_object_or_404(trimestre_parcial, id=tri_id)
#         mate_id=request.POST.get('materia')
#         mate= get_object_or_404(materia, id=mate_id)
#         registro = request.POST.get('registro')
#         puntaje = request.POST.get('puntaje')




#         use = notas(
#             id = id,
#             matricula=matri,
#             trimestre_parcial = tri,
#             materia = mate  ,
#             registro=registro,
#             puntaje = puntaje,

#         )
#         use.save()
#         messages.success(request,"Modicado exitoso")
#         return redirect('inicio')

#     return redirect(request,'modificar_nota.html')

@login_required
def nota(request,id):

    try:
        pro= profesor.objects.get(usuario_id=id)
        pro_id = pro.id
        asign= profesor_cur_materia.objects.filter(profesor=pro_id,periodo__estado=True)
        return render(request,'notapro.html',{'pro':asign})
    except profesor.DoesNotExist:
        messages.warning(request, "Registre sus datos")
        return redirect('inicio')


# def nota1(request,id):
#     try:
#         pcm= profesor_cur_materia.objects.get(id=id)
#         cp= pcm.curso_paralelo.id
#         jor= pcm.jornada.id
#         pe= pcm.periodo.id
#         ma= pcm.materia.id
#         matri= matricula.objects.filter(curso_paralelo=cp,jornada=jor,periodo=pe)
#         matri_id=matri.id
#         nota= notas.objects.filter(matricula=matri_id,jornada=jor,materia=ma)
#         return render(request,'nota2.html',{'x': nota})
#     except notas.DoesNotExist:    
#         pcm= profesor_cur_materia.objects.get(id=id)
#         cp= pcm.curso_paralelo.id
#         jor= pcm.jornada.id
#         pe= pcm.periodo.id
#         matri= matricula.objects.filter(curso_paralelo=cp,jornada=jor,periodo=pe)
        
#         return render(request,'nota1.html',{'x': matri,'p':pcm})

# def nota1(request, id):
#     try:
#         pcm = get_object_or_404(profesor_cur_materia, id=id)
#         matri = matricula.objects.filter(curso_paralelo=pcm.curso_paralelo, jornada=pcm.jornada, periodo=pcm.periodo)
#         nota = notas.objects.filter(matricula__in=matri, jornada=pcm.jornada, materia=pcm.materia)
#         return render(request, 'nota2.html', {'x': nota,'p': pcm})
#     except notas.DoesNotExist:
#         pcm = get_object_or_404(profesor_cur_materia, id=id)
#         matri = matricula.objects.filter(curso_paralelo=pcm.curso_paralelo, jornada=pcm.jornada, periodo=pcm.periodo)
#         return render(request, 'nota1.html', {'x': matri, 'p': pcm})
@login_required
def nota1(request, id):
    pcm = get_object_or_404(profesor_cur_materia, id=id)
    matri = matricula.objects.filter(curso_paralelo=pcm.curso_paralelo, jornada=pcm.jornada, periodo=pcm.periodo, estado=True)
    nota = notas.objects.filter(matricula__in=matri, jornada=pcm.jornada, materia=pcm.materia)

    if nota.exists():
        return render(request, 'nota2.html', {'x': nota, 'p': pcm})
    else:
        return render(request, 'nota1.html', {'x': matri, 'p': pcm})
@login_required
def AGG_NOTA(request):
    if request.method == "POST":
        est_ids = request.POST.get('est_ids').split(',')  
        jor_id = request.POST.get('jornada')
        mater_id = request.POST.get('materia')
        usuario = request.POST.get('usuario')

        jor = get_object_or_404(jornada, id=jor_id)
        mater = get_object_or_404(materia, id=mater_id)
        
        for est_id in est_ids:
            matricul = get_object_or_404(matricula, id=est_id)
            nota1 = float(request.POST.get(f'nota1_{est_id}'))
            nota2 = float(request.POST.get(f'nota2_{est_id}'))
            nota3 = float(request.POST.get(f'nota3_{est_id}'))

            nota_final = (nota1 + nota2 + nota3) / 3.0
            
            notasds = notas(
                matricula=matricul,
                jornada=jor,
                materia=mater,
                puntaje1=nota1,
                puntaje2=nota2,
                puntaje3=nota3,
                promedio_general=nota_final,
                registro=usuario,
            )
            notasds.save()
        
        messages.success(request, "Agregado exitoso")
        return redirect('inicio')
    
@login_required
def MODI_NOTA(request):
    if request.method == "POST":
        id = request.POST.get('est_ids').split(',')  
        jor_id = request.POST.get('jornada')
        mater_id = request.POST.get('materia')
        usuario = request.POST.get('usuario')

        jor = get_object_or_404(jornada, id=jor_id)
        mater = get_object_or_404(materia, id=mater_id)
        
        for est_id in id:
            matri_id = request.POST.get(f'matriculax_{est_id}')
            matricul=get_object_or_404(matricula, id=matri_id)
            nota1 = float(request.POST.get(f'nota1_{est_id}').replace(',','.'))
            nota2 = float(request.POST.get(f'nota2_{est_id}').replace(',','.'))
            nota3 = float(request.POST.get(f'nota3_{est_id}').replace(',','.'))

            nota_final = (nota1 + nota2 + nota3) / 3.0
            
            notasds = notas(
                id=est_id,
                matricula=matricul,
                jornada=jor,
                materia=mater,
                puntaje1=nota1,
                puntaje2=nota2,
                puntaje3=nota3,
                promedio_general=nota_final,
                registro=usuario,
            )
            notasds.save()
        
        messages.success(request, "Agregado exitoso")
        return redirect('inicio')    