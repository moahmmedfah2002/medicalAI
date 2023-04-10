from django.shortcuts import render
from django.http import HttpResponse


def recherche(request):
      import sqlite3
      recherche=request.POST['search']
      conn = sqlite3.connect('db.sqlite3')
      cur=conn.cursor()
      search=recherche.split()
      req="SELECT * FROM patient,consultation where nom='{}' AND prenom='{}' AND id_patient=patient_consulte ".format(search[0],search[1])
      resultat=cur.execute(req)
      result = cur.fetchone()
      return render(request, 'affichage.html', {'nom': result[1], 'prenom': result[2] , 'tel': result[3], 'naissance':result[4], 'tel': result[5] ,'adresse': result[6] ,'date_consultation': result[8], 'maladie': result[9], 'traitement': result[10], 'diagnostic': result[11]  })

def sec(request):
     return render(request,'sec.html')

