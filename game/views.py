from django.shortcuts import render,redirect

from django.contrib import messages
from django.http import HttpResponse
from .models import user_details,Movie,Song
from .forms import LoginForm

import random
movie_name = " "
song_name = " "
message = ""
result_name =" "
user_name=""
score=0
def home(request):
    global user_name
    user_detail= user_details.objects.all()
    print (user_detail)
    return render(request ,"home.html", {'user_name': user_name,"message":""})

def register(request):
    global user_name
    if request.method=='POST':
        user_name = request.POST['firstname']
        password= request.POST['password']
        confirmPassword= request.POST['confirmPassword']
        print(user_name)
        
        if user_details.objects.filter(name=user_name).exists():
            message="Username already exists."
            return render(request ,"register.html", {"message": message})
        else:
            
            if password == confirmPassword:
                message="User created successfully !"
                #form=LoginForm(request.POST)
                user_details.objects.create(name=user_name,password=password)
                return render(request ,"login.html", {"message": message})
            else:
                message="Password didn't matched !"
                #form=LoginForm(request.POST)
                return render(request ,"register.html", {"message": message})
    return render(request ,"register.html", {"message": ""})


def login(request):
    global user_name,score
    if request.method=='POST':
        if request.POST.get('username'):
            name_in_details = request.POST.get('username')
            password = request.POST.get('password')
            user_name=""
            if user_details.objects.filter(name=name_in_details).exists():
                user_name=name_in_details
                userlist=user_details.objects.values_list('name','password','score')
                for i in range(0,len(userlist)):
                    if user_name==userlist[i][0] and password==userlist[i][1]:
                        score=userlist[i][2]
                        message=name_in_details+" logged in successfully !"
                        user_login_details={"user_name":user_name,"message":message}
                        print(user_name)
                        return render(request ,"home.html", user_login_details)
                flag=1
                if flag==1:
                    message=" Incorrect Password!"
                    user_login_details={"user_name":user_name,"message":message}
                    #print(user_name)
                    return render(request ,"login.html", user_login_details)
                
            else:
                return redirect("register")
        else:
            message=""
            return render(request,"login.html",{"message":message})
    message=""
    return render(request ,"login.html", {"message":message})

def random_name():
    id_m=random.randint(1,1284)
    print(id_m)
    return id_m

def pig_latin(name):
    
    global result_name
    vowels=['a','e','i','o','u']
    result=[]
    result_name=""
    digit=''
    for position in range(0,len(name)) :
        counter=0
        if name[position][counter].isdigit() or name[position]==':':
            result.append(name[position])
            continue
        if name[position][counter].lower() in vowels and name[position][counter].isalpha():
            counter=1
            #if name[position][counter]==':':
                #continue
            counter=1
        else:
            while counter<len(name[position]) and name[position][counter].lower() not in vowels:
                digit=''
                if name[position][counter].isdigit() or name[position][counter]==':' or name[position][counter]=='/':
                    digit=name[position]
                    print(digit)
                    continue
                #print("Breakpoint"+' '+name[position][counter])
                counter +=1
                #print("Breakpoint"+' '+name[position][counter])
        result.append(name[position][counter:]+name[position][:counter]+'ay')
        result_name=' '.join(result)
        result_name=result_name+digit

    return result_name

def translator1(request):
    global user_name
    translate_detail={"user_name" : user_name }
    return render(request,"translator.html",{'translate_detail': translate_detail})

def translator(request):
    global user_name
    user_sentence= request.GET['answer']
    print(user_sentence)
    name=user_sentence.split()
    print(name)
    result_name=''
    flag=0
    '''while(1):
        if digits in name:
            flag=1
        if flag==1:
            id_m = random_name()
            movie_detail=Movie.objects.get(id=id_m)
            movie_name = movie_detail.title
            name=movie_name.split()   
        if flag==0:
            break  '''       

    result_name=pig_latin(name)
    
    translate_detail={"name":result_name,"user_name" : user_name }
    
    
    return render(request,"translator.html", {'translate_detail': translate_detail})


def movie_game(request):
    global movie_name,message,result_name,user_name,score
    digits=[0,1,2,3,4,5,6,7,8,9]
    movie_detail= Movie.objects.all()
    
    id_m = random_name()
    movie_detail=Movie.objects.get(id=id_m)
    
    movie_name = movie_detail.title
    name=movie_name.split()
    print(name)
    result_name=''
    flag=0
    '''for i in range (0,len(name)):
            for j in range (0,len(name[i])):
                if name[i][j]==':' or name[i][j]=='/' or name[i][j].isdigit() or name[i][j]=='!' :
                    flag=1
            if flag==1:
                break'''
    while(1):
        if digits in name:
            flag=1
        if flag==1:
            id_m = random_name()
            movie_detail=Movie.objects.get(id=id_m)
            movie_name = movie_detail.title
            name=movie_name.split()   
        if flag==0:
            break         

    result_name=pig_latin(name)
    
    movie_detail={"name":result_name, "message":message, "user_name":user_name, "score":score}
    
    
    return render(request,"movie.html", {'movie_detail': movie_detail})


def check_answer(request):
    global movie_name,message,user_name,score
    user_answer= request.GET['answer']
    print(user_answer)
    if user_answer == movie_name:
        message="That was correct strike."
        score+=10
        user_details.objects.filter(name=user_name).update(score=score)
        return movie_game(request)
    else:
        message="You need to try again."
        print("Not Correct")
    movie_detail={"user_name":user_name,"name":result_name,"message":message,"score":score}
    print(result_name)
    return render(request,'movie.html',{'movie_detail': movie_detail})


def main_page(request):
    return render(request,"index.html",{})


def song_game(request):

    global message,song_name
    
    song_detail= Song.objects.all()
    #print (movie_detail)
    id_s=random.randint(1,1284)
    print(id_s)
    song_detail=Song.objects.get(id=id_s)
    #print(movie_detail.year)
 
    song_name = song_detail.title
    name=song_name.split()
    print(name)
    result=[]
    result_name=''
    
    result_name=pig_latin(name)

    song_detail={"name":result_name, "message":message , "user_name":user_name, "score":score}
    return render(request,"song.html", {'song_detail': song_detail})

def check_answer_song(request):
    global song_name,message,result_name,user_name,score
    user_answer= request.GET['answer']
    print(user_answer)
    if user_answer == song_name:
        message="That was correct strike."
        score+=10
        user_details.objects.filter(name=user_name).update(score=score)
        return song_game(request)
    else:
        message="You need to try again."
        print("Not Correct")
    song_detail={"user_name":user_name,"name":result_name,"message":message,"score":score}
    print(result_name)
    return render(request,'song.html',{'song_detail': song_detail})

# Create your views here.


