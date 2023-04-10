from django.shortcuts import render
from django.http import HttpResponse

from authentification.views import login
from .classe_user import recuperation

# Create your views here.
def recherche(request):
      import sqlite3
      recherche=request.POST['search']
      conn = sqlite3.connect('db.sqlite3')
      cur=conn.cursor()
      search=recherche.split()
      req="SELECT * FROM patient,consultation where nom='{}' AND prenom='{}' AND id_patient=patient_consulte ".format(search[0],search[1])
      resultat=cur.execute(req)
      result = cur.fetchone()
      nom=result[0]
      return render(request, 'resultat_recherche.html', {'nom': result[1], 'prenom': result[2] , 'cin': result[3], 'naissance':result[4], 'tel': result[5] })


# Create your views here.
def current_datetime(request):
  if request.session['stat'] == 'assistant':

        nom = request.POST['nom']

        prenom = request.POST['prenom']

        cin = request.POST['cin']

        naissance = request.POST['naissance']

        tel = request.POST['tel']
    
        adresse = request.POST['adresse']
    
        photo = request.POST['photo']
    
        if nom != '' and prenom != '' and cin != '' and naissance != '' and tel != '' and adresse != '' and photo != '':
          import sqlite3
          conn = sqlite3.connect('db.sqlite3')

          cur=conn.cursor()

          req="select * from patient"

          result=cur.execute(req)
        
          resultt=result.fetchall()

          for row in resultt :
           
            html = """
                <!DOCTYPE html>
      <html lang="en">
      <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>rechercher la consultation</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
      rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" 
      integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>

      <link rel="stylesheet" href="{% static 'static/style.css'%}">
      <style>
         .ddList{ width:100%; text-align: center; font-weight: bold; border: 3px solid black ;color:black;
            border-radius: 150px; height: 50px;} 
         select .lt { text-align: center; font-weight: bold; }

         th, td,tr,tbody{background-color: white;border: 2px solid rgb(3, 17, 19);padding: 20px;}
         .mytab{
            width: 800px;
            max-height: 500px;
            overflow:auto;
            height: 250px;
            margin-left: 30%;}

         .btn:hover{color:black;background-color:white;border: 3px solid black ;}
          body {color:black;background-color:white;background-image:url(temp.jpg);}
         .mx-auto{ width:20%;} 
         .btn{background-color: black; font-weight: bold; border-color:white; }
   
      </style>
      </head>
      <body>
    
      <center><img src="CodeBlocks.lnk"> <br><br></center>
      <div class="mytab">
      <table class="table table-striped">
        
            <thead>
              <tr>
                <center>
                    <h1><b><i>Information Du Client:</i></b></h1><br>
                </center>  
              </tr>
            </thead>
            <tbody>
                <tr><th scope="col">Nom</th><td>""",row[1],"""</td></tr>
                <tr><th scope="col">Prénom</th><td>""",row[2],""" </td></tr>
                <tr><th scope="col">Date De Naissance</th><td>""",row[4],"""</td></tr>
           
            </tbody>
        </table></div><br><br>
          
      <select name="state" class="ddList">
            <option class='lt' value="">Consultation</option>
            <option class="lt" value="--">none</option>
            <option class="lt" value="AL">Alabama</option>
            <option class="lt" value="AK">Alaska</option>
            <option class="lt" value="AZ">Arizona</option>
            <option class="lt" value="AR">Arkansas</option>
            <option class="lt" value="CA">California</option>
            <option class="lt" value="CO">Colorado</option></select>

      <div class="d-grid gap-2 col-6 mx-auto "><br>
            <button class="btn btn-primary" type="button">Afficher</button>
      </div><br><br>

      <div class="mytab">
      <table class="table  table-striped">
        <thead></thead>
        <tbody>
                <tr><th scope="col">Date De Consultation</th><td>cc</td></tr>
                <tr><th scope="col">Type Maladie</th><td>cv</td></tr>
                <tr><th scope="col">Traitement</th><td>cv</td></tr>
                <tr><th scope="col">Diagnostique</th><td>cv</td></tr>
                <tr><th scope="col">Description</th><td>cv</td></tr>
        </tbody>
      </table>
      </div>
      <div class="d-grid gap-2 col-6 mx-auto">
        <button class="btn btn-primary" type="button">Afficher</button>
      </div>
      </body>
    </html>

    """
            
        return HttpResponse(html)

  elif request.session['stat'] == 'doctor':

        date_Consultation = request.POST['date_Consultation']
            
        Type_maladie = request.POST['Type_maladie']
     
        Traitement = request.POST['Traitement']
            
        Diagnostic = request.POST['Diagnostic']
        
        patient_consulte = request.POST['patient_consulte']

        if date_Consultation  != '' and Type_maladie != '' and Traitement != '' and  Diagnostic != '' and patient_consulte != '' :
          
          import sqlite3

          conn = sqlite3.connect('db.sqlite3')

          cur=conn.cursor()

          req="select * from consultation"

          result=cur.execute(req)

          resultt=result.fetchall()

          for row in resultt :
           
                html = """
                <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>rechercher la consultation</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
      rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" 
      integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>

    <link rel="stylesheet" href="{% static 'static/style.css'%}">
    <style>
         .ddList{ width:100%; text-align: center; font-weight: bold; border: 3px solid black ;color:black;
            border-radius: 150px; height: 50px;} 
         select .lt { text-align: center; font-weight: bold; }

         th, td,tr,tbody{background-color: white;border: 2px solid rgb(3, 17, 19);padding: 20px;}
         .mytab{
            width: 800px;
            max-height: 500px;
            overflow:auto;
            height: 250px;
            margin-left: 30%;}

         .btn:hover{color:black;background-color:white;border: 3px solid black ;}
          body {color:black;background-color:white;background-image:url(temp.jpg);}
         .mx-auto{ width:20%;} 
         .btn{background-color: black; font-weight: bold; border-color:white; }
   
    </style>
</head>
<body>
    
    <center><img src="CodeBlocks.lnk"> <br><br></center>
   <div class="mytab">
    <table class="table table-striped">
        
            <thead>
              <tr>
                <center>
                    <h1><b><i>Information Du Client:</i></b></h1><br>
                </center>  
              </tr>
            </thead>
            <tbody>
                <tr><th scope="col">Nom</th><td>""",row[1],"""</td></tr>
                <tr><th scope="col">Prénom</th><td>""",row[2],""" </td></tr>
                <tr><th scope="col">Date De Naissance</th><td>""",row[4],"""</td></tr>
           
            </tbody>
    </table></div><br><br>
          
    <select name="state" class="ddList">
            <option class='lt' value="">Consultation</option>
            <option class="lt" value="--">none</option>
            <option class="lt" value="AL">Alabama</option>
            <option class="lt" value="AK">Alaska</option>
            <option class="lt" value="AZ">Arizona</option>
            <option class="lt" value="AR">Arkansas</option>
            <option class="lt" value="CA">California</option>
            <option class="lt" value="CO">Colorado</option></select>

    <div class="d-grid gap-2 col-6 mx-auto "><br>
            <button class="btn btn-primary" type="button">Afficher</button>
    </div><br><br>

    <div class="mytab">
    <table class="table  table-striped">
        <thead></thead>
        <tbody>
                <tr><th scope="col">Date De Consultation</th><td>cc</td></tr>
                <tr><th scope="col">Type Maladie</th><td>cv</td></tr>
                <tr><th scope="col">Traitement</th><td>cv</td></tr>
                <tr><th scope="col">Diagnostique</th><td>cv</td></tr>
                <tr><th scope="col">Description</th><td>cv</td></tr>
        </tbody>
    </table>
    </div>
    <div class="d-grid gap-2 col-6 mx-auto">
        <button class="btn btn-primary" type="button">Afficher</button>
    </div>
</body>
</html>

               """
            
                return HttpResponse(html)
            
        else: return render(request,'login.html')