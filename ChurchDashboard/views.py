from django.shortcuts import render
from ChurchDashboard.models import AttendanceSummaries,Attendances,Members,Groups,Chapels, DBUser

# Create your views here.
#list members oredered by chapel
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

# Details View

