from django.contrib import admin
from .models import book_detail, author_detail, newsletter, garuda_news, people_message, affiliators_detail, distributors_detail, want_to_join
# Register your models here.

class book_detail_admin(admin.ModelAdmin):
    list_display = ["book_id", "name", "front_image",  "category", "author_name", "isbn_number", "asin", "mrp", "selling_price", "new_release", "upcoming_book", "show_on_main_page", "competitive_exam", "updated", "timestamp"]
    list_display_links = ["name"]
    class Meta:
        model = book_detail

class author_detail_admin(admin.ModelAdmin):
    list_display = ["author_id", "name", "list_of_books", "main_image", "email_id", "phone_no", "address", "writing_field", "show_on_main_page", "updated", "timestamp"]
    list_display_links = ["name"]
    class Meta:
        model = author_detail

class newsletter_admin(admin.ModelAdmin):
    list_display = ["id", "user_email"]
    class Meta:
        model = newsletter

class garuda_news_admin(admin.ModelAdmin):
    list_display = ["id", "news_feed"]
    list_display_links = ["id", "news_feed"]
    class Meta:
        model = garuda_news

class people_message_admin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "msg"]
    class Meta:
        model = people_message

class affiliators_detail_admin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "mobile", "message"]
    class Meta:
        model = affiliators_detail

class distributors_detail_admin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "mobile", "message"]
    class Meta:
        model = distributors_detail

class want_to_join_admin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "mobile", "message"]
    class Meta:
        model = distributors_detail

admin.site.register(book_detail, book_detail_admin)
admin.site.register(author_detail, author_detail_admin)
admin.site.register(newsletter, newsletter_admin)
admin.site.register(garuda_news, garuda_news_admin)
admin.site.register(people_message, people_message_admin)
admin.site.register(affiliators_detail, affiliators_detail_admin)
admin.site.register(distributors_detail, distributors_detail_admin)
admin.site.register(want_to_join, want_to_join_admin)
