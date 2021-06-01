from django import forms
from .models import User

class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={'required':'아이디를 입력해주세요.'},
        max_length=64, label='이메일'
    )

    password = forms.CharField(
        error_messages={'required': '비밀번호를 입력해주세요.'},
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
                if password != user.password:
                    self.add_error('password', '비밀번호가 틀렸습니다.')
                #else: --> view에서 처리
                #    self.email = fcuser.email # email을 form에 저장

            except User.DoesNotExist:
                self.add_error('email', "아이디가 없습니다.")


class SearchForm(forms.Form):
    product_code = forms.CharField(error_messages={
        'required': '품번을 입력하세요'
    },
        max_length=100, label='AA1234-101')

    def clean(self):
        cleaned_data = super().clean() # form에서 clean이라는 함수가 이미 있음
        product_code = cleaned_data.get('product_code')
        if product_code and len(product_code) != 10 :
            self.add_error('product_code','품번을 입력하세요. 예) AA1111-111')
        else:
            self.product_code = product_code # session을 위해 id 반환

#class ShowForm(forms.Form):
