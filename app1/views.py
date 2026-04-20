from django.shortcuts import render
from .models import Doctor, Patient

def home(request):
    return render(request, 'home.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == "admin" and password == "1234":
            return render(request, 'dashboard.html')
        else:
            return render(request, 'adminlogin.html', {'error': 'Invalid Credentials'})

    return render(request, 'adminlogin.html')

def add_doctor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        specialization = request.POST.get('specialization')
        phone = request.POST.get('phone')

        if name and specialization and phone:
            Doctor.objects.create(
                name=name,
                specialization=specialization,
                phone=phone
            )
            return render(request, 'add_doctor.html', {'success': 'Doctor Added Successfully'})
        else:
            return render(request, 'add_doctor.html', {'error': 'Please fill all fields'})

    return render(request, 'add_doctor.html')

def view_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'view_doctors.html', {'doctors': doctors})

def delete_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return view_doctors(request)

def add_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        disease = request.POST.get('disease')

        if name and age and disease:
            Patient.objects.create(
                name=name,
                age=age,
                disease=disease
            )
            return render(request, 'add_patient.html', {'success': 'Patient Added Successfully'})
        else:
            return render(request, 'add_patient.html', {'error': 'Please fill all fields'})

    return render(request, 'add_patient.html')

def view_patients(request):
    patients = Patient.objects.all()
    return render(request, 'view_patients.html', {'patients': patients})

def logout(request):
    return render(request, 'adminlogin.html')