from __future__ import unicode_literals
from django.db import models

# Create your models here.
category_choices = (
    ("Academic", "Academic"),
    ("Competitive", "Competitive"),
    ("Science fiction", "Science fiction"),
    ("Satire", "Satire"),
    ("Drama", "Drama"),
    ("Action and Adventure", "Action and Adventure"),
    ("Romance", "Romance"),
    ("Mystery", "Mystery"),
    ("Horror", "Horror"),
    ("Self help", "Self help"),
    ("Health", "Health"),
    ("Guide", "Guide"),
    ("Travel", "Travel"),
    ("Children's", "Children's"),
    ("Religion, Spirituality & New Age", "Religion, Spirituality & New Age"),
    ("Science", "Science"),
    ("History", "History"),
    ("Math", "Math"),
    ("Anthology", "Anthology"),
    ("Poetry", "Poetry"),
    ("Encyclopedias", "Encyclopedias"),
    ("Dictionaries", "Dictionaries"),
    ("Comics", "Comics"),
    ("Art", "Art"),
    ("Cookbooks", "Cookbooks"),
    ("Diaries", "Diaries"),
    ("Journals", "Journals"),
    ("Prayer books", "Prayer books"),
    ("Series", "Series"),
    ("Trilogy", "Trilogy"),
    ("Biographies", "Biographies"),
    ("Autobiographies", "Autobiographies"),
    ("Fantasy", "Fantasy"),
)

yes_no_choice = (
    ("Yes", "Yes"),
    ("No", "No"),
)
def upload_location_books(instance, filename):
    return "books/%s/%s" %(instance.name, filename)

class book_detail(models.Model):
    book_id = models.CharField(max_length = 10, blank = True, null = True)
    name = models.CharField(max_length = 100, blank = True)
    front_image = models.FileField(upload_to = upload_location_books, null = True, blank = True)
    back_image = models.FileField(upload_to = upload_location_books, null = True, blank = True)
    image1 = models.FileField(upload_to = upload_location_books, null = True, blank = True)
    image2 = models.FileField(upload_to = upload_location_books, null = True, blank = True)
    image3 = models.FileField(upload_to = upload_location_books, null = True, blank = True)
    description = models.TextField(blank = True, null = True)
    category = models.CharField(max_length = 20, choices = category_choices, blank = True, null = True)
    author_name = models.CharField(max_length = 30, blank = True, null = True)
    isbn_number = models.CharField(max_length = 30, blank = True, null = True)
    asin = models.CharField(max_length = 30, blank = True, null = True)
    mrp = models.CharField(max_length = 10, blank = True, null = True)
    discount = models.CharField(max_length = 10, blank = True, null = True)
    selling_price = models.CharField(max_length = 10, blank = True, null = True)
    preview = models.FileField(upload_to = upload_location_books, null = True, blank = True)
    book = models.FileField(upload_to = upload_location_books, null = True, blank = True)
    new_release = models.CharField(max_length = 5, choices = yes_no_choice, default = "No")
    upcoming_book = models.CharField(max_length = 5, choices = yes_no_choice, default = "No")
    show_on_main_page = models.CharField(max_length = 5, choices = yes_no_choice, default = "No")
    competitive_exam = models.CharField(max_length = 5, choices = yes_no_choice, default = "No")
    amazon_kindle = models.CharField(max_length = 10, blank = True, null = True)
    amazon_hardcover = models.CharField(max_length = 10, blank = True, null = True)
    amazon_paperback = models.CharField(max_length = 10, blank = True, null = True)
    flipkart_kindle = models.CharField(max_length = 10, blank = True, null = True)
    flipkart_hardcover = models.CharField(max_length = 10, blank = True, null = True)
    flipkart_paperback = models.CharField(max_length = 10, blank = True, null = True)
    amazon_link = models.CharField(max_length = 100, blank = True, null = True)
    flipkart_link = models.CharField(max_length = 100, blank = True, null = True)
    recommendation = models.TextField(blank = True, null = True)
    reviews = models.TextField(blank = True, null = True)
    updated = models.DateTimeField(auto_now = True, auto_now_add = False)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
    def __unicode__(self):
        return self.name

gender_choice = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Others", "Others")
)

def upload_location_authors(instance, filename):
    return "authors/%s/%s" %(instance.name, filename)

class author_detail(models.Model):
    author_id = models.CharField(max_length = 10, blank = True, null = True)
    name = models.CharField(max_length = 30)
    list_of_books = models.TextField(blank = True, null = True)
    introduction = models.TextField(blank = True, null = True)
    main_image = models.FileField(upload_to = upload_location_authors, null = True, blank = True)
    image1 = models.FileField(upload_to = upload_location_authors, null = True, blank = True)
    image2 = models.FileField(upload_to = upload_location_authors, null = True, blank = True)
    email_id = models.CharField(max_length = 30, blank = True)
    phone_no = models.CharField(max_length = 15, blank = True)
    address = models.CharField(max_length = 100, blank = True)
    gender = models.CharField(max_length = 10, choices = gender_choice, blank = True)
    writing_field = models.CharField(max_length = 20, choices = category_choices, blank = True)
    youtube_video = models.CharField(max_length = 150, blank = True)
    show_on_main_page = models.CharField(max_length = 5, choices = yes_no_choice, default = "No")
    recommendation = models.TextField(blank = True, null = True)
    facebook_link = models.CharField(max_length = 100, blank = True, null = True)
    twitter_link = models.CharField(max_length = 100, blank = True, null = True)
    instagram_link = models.CharField(max_length = 100, blank = True, null = True)
    google_plus_link = models.CharField(max_length = 100, blank = True, null = True)
    updated = models.DateTimeField(auto_now = True, auto_now_add = False)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
    def __unicode__(self):
        return self.name

class newsletter(models.Model):
    user_email = models.CharField(max_length = 30)
    def __unicode__(self):
        return self.user_email

class garuda_news(models.Model):
    news_feed = models.TextField(blank = True, null = True)
    def __unicode__(self):
        return self.news_feed

class people_message(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    msg = models.TextField(blank = True, null = True)
    def __unicode__(self):
        return self.name

class affiliators_detail(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    mobile = models.CharField(max_length = 15)
    message = models.TextField(blank = True, null = True)
    def __unicode__(self):
        return self.name

class distributors_detail(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    mobile = models.CharField(max_length = 15)
    message = models.TextField(blank = True, null = True)
    def __unicode__(self):
        return self.name

class want_to_join(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    mobile = models.CharField(max_length = 15)
    message = models.TextField(blank = True, null = True)
    def __unicode__(self):
        return self.name
