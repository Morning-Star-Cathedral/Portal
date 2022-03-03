from django.shortcuts import render
from ChurchDashboard.models import AttendanceSummaries,Attendances,Members,Groups,Chapels

# Create your views here.
#list members
def list_view_member(request):
    memlist = Members.objects.all()
    context = {
        'memlist': memlist
    }
    return render(request,'member/list.html',context)


def  list_view_attendance(request):
    read = Attendances.objects.all().order_by('-created_at')
    context = {
        'read': read

    }
    return render(request, 'attendance/list.html', context)