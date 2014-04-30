from django.contrib import admin
from posts.models import Post,Comment

# Register your models here.
class ChoiceInline(admin.StackedInline):
	model = Comment
	extra = 3
class PostAdmin(admin.ModelAdmin):
	inlines = [ChoiceInline]
	list_display = ('title','score','pub_date')
	list_filter =['pub_date']
	search_fields = ['title']

admin.site.register(Post,PostAdmin)
