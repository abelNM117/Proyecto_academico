from django.shortcuts import render, redirect
from .models import estudiantes, tipo_documento as tipoDoc,tipo_sangre as tipoSan, etnia as et
from .models import genero as xd
from .models import *
from PROFESOR.models import*
from .models import periodo as pero, jornada as jor, curso_paralelo as cp
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def actualizacionEstudiante(request, id):
    try:

        estudiante = estudiantes.objects.get(usuariox=id)
        obj=  tipo_sangre.objects.all()
        obj2=  etnia.objects.all()
        return render(request, 'modificar.html', {'est': estudiante,'ts':obj,'et':obj2})
    
    except estudiantes.DoesNotExist: 

        obj=  tipo_sangre.objects.all()
        obj2=  etnia.objects.all()
        return render(request,'actualizacion.html',{'ts':obj, 'et':obj2})

@login_required
def add_est(request):
    if request.method =="POST":
        id_usuario_id= request.POST.get('id_usuario')
        id_usuario= get_object_or_404(User, id=id_usuario_id)
        nombre= request.POST.get('nombre_est')
        apellidos= request.POST.get('apellido_est')
        documento = request.POST.get('numero_est')
        nacimiento_fecha= request.POST.get('fecha_est')
        correo= request.POST.get('email_est')
        direccion = request.POST.get('dir_est')
        celular = request.POST.get('celular_est')
        nacionalidad = request.POST.get('nacional_est')
        dtest_edad =  request.POST.get('edad_est')
        repre_cedula = request.POST.get('numero_rep')
        repre_nomape = request.POST.get('nombre_rep')
        repre_celular = request.POST.get('celular_rep')
        repre_convencional = request.POST.get('tel_rep')
        repre_gmail = request.POST.get('email_rep')
        madre_cedula = request.POST.get('numero_rep')
        madre_nomape =  request.POST.get('nombre_mom')
        infmadre_celular = request.POST.get('celular_mom')
        infmadre_convencional = request.POST.get('tel_mom')
        infmadre_gmail = request.POST.get('email_mom')
        infpadre_cedula = request.POST.get('cedula_dad')
        infpadre_nomap = request.POST.get('nombre_dad')
        infpadre_celular =  request.POST.get('celular_dad')
        infpadre_convencional =  request.POST.get('tel_dad')
        infpadre_gmail = request.POST.get('email_dad')
        estsalud_alergias =request.POST.get('alergia')
        estsalud_tipoalerg = request.POST.get('tipo_alergia')
        tiene_discapacidad= request.POST.get('discapacidad')
        estsalud_vacuna19 = request.POST.get('vacuna')
        estsalud_discapatipo = request.POST.get('tipo_discapacidad')
        estemergencia_numerocell1 = request.POST.get('numero_1')
        estemergencia_nombre1 =  request.POST.get('nombre_1')
        estemergencia_numcell2 = request.POST.get('numero_2')
        estemergencia_nombre2 = request.POST.get('nombre_2')
        genero_id= request.POST.get('genero_est')
        genero = get_object_or_404(xd, id=genero_id)
        tipo_documento_id= request.POST.get('docum_est')
        tipo_documento = get_object_or_404(tipoDoc, id=tipo_documento_id)
        tipo_sangre_id =request.POST.get('tipo_sangre')
        tipo_sangre=get_object_or_404(tipoSan, id=tipo_sangre_id)
        etnia_id = request.POST.get('etnia_est')
        etnia=get_object_or_404(et, id=etnia_id)
        imagenn= request.FILES.get('txt')


        est = estudiantes(
            nombre= nombre,
            apellido=  apellidos,
            documento =  documento,
            nacimiento_fecha= nacimiento_fecha,
            correo= correo,
            direccion = direccion,
            celular =  celular,
            nacionalidad = nacionalidad,
            dtest_edad =  dtest_edad,
            repre_cedula = repre_cedula,
            repre_nomape =  repre_nomape,
            repre_celular = repre_celular,
            repre_convencional = repre_convencional,
            repre_gmail = repre_gmail,
            madre_cedula = madre_cedula,
            madre_nomape =  madre_nomape,
            infmadre_celular = infmadre_celular,
            infmadre_convencional = infmadre_convencional,
            infmadre_gmail = infmadre_gmail,
            infpadre_cedula =  infpadre_cedula,
            infpadre_nomap =  infpadre_nomap,
            infpadre_celular = infpadre_celular,
            infpadre_convencional =  infpadre_convencional,
            infpadre_gmail = infpadre_gmail,
            estsalud_alergias = estsalud_alergias,
            estsalud_tipoalerg = estsalud_tipoalerg,
            estsalud_vacuna19 =  estsalud_vacuna19,
            tiene_discapacidad =  tiene_discapacidad,
            estsalud_discapatipo = estsalud_discapatipo,
            estemergencia_numerocell1 = estemergencia_numerocell1,
            estemergencia_nombre1 =  estemergencia_nombre1,
            estemergencia_numcell2 = estemergencia_numcell2,
            estemergencia_nombre2 = estemergencia_nombre2,
            tipo_documento= tipo_documento,
            tipo_sangre = tipo_sangre,
            etnia =  etnia,
            genero = genero,
            usuariox= id_usuario,
            imagen=imagenn

        )
        print(est)
        est.save()
        messages.success(request,"Guardado exitoso")
        return redirect('inicio')
    return render(request, 'actualizacion.html')

