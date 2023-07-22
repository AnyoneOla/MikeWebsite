from django.http.response import JsonResponse
from django.shortcuts import render

def write_column(name,song):
    f = open('song_list.txt','a')
    f.write(song)
    f.close()
    f = open('name_list.txt','a')
    f.write(name)
    f.close()

def index(request):
    f = open('songs.txt','r')
    song_data = f.readlines()
    f.close()
    temp = []
    contex = {}
    for i in range(len(song_data)):
        temp.append({'song':song_data[i][0:-1]})
    contex['data'] = temp
    return render(request, 'it_works/user_request_form.html',contex)


def requested_songs(request):
    f = open('song_list.txt','r')
    song_data = f.readlines()
    f.close()
    f = open('name_list.txt','r')
    name_data = f.readlines()
    f.close()
    temp = []
    contex = {}
    for i in range(len(song_data)):
        temp.append({'name':name_data[i][0:-1],
                    'song':song_data[i][0:-1]})
    contex['data'] = temp
    print(contex)
    return render(request, 'it_works/user_request_list.html',contex)

def songRequest(request):
    if request.method=="POST":
        name = request.POST['name']
        song = request.POST['song']
        print(song)
        write_column(name+'\n',song+'\n')
    return render(request, 'it_works/user_request_thanks.html')

def addSongsPage(request):
    return render(request,'it_works/user_request_addSong.html')

def addSongs(request):
    if request.method=="POST":
        song = request.POST['song']
        f = open('songs.txt','a')
        f.write(song+'\n')
        f.close()
    return render(request,'it_works/song_added_success.html')

def clearListPage(request):
    return render(request,'it_works/user_request_confirm_delete.html')

def clearList(request):
    f = open('song_list.txt','w')
    f.close()
    f = open('name_list.txt','w')
    f.close()
    return render(request, 'it_works/user_request_list.html')

def searchSong(request):
    song = request.GET.get('song')
    f = open('songs.txt','r')
    song_data = f.readlines()
    f.close()
    op = []
    for i in song_data:
        if song in i:
            op.append(i)
    return JsonResponse({'status':200, 'data':op})
    
