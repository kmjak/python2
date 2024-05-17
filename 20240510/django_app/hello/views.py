from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import SessionForm

## getリクエストの受け取り方
# Create your views here.
# def index(request):
#     if 'msg' in request.GET:
#         msg = request.GET['msg']
#         result = 'you typed:"' + msg + '".'
#     else:
#         result = 'please send msg parameter!'

## 
# def index(request,id,nickname):
#     result = 'id: ' + str(id) + "name: " + nickname
#     return HttpResponse(result)

## ３ページ遷移
# def index(request):
#     params = {
#         'title':'hello/index',
#         'msg':'this is sample page',
#         'goto':'next'
#     }
#     return render(request,'hello/index.html',params)
# def next(request):
#     params = {
#         'title':'hello/next',
#         'msg':'this is next page',
#         'goto':'test'
#     }
#     return render(request,'hello/index.html',params)
# def test(request):
#     params = {
#         'title':'hello/test',
#         'msg':'this is test page',
#         'goto':'index'
#     }
#     return render(request,'hello/index.html',params)

## formを作る
# def index(request):
#     params = {
#         'title':'Hello/Index',
#         'msg':'お名前は?'
#     }
#     return render(request, 'hello/index.html', params)

# def form(request):
#     msg = request.POST['msg']
#     params = {
#         'title':'Hello/Form',
#         'msg':'こんにちは' + msg + 'さん。'
#     }
#     return render(request, 'hello/index.html', params)

## forms.pyを使ってformを作る
# def index(request):
#     params = {
#         'title':'Hello',
#         'message':'your data',
#         'form':HelloForm()
#     }
#     if request.method == 'POST':
#         params['message'] = '名前' + request.POST['name'] + \
#             '<br>メール:' + request.POST['mail'] + \
#             '<br>年齢:' + request.POST['age']
#         params['form'] = HelloForm(request.POST)
#     return render(request,'hello/index.html',params)

## HelloViewクラスを作る
# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             'title':'Hello',
#             'message': 'your data',
#             'form': HelloForm()
#         }
#     def get(self,request):
#         return render(request, 'hello/index.html', self.params)
#     def post(self,request):
#         msg = 'あなたは、<b>' + request.POST['name'] + '(' + request.POST['age'] + ')</b>さんです。<br>メールアドレスは<b>' + request.POST['mail'] + '</b>ですね。'
#         self.params['message'] = msg
#         self.params['form'] = HelloForm(request.POST)
#         return render(request,"hello/index.html",self.params)

## checkboxをクリックするとsuccessと表示する
# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             'title' : 'hello',
#             'form' : HelloForm(),
#             'result' :  None
#         }
#     def get(self,request):
#         return render(request,"hello/index.html",self.params)
#     def post(self,request):
#         if('check' in request.POST):
#             self.params['result'] = 'Checked!!'
#         else:
#             self.params['result'] = "Not Checked.."
#         self.params['form'] = HelloForm(request.POST)
#         return render(request,"hello/index.html",self.params)

## null も含めたcheck box
# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             'title':'',
#             'form':HelloForm(),
#             'result':None
#         }
#     def get(self,request):
#         return render(request,"hello/index.html",self.params)
#     def post(self,request):
#         chk = request.POST['check']
#         self.params['result'] = "you checked " + chk + "."
#         self.params['form'] = HelloForm(request.POST)
#         return render(request,"hello/index.html",self.params)

## プルダウンメニューの作成(ラジオボタン、選択リストでも同じでできる)
# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             'title':'',
#             'form':HelloForm(),
#             'result':None
#         }
#     def get(self,request):
#         return render(request,"hello/index.html",self.params)
#     def post(self,request):
#         ch = request.POST['choice']
#         self.params['result'] = "you checked " + ch + "."
#         self.params['form'] = HelloForm(request.POST)
#         return render(request,"hello/index.html",self.params)

## 複数選択項目リスト
# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             'title':'',
#             'form':HelloForm(),
#             'result':None
#         }
#     def get(self,request):
#         return render(request,"hello/index.html",self.params)
#     def post(self,request):
#         ch = request.POST.getlist('choice')
#         self.params['result'] = "you checked " + str(ch) + "."
#         self.params['form'] = HelloForm(request.POST)
#         return render(request,"hello/index.html",self.params)

## session 
class HelloView(TemplateView):
    def __init__(self):
        self.params = {
            'title':'',
            'form':SessionForm(),
            'result':None
        }
    def get(self,request):
        self.params['result'] = request.session.get('last_msg','No message')
        return render(request,"hello/index.html",self.params)
    def post(self,request):
        ses = request.POST['session']
        self.params['result'] = "send : '" + ses + "'."
        # request.session['last_msg'] = ses    なんかエラー出る
        self.params['form'] = SessionForm(request.POST)
        return render(request,"hello/index.html",self.params)
