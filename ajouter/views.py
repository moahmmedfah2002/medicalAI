from django.shortcuts import render
from django.http import HttpResponse
from .classe_assistant import insertion_assistante ,modification_assistante,suppression_assistante
from .classe_medecin import insertion_medcin ,modification_medcin,suppression_medcin


# Create your views here.


def ajouter(request):

    if  request.session['stat'] == 'assistant' :

        return render(request, 'ajouter.html') #formulair d4ajout de l'assistante
    
    else: return render(request, 'docteur.html') #formulair d4ajout de medcin sinon

def ajout(request):

        nom = request.POST['nom']

        prenom = request.POST['prenom']

        cin = request.POST['cin']

        naissance = request.POST['naissance']

        tel = request.POST['tel']
    
        adresse = request.POST['adresse']
    
        photo = request.POST['photo']
    
        if nom != '' and prenom != '' and cin != '' and naissance != '' and tel != '' and adresse != '' and photo != '':

            insertion_assistante(nom,prenom,cin,naissance,tel,adresse,photo)

            request.session['msg'] = "AJoutavec Succé"

            return render(request, 'ajouter.html', {'a':  "Ajouté avec succés ."})
        
        else: return render(request, 'ajouter.html', {'b':  "Vuilliez remplaire toutes les champs...! "})
"""
    if request.session['stat'] == 'doctor' :

        date_Consultation = request.POST['date_Consultation']
            
        Type_maladie = request.POST['Type_maladie']
     
        Traitement = request.POST['Traitement']
            
        Diagnostic = request.POST['Diagnostic']
        
        patient_consulte = request.POST['patient_consulte']

        if date_Consultation  != '' and Type_maladie != '' and Traitement != '' and  Diagnostic != '' and patient_consulte != '' :
            
            insertion_medcin(date_Consultation,Type_maladie,Traitement,Diagnostic,patient_consulte)

    request.session['msg'] = "AJoutavec Succé"
    

    return render(request, 'ajouter.html')
"""