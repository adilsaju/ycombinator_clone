from django.contrib import admin

# class user(admin.ModelAdmin):
#     list_display = ("pk", "get_title_or_nothing")

#     def get_form(self, request, obj=None, **kwargs):
#         if obj.type == "1":
#             self.exclude = ("title", )
#         form = super(user, self).get_form(request, obj, **kwargs)
#         return form