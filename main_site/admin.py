# # from django.contrib import admin
# from django.contrib import admin
# from main_site.models import NewsItem  # Just an example.
# from main_site.models import Page  # Just an example.

# # Register your models here.

# @admin.register(Page)
# class PageAdmin(admin.ModelAdmin):
#     ...

#     def queryset(self, request):
#         """Limit Pages to those that belong to the request's user."""
#         qs = super(PageAdmin, self).queryset(request)
#         if request.user.is_superuser:
#             # It is mine, all mine. Just return everything.
#             return qs
#         # Now we just add an extra filter on the queryset and
#         # we're done. Assumption: Page.owner is a foreignkey
#         # to a User.
#         return qs.filter(owner=request.user)

# # admin.site.register(Page, PageAdmin)