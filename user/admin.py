from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email','password','level','store','address','phone_number','kakao','kakao_store','register_date',)
    list_filter = ['register_date']
    search_fields = ['email','store']

    fieldsets = [
        ('EMAIL', {'fields': ['email']}),
        ("PASSWORD", {'fields' : ['password']}),
        ('LEVEL',{'fields':['level']}),
        ('STORE',{'fields':['store']}),
        ('ADDRESS', {'fields': ['address']}),
        ('PHONE_NUMBER', {'fields': ['phone_number']}),
        ('KAKAO', {'fields': ['kakao']}),
        ('KAKAO_STORE', {'fields': ['kakao_store']})
    ]
#    inlines = [ChoiceInline]

admin.site.register(User, UserAdmin)
#admin.site.register(Choice)
# Register your models here.