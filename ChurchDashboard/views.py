from django.shortcuts import get_object_or_404, render, redirect
from ChurchDashboard.models import AttendanceSummaries, Attendances, Members, Groups, Chapels, DBUser
from django.core.cache import cache
from .forms import CreateGroupForm, CreateChapelForm, CreateMemberForm
import json
from django.contrib.auth.decorators import login_required


# Create your views here.
# list members oredered by chapel
@login_required(login_url='accounts:login_user')
def index_page(request):
    memcounts = Members.objects.all().count()
    groupcount = Groups.objects.all().count()
    usercount = DBUser.objects.all().count()
    chapscount = Chapels.objects.all().count()
    db_usered = DBUser.objects.all().order_by('-id')[:20].select_related('chapel', 'group')

    context = {
        'memcounts': memcounts,
        'groupcount': groupcount,
        'usercount': usercount,
        'chapscount': chapscount,
        'db_usered': db_usered,

    }
    return render(request, 'index.html', context)

@login_required(login_url='accounts:login_user')
def memberindex(request):
    mil = Members.objects.all().order_by('-id')[:5].select_related('group', 'chapel')
    # nil = DBUser.objects.filter(group__id = Members.group)

    context = {
        'mil': mil,
        # 'nil': nil
    }
    return render(request, 'membersindex.html', context)


# chapel=chapel_page, availabe=True
@login_required(login_url='accounts:login_user')
def list_view_member(request):
    memlist = Members.objects.all().select_related('chapel', 'group')
    # groud = DBUser.objects.filter(group__id=Members.group)

    context = {
        'memlist': memlist
        # 'groud': groud,
    }
    return render(request, 'member/list.html', context)


# def db_userindex(request):
#     dbusered = DBUser.objects.all().order_by('-id')[:20]
#
#     context = {
#         'dbusered': dbusered
#     }
#     return render(request, 'Dbuserlistindex.html', context)


# list attendance ordered by created at
# Ruben should look at the data being passed to service date ie am receiving a char instead of a date field
@login_required(login_url='accounts:login_user')
def list_view_attendance(request):
    read = Attendances.objects.all().order_by('service_date').select_related('member')
    context = {
        'read': read

    }
    return render(request, 'attendance/list.html', context)


# attendance summary list ordered by created at asecending
@login_required(login_url='accounts:login_user')
def attendance_summmaries_list(request):
    att_summary = AttendanceSummaries.objects.all().order_by('attendance_date').select_related('group')
    context = {
        'att_summary': att_summary
    }
    return render(request, 'attendance/attendance_summary.html', context)


# group list
@login_required(login_url='accounts:login_user')
def groups_list(request):
    gro = Groups.objects.all()
    # userlist = DBUser.objects.filter(group__id=gro.id)
    context = {
        'gro': gro
        # 'userlist': userlist
    }
    return render(request, 'groups/list.html', context)


# chapels list
@login_required(login_url='accounts:login_user')
def chapel_list(request):
    chaps = Chapels.objects.all()
    context = {
        'chaps': chaps
    }
    return render(request, 'chapels/list.html', context)


# DB USer list
@login_required(login_url='accounts:login_user')
def db_user_list(request):
    db_user = DBUser.objects.all().order_by('created_at').select_related('group', 'chapel')
    context = {
        'db_user': db_user
    }
    return render(request, 'DbUser/Dbuser.html', context)


# Details View Members
@login_required(login_url='accounts:login_user')
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
@login_required(login_url='accounts:login_user')
def chap_details(request, id):
    db_users = DBUser.objects.filter(chapel__id=id)
    dbuser_count = DBUser.objects.filter(chapel__id=id).count()
    ch_mem_count = Members.objects.filter(chapel__id=id).count()
    cha_mem = Members.objects.filter(chapel__id=id).order_by(('-id')[:5])
    membered = Members.objects.filter(group__id=id)
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
        'ch_mem_count': ch_mem_count,
        'cha_mem': cha_mem,
        'membered': membered

    }
    return render(request, 'chapels/details3.html', context)


# Details View group
@login_required(login_url='accounts:login_user')
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


#
# def db_detail(request, id):
#     db_details = DBUser.objects.filter(group__id=id)
#     gro_membs_count = Members.objects.filter(group__id=DBUser.group).count()
#     # gro_membs = Members.objects.filter(group__id=id) & DBUser.objects.filter(group__id =Members.)
#     if cache.get(id):
#         db_details = cache.get(id)
#     else:
#         try:
#             db_details = DBUser.objects.get(id=id)
#             cache.set(id, db_details)
#         except DBUser.DoesNotExist:
#             return redirect('ChurchDashboard:home_page')
#     context = {
#         'db_details': db_details,
#         'gro_membs_count': gro_membs_count,
#          # 'gro_membs': gro_membs
#         # 'mens': mens
#     }
#     return render(request, 'DbUser/details.html', context)
# create views
@login_required(login_url='accounts:login_user')
def create_view_group(request):
    context = {}
    groupcreate = CreateGroupForm(request.POST or None)
    if groupcreate.is_valid():
        groupcreate.save()
        return redirect('ChurchDashboard:list_group_url')

    context['groupcreate'] = groupcreate
    return render(request, "groups/create.html", context)


# member creation
@login_required(login_url='accounts:login_user')
def create_members(request):
    context = {}
    mem_create = CreateMemberForm(request.POST or None)
    if mem_create.is_valid():
        mem_create.save()
        return redirect('ChurchDashboard:list_member_url')

    context['mem_create'] = mem_create
    return render(request, "member/create.html", context)


# def group_delete(request, pk):
#     delete_group = get_object_or_404(Groups, pk=pk)
#     if request.method == "POST":
#         delete_group.delete()
#         return redirect('ChurchDashboard:list_group_url')
#     return render(request, 'groups/delete.html', context={})

@login_required(login_url='accounts:login_user')
def create_chapel(request):
    context = {

    }
    chapel_create = CreateChapelForm(request.POST or None)
    if chapel_create.is_valid():
        chapel_create.save()
        return redirect('ChurchDashboard:list_chapel_url')
    context['chapel_create'] = chapel_create
    return render(request, 'chapels/add.html', context)


@login_required(login_url='accounts:login_user')
def group_delete(request, pk):
    delete_group = get_object_or_404(Groups, pk=pk)
    if request.method == "POST":
        delete_group.delete()
        return redirect('ChurchDashboard:list_group_url')
    context = {}
    return render(request, 'groups/delete.html', context)


@login_required(login_url='accounts:login_user')
def dbuser_delete(request, id):
    delete_group = get_object_or_404(Groups, id=id)
    if request.method == "POST":
        delete_dbuser.delete()
        return redirect('ChurchDashboard:list_grouplead_url')
    context = {}
    return render(request, 'DbUser/delete.html', context)
