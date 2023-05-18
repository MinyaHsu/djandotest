from django.shortcuts import render, redirect

# Create your views here.
from students.models import student
from students.form import PostForm

def listone(request): 
    try: 
        unit = student.objects.get(stdName="許茗雅") #讀取一筆資料
    except:
        errormessage = " (讀取錯誤!)"
    return render(request, "student/listone.html", locals())

def listall(request):  
    allStudents = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "student/listall.html", locals())

def post(request):
    #判斷表單資料傳送方式
    if request.method == "POST":
        #接收傳送資料
        stdName = request.POST['stdName']
        stdID = request.POST['stdID']
        stdSex = request.POST['stdSex']
        stdBirth = request.POST['stdBirth']
        stdPhone = request.POST['stdPhone']
        stdEmail = request.POST['stdEmail']
        #新增一筆紀錄
        unit = student.objects.create(stdName=stdName, stdID=stdID, stdSex=stdSex, stdBirth=stdBirth, stdPhone=stdPhone, stdEmail=stdEmail)
        unit.save() #寫入資料庫
        return redirect('/listall/')
    else:
        mess = '請輸入資料(資料不做驗證)'
    return render(request, "student/addstudent.html", locals())

def postform(request):
    #新增PostForm表單物件
    stdform = PostForm()
    return render(request, "student/stdform.html", locals())

def delete(request, stdID=None):
    if stdID != None:
        if request.method == "POST":
            stdID = request.POST["stdID"]
        #嘗試抓取此id之學生
        #嘗試try區塊的程式碼，如果發生錯誤或例外情形 執行except區塊之程式碼
        try:
            unit = student.objects.get(stdID=stdID)
            #刪除資料
            unit.delete()
            return redirect('/listall/')
        except:
            mess = "查無該學號"
    return render(request, "student/delete.html", locals())

def edit(request, stdID=None, mode=None):
    if mode == "edit":
        unit = student.objects.get(stdID=stdID)
        unit.stdName = request.GET['stdName']
        unit.stdID = request.GET['stdID']
        unit.stdSex = request.GET['stdSex']
        unit.stdBirth = request.GET['stdBirth']
        unit.stdPhone = request.GET['stdPhone']
        unit.stdEmail = request.GET['stdEmail']
        unit.save()
        mess = "已修改完成"
        return redirect('/listall/')
    else:
        try:
            unit = student.objects.get(stdID=stdID)
            strDate = str(unit.stdBirth)
            strDate2 = strDate.replace(" 年 ", "-")
            strDate2 = strDate.replace(" 月 ", "-")
            strDate2 = strDate.replace(" 日 ", "-")
            unit.stdBirth = strDate2
        except:
            mess = "此學號不存在"
        return render(request, "student/edit.html", locals())
    