from .forms import LoginForm, SearchForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from .nike_search import search
from .models import User

# Create your views here.
class LoginView(FormView):
    template_name = 'search/login.html'
    form_class = LoginForm
    success_url = '/main/search/'

    def form_valid(self, form):
        #self.request.session['user'] = form.email # 세션에 아이디 저장
        self.request.session['user'] = form.data.get('email')  # 세션에 아이디 저장
        return super().form_valid(form)

def logout(request):
    if 'user' in request.session:
        del(request.session['user'])
    #return redirect('/login') # 로그인 페이지로
    return redirect('')  # 로그인 페이지로

    ################################################
    ################################################
    ##### POST 방식 ####

def search_product(request):
    user = request.session.get('user')
    if not user:
        messages.error(request, '로그인해주세요.')
        #return redirect('/login/')
        return redirect('')
    # 로그인 안하고 글 작성 시 오류 발생
    #if not request.session.get('email'):
    #    return redirect('login/')
    else:
         # request에 product_code 라는 이름으로 데이터 저장
        return render(request, 'search/search.html') # html 파일 주소

def detail(request):
    if request.method == 'POST':
        product_code = request.POST['product_code']

        user_id = request.session.get('user')  # 세션으로부터 유저 정보 가져오기
        if user_id:
            user = User.objects.get(email=user_id)
            if (len(product_code) == 10 ) and ('-' in product_code):
                try:
                    data = search.search_item(product_code)
                    data['store'] = user.store
                    data['address'] = user.address
                    data['phone_number'] = user.phone_number
                    data['kakao'] = user.kakao
                    data['kakao_store'] = user.kakao_store
                    context = {'data':data}
                    return render(request, 'search/detail.html', context)
                except:
                    messages.error(request,'품번을 제대로 입력해주세요.')
                    return redirect('/main/search/')
            else:
                messages.error(request, '품번을 제대로 입력해주세요.')
                return redirect('/main/search/')
        else:
            messages.error(request,'로그인해주세요.')
            #return redirect('/login/')
            return redirect('')