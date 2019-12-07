from django.contrib import admin
from blog.models import Post, Grade, UserInfo, Student


def gender(self):
    if self.sex:
        return "男"
    return "女"

gender.short_description = "性别"


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'body']
    search_fields = ['title', 'body']
    list_filter = ['id', 'title']
    list_per_page = 2
    ordering = ['id']
    fields = ['title', 'body']


class StudentInline(admin.StackedInline):
    model = Student
    extra = 5

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', gender]

class GradeAdmin(admin.ModelAdmin):
    inlines = [StudentInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(UserInfo)
admin.site.register(Student, StudentAdmin)
