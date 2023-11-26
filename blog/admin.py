from abc import ABC

from django.contrib import admin
from . import models


class FilterTitle(admin.SimpleListFilter):
    title = "عناوین پر تکرار"
    parameter_name = "title"

    def lookups(self, request, model_admin):
        return (
            ('python', 'پایتون'),
            ('java', 'جاوا'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())


# class FilterCategory(admin.SimpleListFilter):
#     title = "محبوب ترین دسته بندی ها"
#     parameter_name = "category"
#
#     def lookups(self, request, model_admin):
#         return(
#             ('Game', 'بازی'),
#             ('Programming', 'برنامه نویسی')
#         )
#
#     def queryset(self, request, queryset):
#         if self.value():
#             if self.value().isdigit():
#                 return queryset.filter(category=int(self.value()))
#             else:
#                 return queryset.filter(category__exact=self.value())
#         # if self.value():
#         #     return queryset.filter(category=int(self.value()))


class CommentInLine(admin.TabularInline):
    model = models.Comment


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "show_image")
    list_filter = ("created", FilterTitle)
    search_fields = ("title", "body", "created", "category")
    inlines = (CommentInLine,)


admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Message)
admin.site.register(models.Like)

