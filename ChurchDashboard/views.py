from django.shortcuts import get_object_or_404, render, redirect
from ChurchDashboard.models import AttendanceSummaries, Attendances, Members, Groups, Chapels, DBUser
from django.core.cache import cache


# Create your views here.
# list members oredered by chapel
def index_page(request):
    memcounts = Members.objects.all().count()
    groupcount = Groups.objects.all().count()
    usercount = DBUser.objects.all().count()
    chapscount = Chapels.objects.all().count()
    mil = Members.objects.all().order_by('-id')[:5]
    db_usered = DBUser.objects.all().order_by('id')[:20]

    context = {
        'memcounts': memcounts,
        'groupcount': groupcount,
        'usercount': usercount,
        'chapscount': chapscount,
        'mil': mil,
        'db_usered': db_usered
    }
    return render(request, 'index.html', context)


# chapel=chapel_page, availabe=True

def list_view_member(request):
    memlist = Members.objects.all()
    groud = Groups.objects.filter()
    context = {
        'memlist': memlist
    }
    return render(request, 'member/list.html', context)


# list attendance ordered by created at
# Ruben should look at the data being passed to service date ie am receiving a char instead of a date field
def list_view_attendance(request):
    read = Attendances.objects.all().order_by('-created_at')
    context = {
        'read': read

    }
    return render(request, 'attendance/list.html', context)


# attendance summary list ordered by created at asecending
def attendance_summmaries_list(request):
    att_summary = AttendanceSummaries.objects.all().order_by('-created_at')
    context = {
        'att_summary': att_summary
    }
    return render(request, 'attendance/attendance_summary.html', context)


# group list
def groups_list(request):
    gro = Groups.objects.all()
    context = {
        'gro': gro
    }
    return render(request, 'groups/list.html', context)


# chapels list
def chapel_list(request):
    chaps = Chapels.objects.all()
    context = {
        'chaps': chaps
    }
    return render(request, 'chapels/list.html', context)


# DB USer list
def db_user_list(request):
    db_user = DBUser.objects.all().order_by('created_at')
    context = {
        'db_user': db_user
    }
    return render(request, 'DbUser/Dbuser.html', context)


# Details View Members

def members_details(request, pk):
    if cache.get(pk):
        print('cache working')
        mem_det = cache.get(pk)
    else:
        try:
            mem_det = Members.objects.get(pk=pk)
            cache.set(pk, mem_det)
            print('DB DATA')
        except Members.DoesNotExist:
            return redirect('ChurchDashboard:home_page')
    context = {
        'mem_det': mem_det
    }
    return render(request, 'member/details.html', context)


# Details View Chapels
def chap_details(request, id):
    db_users = DBUser.objects.filter(chapel__id=id)
    dbuser_count = DBUser.objects.filter(chapel__id=id).count()
    ch_mem_count = Members.objects.filter(chapel__id=id).count()
    if cache.get(id):
        print('we did it')
        chadetails = cache.get(id)
    else:
        try:
            chadetails = Chapels.objects.get(id=id)
            cache.set(id, chadetails)

        except Chapels.DoesNotExist:
            return redirect('ChurchDashboard:home_page')
    context = {
        'chadetails': chadetails,
        'db_users': db_users,
        'dbuser_count': dbuser_count,
        'ch_mem_count': ch_mem_count
    }
    return render(request, 'chapels/details3.html', context)


# Details View group
def groups_details(request, pk):
    userlist = DBUser.objects.filter(group__id=pk)
    gro_membs_count = Members.objects.filter(group__id=pk).count()
    gro_membs = Members.objects.filter(group__id=pk)
    if cache.get(pk):
        print('cache')
        grodetails = cache.get(pk)
    else:
        try:
            grodetails = Groups.objects.get(pk=pk)
            cache.set(pk, grodetails)
        except Groups.DoesNotExist:
            return redirect('ChurchDashboard:home_page')
    context = {
        'grodetails': grodetails,
        'userlist': userlist,
        'gro_membs_count': gro_membs_count,
        'gro_membs': gro_membs

    }
    return render(request, 'groups/details3.html', context)


def db_detail(request, id):
    # mens = Members.objects.filter(dbuser__id=id)
    if cache.get(id):
        db_details = cache.get(id)
    else:
        try:
            db_details = DBUser.objects.get(id=id)
            cache.set(id, db_details)
        except DBUser.DoesNotExist:
            return redirect('ChurchDashboard:home_page')
    context = {
        'db_details': db_details
        # 'mens': mens
    }
    return render(request, 'DbUser/details.html', context)
