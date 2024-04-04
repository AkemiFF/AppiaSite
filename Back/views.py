from django.shortcuts import render
from .models import Contact

def formulaire_contact(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        societe = request.POST['societe']
        adresse = request.POST['adresse']
        telFixe = request.POST['telFixe']
        telMobile = request.POST['telMobile']
        besoin = request.POST['besoin']
        
        contact = Contact.objects.create(
            nom=nom,
            societe=societe,
            adresse=adresse,
            telFixe=telFixe,
            telMobile=telMobile,
            besoin=besoin
        )
        contact.save()

        return render(request, 'index.html', {'message': 'Formulaire envoyé avec succès !'})

    return render(request, 'index.html')
