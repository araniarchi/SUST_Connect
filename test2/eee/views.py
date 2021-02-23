from django.shortcuts import render
from .models import CustomUser, Paper, Job
from django.db.models import Q
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.conf import settings

# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout

IMAGE_FILES_TYPES = ['png', 'jpg', 'jpeg']

from django.contrib.auth import get_user


def index(request):
    print("sust")
    return render(request, 'eee/start.html')


def login(request):
    if request.method == 'POST':
        tusername = request.POST.get('username')
        tpassword = request.POST.get('password')

        print(tusername)

        user = authenticate(username=tusername, password=tpassword)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return render(request, 'eee/mainpage.html')
            else:
                return render(request, 'eee/login.html')
        else:
            return render(request, 'eee/login.html')
    else:
        return render(request, 'eee/login.html')


def logout(request):
    auth_logout(request)
    return render(request, 'eee/start.html')


def registration(request):
    print("registration e dhukse")

    if request.method == 'POST':
        # return render(request , 'eee/mainpage.html')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        username = request.POST.get('username')

        password = request.POST.get('password')
        print('vitore dukse')
        # print(f_name)
        email = request.POST.get('email')
        date_of_birth = request.POST.get('birthDate')
        blood_group = request.POST.get('bloodgroup')
        gender = request.POST.get('Gender')
        home_town = request.POST.get('hometown')
        Current_City = request.POST.get('currentcity')
        # Picture = request.POST.get('Photos')
        about_me = request.POST.get('about_me')
        skill_name = request.POST.get('skill_name')
        department = request.POST.get('department')
        sust_reg_no = request.POST.get('Regno')
        session = request.POST.get('Session')
        cur_semester = request.POST.get('Semester')
        contact_no = request.POST.get('contact')
        Linkedin_link = request.POST.get('LinkedIn')
        Github_Link = request.POST.get('Github')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        all_user = CustomUser(first_name=first_name, last_name=last_name, email=email,
                              date_of_birth=date_of_birth, blood_group=blood_group,
                              gender=gender, home_town=home_town, Current_City=Current_City,
                              about_me=about_me, skill_name=skill_name, department=department,
                              sust_reg_no=sust_reg_no, session=session, cur_semester=cur_semester,
                              contact_no=contact_no, Linkedin_link=Linkedin_link,
                              Github_Link=Github_Link, height=height, weight=weight, username=username)

        all_user.set_password(password)
        # return render(request,'eee/mainpage.html')
        # all_user.Picture='b.jpg'
        # all_user.Picture = request.FILES['Photos']
        # file_type=all_user.Picture.url.split('.')[-1]
        # file_type = file_type.lower()
        # if file_type not in IMAGE_FILES_TYPES:
        #    return render(request,'eee/registration.html')

        all_user.is_active = True

        all_user.save()

        return render(request, 'eee/login.html')

    else:
        return render(request, 'eee/registration.html')


def mainpage(request):
    if request.user.is_authenticated:
        return render(request, 'eee/mainpage.html')
    else:
        return render(request, 'eee/login.html')


def listing_filter(request):
    return render(request, 'eee/listing_filter_none.html')


def stu_search(request):
    if request.user.is_authenticated:
        paperall = Paper.objects.all()
        userall = CustomUser.objects.all()
        query = request.GET.get("q")
        print(query)
        # return render(request,'eee/mainpage.html')
        if query:
            amader_result = userall.filter(
                Q(Current_City__icontains=query) |
                Q(skill_name__icontains=query) |
                Q(MSc_Institute_name__icontains=query) |
                Q(MSc_Institute_Country__icontains=query) |
                Q(Phd_Institute_name__icontains=query) |
                Q(Phd_Institute_Country__icontains=query)

            ).distinct()
            amader_result2 = paperall.filter(
                Q(Research_area__icontains=query)
            ).distinct()
            return render(request, 'eee/listing-filter.html', {'allstu': amader_result, 'allstu2': amader_result2})
        else:
            return render(request, 'eee/listing_filter_none.html')
    else:
        return render(request, 'eee/login.html')


def contact(request):
    return render(request, 'eee/contact.html')


def profile(request):
    if request.user.is_authenticated:
        user_info = request.user
        return render(request, 'eee/profile.html', {'user_in': user_info})
    else:
        return render(request, 'eee/login.html')


def job(request):
    user_info = request.user
    c = Job.objects.filter(user_id_id=request.user.id)
    return render(request, 'eee/job.html', {'user_in': user_info, 'alljob': c})


def job_general(request, id):
    user_info = CustomUser.objects.get(id=id)
    c = Job.objects.filter(user_id_id=id)

    return render(request, 'eee/job_general.html', {'user_in': user_info, 'alljob': c})


def jobupdate(request):
    if request.method == 'POST':
        Job_Institute_or_Company = request.POST.get('InstitutionName')
        Address = request.POST.get('address')
        Job_Position = request.POST.get('jobPosition')
        Job_start_date = request.POST.get('Job_Star_Date')
        Job_end_date = request.POST.get('jobEnd_Date')

        jobup = Job(Job_Institute_or_Company=Job_Institute_or_Company,user_id_id=request.user.id,
                    Address=Address,Job_Position=Job_Position,Job_start_date=Job_start_date,Job_end_date=Job_end_date)

        jobup.save()
    else:
        return render(request, 'eee/jobupdate.html')

    # return render(request, 'eee/jobupdate.html')


def phd(request, id):
    if request.user.is_authenticated:
        user_info = CustomUser.objects.get(id=id)
        return render(request, 'eee/profile_general.html', {'user_in': user_info})
    else:
        return render(request, 'eee/login.html')


def paper(request):
    return render(request, 'eee/paper.html')


def education(request):
    c = Paper.objects.filter(user_id_id=request.user.id)
    return render(request, 'eee/education.html', {'user_in': request.user, 'user_r': c})


def education_general(request, id):
    c = Paper.objects.filter(user_id_id=id)
    user_info = CustomUser.objects.get(id=id)
    return render(request, 'eee/education_general.html', {'user_in': user_info, 'user_r': c})


def msc(request):
    if request.method == 'POST':
        user_info = request.user
        user_info.MSc_Institute_name = request.POST.get('mscInstitutionName')
        user_info.MSc_Institute_Country = request.POST.get('mscInstitutionCountry')
        user_info.MSc_start_date = request.POST.get('mscStart_Date')
        user_info.MSc_end_date = request.POST.get('mscEnd_Date')
        user_info.save()
        return render(request, 'eee/mainpage.html')

    else:
        return render(request, 'eee/msc.html')


def phd1(request):
    if request.method == 'POST':
        user_info = request.user
        user_info.Phd_Institute_name = request.POST.get('phdInstitutionName')
        user_info.Phd_Institute_Country = request.POST.get('phdInstitutionCountry')
        user_info.Phd_start_date = request.POST.get('phdStar_Date')
        user_info.Phd_end_date = request.POST.get('phdEnd_Date')
        user_info.save()
        return render(request, 'eee/mainpage.html')

    else:
        return render(request, 'eee/phd.html')


def paper(request):
    if request.method == 'POST':
        Research_area = request.POST.get('research')
        Published_Paper = request.POST.get('publishedPaper')
        Published_Journal = request.POST.get('publishedJournal')
        papup = Paper(Research_area=Research_area, user_id_id=request.user.id, Published_Paper=Published_Paper,
                      Published_Journal=Published_Journal)
        papup.save()
        return render(request, 'eee/mainpage.html')

    else:
        return render(request, 'eee/paper.html')
