from django.shortcuts import render
from cricketapp.models import Team

# Create your views here.
def teamdata(request):
    team_list=Team.objects.all()
    my_dict={'team_list':team_list}
    return render(request,'cricketapp/index.html',context=my_dict)
