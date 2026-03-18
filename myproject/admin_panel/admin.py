from django.contrib import admin
from myproject.ott.models import Content, Genre, Tag, Person

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'status', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('content_type', 'status')
    # Added detailed admin features for content management
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('content_type')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order')
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
