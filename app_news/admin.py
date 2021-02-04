from django.contrib import admin
from .models import News, StatusNews, Comments


class CommentInLine(admin.TabularInline):
    model = Comments


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'update_at', 'status',)
    inlines = [CommentInLine]
    list_filter = ('status',)
    actions = [f'mark_as_{status}' for status in StatusNews.objects.all()]

    def mark_as_draft(self, request, queryset):
        self._change_status(request, queryset, status_name='draft')

    def mark_as_publisher(self, request, queryset):
        self._change_status(request, queryset, status_name='publisher')

    def mark_as_archive(self, request, queryset):
        self._change_status(request, queryset, status_name='archive')

    def _change_status(self, request, queryset, status_name):
        status_id = StatusNew.objects.get(status=status_name)
        queryset.update(status=status_id)

    mark_as_draft.short_description = 'Mark selected news as draft'
    mark_as_publisher.short_description = 'Mark selected news as publisher'
    mark_as_archive.short_description = 'Mark selected news as archive'


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('username', 'show_comment')
    list_filter = ('username',)
    actions = ['mark_as_deleted_by_admin']

    def mark_as_deleted_by_admin(self, request, queryset):
        text = '***текст удален администратором***'
        queryset.update(comment=text)

    mark_as_deleted_by_admin.short_description = 'Mark selected comments as deleted by admin'

    def show_comment(self, obj):
        permissible_length = 15
        comment = obj.comment
        return comment if len(comment) < permissible_length else comment[:permissible_length] + '...'

    show_comment.short_description = 'comment'


@admin.register(StatusNews)
class StatusNews(admin.ModelAdmin):
    pass
