from django.contrib import admin
from .models import Review, Review1, Review2, Review3, Review4, Review5, Review6, Review7


class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Review, ReviewAdmin)
admin.site.register(Review1, ReviewAdmin)
admin.site.register(Review2, ReviewAdmin)
admin.site.register(Review3, ReviewAdmin)
admin.site.register(Review4, ReviewAdmin)
admin.site.register(Review5, ReviewAdmin)
admin.site.register(Review6, ReviewAdmin)
admin.site.register(Review7, ReviewAdmin)