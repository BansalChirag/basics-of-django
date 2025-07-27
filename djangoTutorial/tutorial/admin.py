# Import the necessary models to register them in the Django admin.


from django.contrib import admin
from .models import ChaiVariety,ChaiReview,ChaiCertificate,Store


#  ChaiReviewInLine
# python
# Copy
# Edit

# ✅ Adds an inline form for ChaiReview inside the ChaiVariety admin page in tabular format.

# extra = 2: Shows 2 empty forms by default for adding new reviews.

# This makes it easy to add/edit ChaiReview objects directly from the ChaiVariety page.

class ChaiReviewInLine(admin.TabularInline):
    model = ChaiReview
    extra = 1


# customizes how the ChaiVariety model appears in the Django admin list view:

# list_display: Shows columns like name, price, etc. in the list.

# search_fields: Adds a search box to search by name.

# list_filter: Adds filters in the sidebar for filtering by type.

# inlines: Includes related ChaiReview form on the detail page.

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date_added', 'type')
    search_fields = ('name',)
    list_filter = ('type',)
    inlines = [ChaiReviewInLine,]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)
    
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai_variety', 'certificate_number',)
    # search_fields = ('certificate_number',)



# Regsitering the ChaiVariety model with the admin site
admin.site.register(ChaiVariety,ChaiVarietyAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin,)