@login_required
def modificar_est(request, id):
    if request.method =="POST":
        id_usuario_id= request.POST.get('id_usuario')
        id_usuario= get_object_or_404(User, id=id_usuario_id)
        nombre= request.POST.get('nombre_est')
        apellidos= request.POST.get('apellido_est')
        documento = request.POST.get('numero_est')
        nacimiento_fecha= request.POST.get('fecha_est')
        correo= request.POST.get('email_est')
        direccion = request.POST.get('dir_est')
        celular = request.POST.get('celular_est')
        nacionalidad = request.POST.get('nacional_est')
        dtest_edad =  request.POST.get('edad_est')
        repre_cedula = request.POST.get('numero_rep')
        repre_nomape = request.POST.get('nombre_rep')
        repre_celular = request.POST.get('celular_rep')
        repre_convencional = request.POST.get('tel_rep')
        repre_gmail = request.POST.get('email_rep')
        madre_cedula = request.POST.get('numero_rep')
        madre_nomape =  request.POST.get('nombre_mom')
        infmadre_celular = request.POST.get('celular_mom')
        infmadre_convencional = request.POST.get('tel_mom')
        infmadre_gmail = request.POST.get('email_mom')
        infpadre_cedula = request.POST.get('cedula_dad')
        infpadre_nomap = request.POST.get('nombre_dad')
        infpadre_celular =  request.POST.get('celular_dad')
        infpadre_convencional =  request.POST.get('tel_dad')
        infpadre_gmail = request.POST.get('email_dad')
        estsalud_alergias =request.POST.get('alergia')
        estsalud_tipoalerg = request.POST.get('tipo_alergia')
        tiene_discapacidad= request.POST.get('discapacidad')
        estsalud_vacuna19 = request.POST.get('vacuna')
        estsalud_discapatipo = request.POST.get('tipo_discapacidad')
        estemergencia_numerocell1 = request.POST.get('numero_1')
        estemergencia_nombre1 =  request.POST.get('nombre_1')
        estemergencia_numcell2 = request.POST.get('numero_2')
        estemergencia_nombre2 = request.POST.get('nombre_2')
        genero_id= request.POST.get('genero_est')
        genero = get_object_or_404(xd, id=genero_id)
        tipo_documento_id= request.POST.get('docum_est')
        tipo_documento = get_object_or_404(tipoDoc, id=tipo_documento_id)
        tipo_sangre_id =request.POST.get('tipo_sangre')
        tipo_sangre=get_object_or_404(tipoSan, id=tipo_sangre_id)
        etnia_id = request.POST.get('etnia_est')
        etnia=get_object_or_404(et, id=etnia_id)
        imagenn= request.FILES.get('txt')


        est = estudiantes(
            id=id,
            nombre= nombre,
            apellido=  apellidos,
            documento =  documento,
            nacimiento_fecha= nacimiento_fecha,
            correo= correo,
            direccion = direccion,
            celular =  celular,
            nacionalidad = nacionalidad,
            dtest_edad =  dtest_edad,
            repre_cedula = repre_cedula,
            repre_nomape =  repre_nomape,
            repre_celular = repre_celular,
            repre_convencional = repre_convencional,
            repre_gmail = repre_gmail,
            madre_cedula = madre_cedula,
            madre_nomape =  madre_nomape,
            infmadre_celular = infmadre_celular,
            infmadre_convencional = infmadre_convencional,
            infmadre_gmail = infmadre_gmail,
            infpadre_cedula =  infpadre_cedula,
            infpadre_nomap =  infpadre_nomap,
            infpadre_celular = infpadre_celular,
            infpadre_convencional =  infpadre_convencional,
            infpadre_gmail = infpadre_gmail,
            estsalud_alergias = estsalud_alergias,
            estsalud_tipoalerg = estsalud_tipoalerg,
            estsalud_vacuna19 =  estsalud_vacuna19,
            tiene_discapacidad =  tiene_discapacidad,
            estsalud_discapatipo = estsalud_discapatipo,
            estemergencia_numerocell1 = estemergencia_numerocell1,
            estemergencia_nombre1 =  estemergencia_nombre1,
            estemergencia_numcell2 = estemergencia_numcell2,
            estemergencia_nombre2 = estemergencia_nombre2,
            tipo_documento= tipo_documento,
            tipo_sangre = tipo_sangre,
            etnia =  etnia,
            genero = genero,
            usuariox= id_usuario,
            imagen = imagenn

        )
        est.save()
        messages.success(request,"Actualización exitoso")
        return redirect('inicio')
    return render(request, 'modificar.html')


