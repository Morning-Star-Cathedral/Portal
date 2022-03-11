from django.shortcuts import get_object_or_404, render
from ChurchDashboard.models import AttendanceSummaries,Attendances,Members,Groups,Chapels, DBUser
from django.db.models import Count
from django.db.models import Q
from rest_framework import generics
from .serializers import DbUserSerializer,ChapelDbuserSerializer



# Create your views here.
#list members oredered by chapel
def index_page(request):
    memcounts = Members.objects.all().count()
    groupcount = Groups.objects.all().count()
    usercount = DBUser.objects.all().count()
    chapscount = Chapels.objects.all().count()
    mil = Members.objects.all().order_by('-id')[:10]

    context = {
        'memcounts':memcounts,
        'groupcount':groupcount,
        'usercount':usercount,
        'chapscount':chapscount,
        'mil':mil
    }
    return render(request,'index.html',context)



def list_view_member(request):
    memlist = Members.objects.all().order_by('chapel')
    context = {
        'memlist': memlist
    }
    return render(request,'member/list.html',context)

#list attendance ordered by created at
#Ruben should look at the data being passed to service date ie am receiving a char instead of a date field
def  list_view_attendance(request):
    read = Attendances.objects.all().order_by('-created_at')
    context = {
        'read': read

    }
    return render(request, 'attendance/list.html', context)

#attendance summary list ordered by created at asecending
def attendance_summmaries_list(request):
    att_summary = AttendanceSummaries.objects.all().order_by('-created_at')
    context = {
        'att_summary':att_summary
    }
    return render(request, 'attendance/attendance_summary.html', context)

#group list
def groups_list(request):
    gro = Groups.objects.all()
    context  = {
        'gro' :gro
    }
    return render(request,'groups/list.html', context)


#chapels list
def chapel_list(request):
    chaps = Chapels.objects.all()
    context = {
        'chaps' : chaps
    }
    return render(request,'chapels/list.html', context)


# DB USer list
def db_user_list(request):
    db_user = DBUser.objects.all().order_by('created_at')
    context = {
        'db_user': db_user
    }
    return  render (request,'DbUser/Dbuser.html', context)

# Details View Members

def members_details(request, id):
    mem_det = get_object_or_404(Members,id = id)
    context = {
        'mem_det':mem_det
    }
    return render(request,'member/details.html',context)

# Details View Chapels

def chap_details(request, id):
    chadetails = get_object_or_404(Chapels,id=id)
    db_users = DBUser.objects.filter(chapel__id =id)
    context = {
        'chadetails':chadetails,
        'db_users':db_users
    }
    return render (request,'chapels/details3.html', context)

# Details View group
def groups_details(request, pk):
    grodetails = get_object_or_404(Groups,pk =pk)
    db_mem = Members.objects.filter(groups__pk =pk)
    context ={
        'grodetails':grodetails,
        'db_mem':db_mem
    }
    return render(request, 'groups/details3.html', context)

def  db_details(request, id):
    db_details = get_object_or_404(DBUser,id =id)
    mens = Members.objects.filter(dbuser__id=id)
    context = {
        'db_details':db_details,
        'mens':mens
    }
    return render(request, 'DbUser/details.html', context)


# API VIEWS

#uSER lIST API
class DbUserListAPi(generics.ListAPIView):
    queryset = DBUser.objects.all()
    serializer_class = DbUserSerializer


#CHAPEL LIST apI
class ChapelListAPi(generics.ListAPIView):
    queryset = Chapels.objects.all()
    serializer_class = ChapelDbuserSerializer

