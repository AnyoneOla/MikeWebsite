from django.http.response import JsonResponse
from django.shortcuts import render
import pyrebase

config = {
    "apiKey": "AIzaSyDGFUpZTmtZdjzuoSsLDlspfMt2TM-MDPc",
    "authDomain": "abcd-1564836707355.firebaseapp.com",
    "databaseURL": "https://abcd-1564836707355-default-rtdb.firebaseio.com/",
    "projectId": "abcd-1564836707355",
    "storageBucket": "abcd-1564836707355.appspot.com",
    "messagingSenderId": "18942703899",
    "appId": "1:18942703899:web:cfafec3b8c4d63d1117bbe",    
}


firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()



def write_column(name,song):
    data = {'name':name,'song':song}
    database.child("Data").push(data)

def index(request):
    song_data = []
    x = database.child('Data').get().val()
    for i in x:
        song_data.append(x[i]['song'])
    contex = {}
    contex['data'] = song_data
    return render(request, 'it_works/user_request_form.html',contex)


def requested_songs(request):
    name_data = []
    song_data = []
    x = database.child('Data').get().val()
    for i in x:
        name_data.append(x[i]['name'])
        song_data.append(x[i]['song'])
    temp = []
    contex = {}
    for i in range(len(song_data)):
        temp.append({'name':name_data[i],
                    'song':song_data[i]})
    contex['data'] = temp
    print(contex)
    return render(request, 'it_works/user_request_list.html',contex)

def songRequest(request):
    if request.method=="POST":
        name = request.POST['name']
        song = request.POST['song']
        print(song)
        write_column(name,song)
    return render(request, 'it_works/user_request_thanks.html')

def addSongsPage(request):
    return render(request,'it_works/user_request_addSong.html')

def addSongs(request):
    if request.method=="POST":
        song = request.POST['song']
        data = {'Song':song}
        database.child("Songs").push(data)
    return render(request,'it_works/song_added_success.html')

def clearListPage(request):
    return render(request,'it_works/user_request_confirm_delete.html')

def clearList(request):
    x = database.child('Data').get().val()
    l = len(x.keys())
    cnt = 0
    for i in x.keys():
        if cnt==l-1:
            break
        database.child("Data").child(i).remove()
        cnt+=1
    return render(request, 'it_works/user_request_list.html')

def searchSong(request):
    song = request.GET.get('song')
    x = database.child('Songs').get().val()
    song_data = []
    for i in x:
        song_data.append(x[i]['song'])
    op = []
    for i in song_data:
        if song in i:
            op.append(i)
    return JsonResponse({'status':200, 'data':op})