# @login_required
# def matri_cula(request, id):
#     try:
#         estudiant = estudiantes.objects.get(usuariox=id)
#         estudiante_id = estudiant.id
#         print(estudiante_id, "uno-----------------------------------")
#         try:
#             matri = matricula.objects.filter(estudiante=estudiante_id)
#             matri_id = matri.id
#             print(matri_id, "dos-----------------------------------")
#             per = periodo.objects.filter(id=matri.periodo.id).first()
#             if per.estado == False or per.estado == 0:
#                 obj2 = periodo.objects.filter(estado=True)
#                 obj3 = jornada.objects.all()
#                 obj4 = curso_paralelo.objects.all()
#                 return render(request, 'matricula.html', {'est': estudiant, 'uno': obj2, 'dos': obj3, 'tres': obj4})
#             else:
#                 messages.success(request,"Tu matricula ya existe")
#                 return redirect('inicio')
            
#         except matricula.DoesNotExist:
#             obj2 = periodo.objects.all()
#             obj3 = jornada.objects.all()
#             obj4 = curso_paralelo.objects.all()
#             return render(request, 'matricula.html', {'est': estudiant, 'uno': obj2, 'dos': obj3, 'tres': obj4})
#     except estudiantes.DoesNotExist:
#         messages.warning(request,"Ingrese primero sus datos")
#         return redirect('inicio')
    

@login_required
def matri_cula(request, id):
    try:
        estudiant = estudiantes.objects.get(usuariox=id)
        estudiante_id = estudiant.id
        print(estudiante_id, "uno-----------------------------------")
        
        while True:
            try:
                matri = matricula.objects.filter(estudiante=estudiante_id, periodo__estado=True).first()
                
                if matri:
                    messages.success(request, "Tu matrícula ya existe")
                    return redirect('inicio')
                else:
                    obj2 = periodo.objects.filter(estado=True)
                    obj3 = jornada.objects.all()
                    obj4 = curso_paralelo.objects.all()
                    return render(request, 'matricula.html', {'est': estudiant, 'uno': obj2, 'dos': obj3, 'tres': obj4})
                
            except matricula.DoesNotExist:
                obj2 = periodo.objects.filter(estado=True)
                obj3 = jornada.objects.all()
                obj4 = curso_paralelo.objects.all()
                return render(request, 'matricula.html', {'est': estudiant, 'uno': obj2, 'dos': obj3, 'tres': obj4})
    
    except estudiantes.DoesNotExist:
        messages.warning(request, "Ingrese primero sus datos")
        return redirect('inicio')


@login_required
def agg_matri(request):
    if request.method =="POST":
        estudiante_id= request.POST.get('estudiante')
        estudiante = get_object_or_404(estudiantes, id=estudiante_id)
        periodo_id = request.POST.get('periodo')
        periodo= get_object_or_404(pero,id=periodo_id)
        jornada_id = request.POST.get('jornada')
        jornada= get_object_or_404(jor, id=jornada_id)
        curso_para_id = request.POST.get('cupa')
        curso_paralelo = get_object_or_404(cp,id=curso_para_id)


        ma = matricula(
            estudiante = estudiante,
            periodo=periodo,
            jornada= jornada,
            curso_paralelo=curso_paralelo

        )
        ma.save()
        messages.success(request,"Registro exitoso")
        return redirect('inicio')





@login_required
def notasm_m (request,id): 
    try: 
        estudiant = estudiantes.objects.get(usuariox=id)
        estudiante_id = estudiant.id
        while True:
            matri = matricula.objects.filter(estudiante=estudiante_id, periodo__estado=True).first()
            if matri:
                matri_id = matri.id
                objc = notas.objects.filter(matricula=matri_id)
                return render(request, 'nota.html',{'x':objc })
            else: 
                messages.warning(request,"No esta matriculado")
                return redirect('inicio')
    except estudiantes.DoesNotExist:
        messages.warning(request,"Ingrese primero sus datos")
        return redirect('inicio')