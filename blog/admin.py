from django.contrib import admin
from blog.models import Articles, Tag, Classification, Author

class AuthorAdmin(admin.ModelAdmin):
	list_display=('name','email','website')
	search_fields=['name']

class ArticlesAdmin(admin.ModelAdmin):
	list_display=('title','content','pub_date','update_date','author','classification','caption','subcaption')
	list_filter=['pub_date']
	date_hierarchy='pub_date'
	ordering=('-pub_date',)
	filter_horizontal=('tags',)

admin.site.register(Author,AuthorAdmin)
admin.site.register(Articles,ArticlesAdmin)
admin.site.register(Tag)
admin.site.register(Classification)

