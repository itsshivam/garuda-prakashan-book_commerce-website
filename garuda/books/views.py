from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.http import HttpResponse, JsonResponse
from random import randint
import os
import json
from .models import author_detail, book_detail, garuda_news, people_message, newsletter, affiliators_detail, distributors_detail, want_to_join

from django.core import serializers
# Create your views here.



def main_page(request):
    return render(request, "index.html", {})

# Starting of Books Pages

def all_books(request):
    return render(request, "all_books.html", {})

def new_release(request):
    return render(request, "new_release.html", {})

def competitive_exam(request):
    return render(request, "competitive_exam.html", {})

def upcoming_books(request):
    return render(request, "upcoming_book.html")

# Ending of Books Pages

# Starting of Join Us pages

def newsletter_page(request):
    return render(request, "newsletter.html", {})

# Ending of Join Us pages

# Starting of opportunities pages

def get_published(request):
    return render(request, "get_published.html", {})

def career_with_us(request):
    return render(request, "career_with_us.html", {})

def join_as_affiliate(request):
    return render(request, "join_as_affiliate.html", {})

def join_as_distributor(request):
    return render(request, "join_as_distributor.html", {})

# Ending of opportunities pages

def our_authors(request):
    return render(request, "our_authors.html", {})

def our_team(request):
    return render(request, "our_team.html", {})

def our_partners(request):
    return render(request, "our_partners.html", {})

def advisors_and_benefactors(request):
    return render(request, "advisors_benefactors.html", {})

# Starting of footer pages

def aboutus_page(request):
    return render(request, "about_us.html", {})

def message_us(request):
    return render(request, "message_us.html", {})

# Ending of footer pages

# Book and Authir Page

def book_page(request):
    return render(request, "book.html", {})

def author_page(request):
    return render(request, "author.html", {})
# Ending of Book and Author Page

def book_code(request):
    if request.method == "POST":
        if request.is_ajax():
            name = request.POST.get("name")
            query = book_detail.objects.get(name__iexact = name)
            author_name = query.author_name
            query1 = author_detail.objects.get(name__iexact = author_name)
            recommend = None
            if query.recommendation != "":
                recommend = {}
                recommendation = query.recommendation.split("\n")
                c = 0
                for x in recommendation:
                    y = int(x)
                    query2 = book_detail.objects.get(book_id = y)
                    temp = {
                        "url" : "http://127.0.0.1:8000%s" %query2.front_image.url,
                        "name" : query2.name,
                    }
                    recommend[c] = temp
                    c += 1
            data = {
                "url" : "http://127.0.0.1:8000%s" %query.front_image.url,
                "name" : query.name,
                "author_name" : query.author_name,
                "isbn" : query.isbn_number,
                "asin" : query.asin,
                "amazon_kindle" : query.amazon_kindle,
                "amazon_paperback" : query.amazon_paperback,
                "amazon_hardcover" : query.amazon_hardcover,
                "flipkart_kindle" : query.flipkart_kindle,
                "flipkart_paperback" : query.flipkart_paperback,
                "flipkart_hardcover" : query.flipkart_hardcover,
                "description" : query.description,
                "amazon_link" : query.amazon_link,
                "flipkart_link" : query.flipkart_link,
                "recommendation" : recommend,
                "reviews" : query.reviews,
                "facebook_link" : query1.facebook_link,
                "twitter_link" : query1.twitter_link,
                "instagram_link" : query1.instagram_link,
                "google_plus_link" : query1.google_plus_link,
                "author_image" : "http://127.0.0.1:8000%s" %query1.main_image.url,
            }
            return JsonResponse(data)

def author_code(request):
    if request.method == "POST":
        if request.is_ajax():
            name = request.POST.get("name")
            print name
            query = author_detail.objects.get(name__iexact = name)
            recommend = None
            if query.recommendation:
                recommend = {}
                recommendation = query.recommendation.split("\n")
                c = 0
                for x in recommendation:
                    y = int(x)
                    query2 = book_detail.objects.get(book_id = y)
                    temp = {
                        "url" : "http://127.0.0.1:8000%s" %query2.front_image.url,
                        "name" : query2.name,
                    }
                    recommend[c] = temp
                    c += 1
            author_books = None
            if query.list_of_books:
                author_books = {}
                books = query.list_of_books.split("\n")
                c = 0
                for x in books:
                    y = int(x)
                    query2 = book_detail.objects.get(book_id = y)
                    temp = {
                        "url" : "http://127.0.0.1:8000%s" %query2.front_image.url,
                        "name" : query2.name,
                    }
                    author_books[c] = temp
                    c += 1
            data = {
                "url" : "http://127.0.0.1:8000%s" %query.main_image.url,
                "name" : query.name,
                "introduction" : query.introduction,
                "recommendation" : recommend,
                "author_books" : author_books,
                "facebook_link" : query.facebook_link,
                "twitter_link" : query.twitter_link,
                "instagram_link" : query.instagram_link,
                "google_plus_link" : query.google_plus_link,
                "youtube_video" : query.youtube_video,
            }
            return JsonResponse(data)

def join_as_affiliate_code(request):
    if request.method == "POST":
        if request.is_ajax():
            name = request.POST.get("user")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            message = request.POST.get("message")
            query = affiliators_detail(name = name, email = email, mobile = mobile, message = message)
            query.save()
            data = {
                "message" : "Your details has been sent to us, thanks!!"
            }
            return JsonResponse(data)

def join_as_distributor_code(request):
    if request.method == "POST":
        if request.is_ajax():
            name = request.POST.get("user")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            message = request.POST.get("message")
            query = distributors_detail(name = name, email = email, mobile = mobile, message = message)
            query.save()
            data = {
                "message" : "Your details has been sent to us, thanks!!"
            }
            return JsonResponse(data)

def career_with_us_code(request):
    if request.method == "POST":
        if request.is_ajax():
            name = request.POST.get("user")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            message = request.POST.get("message")
            query = want_to_join(name = name, email = email, mobile = mobile, message = message)
            query.save()
            data = {
                "message" : "Your details has been sent to us, thanks!!"
            }
            return JsonResponse(data)

def news_feed_code(request):
    news = garuda_news.objects.reverse()[0].news_feed
    data = {
        "news" : news,
    }
    return JsonResponse(data)

def message_us_code(request):
    if request.method == "POST":
        if request.is_ajax():
            name = request.POST.get("user")
            email = request.POST.get("email")
            message = request.POST.get("message")
            query = people_message(name = name, email = email, msg = message)
            query.save()
            data = {
                "message" : "Your message has been sent to us, we'll reply you soon."
            }
            return JsonResponse(data)

def newsletter_page_code(request):
    if request.method == "POST":
        if request.is_ajax():
            email = request.POST.get("email")
            query = newsletter(user_email = email)
            query.save()
            data = {
                "message" : "Your Email ID is sent to us, thanks!!"
            }
            return JsonResponse(data)

def books_on_main_page(request):
    query_list = book_detail.objects.filter(show_on_main_page = "Yes")
    book_list = {}
    c = 0
    for x in query_list:
        book = {
            "url" : "http://127.0.0.1:8000%s" %x.front_image.url,
            "name" : x.name,
            "isbn" : x.isbn_number,
        }
        book_list[c] = book
        c +=1
    return JsonResponse(book_list)

def authors_on_main_page(request):
    query_list = author_detail.objects.filter(show_on_main_page = "Yes")
    author_list = {}
    c = 0
    for x in query_list:
        books = x.list_of_books.split("\n")
        print books
        author = {
            "url" : "http://127.0.0.1:8000%s" %x.main_image.url,
            "name" : x.name,
        }
        author_list[c] = author
        c +=1
    return JsonResponse(author_list)

def upcoming_books_code(request):
    query_list = book_detail.objects.filter(upcoming_book = "Yes")
    book_list = {}
    c = 0
    for x in query_list:
        book = {
            "url" : "http://127.0.0.1:8000%s" %x.front_image.url,
            "name" : x.name,
            "isbn" : x.isbn_number,
        }
        book_list[c] = book
        c +=1
    return JsonResponse(book_list)

def competitive_exam_code(request):
    query_list = book_detail.objects.filter(competitive_exam = "Yes")
    book_list = {}
    c = 0
    for x in query_list:
        book = {
            "url" : "http://127.0.0.1:8000%s" %x.front_image.url,
            "name" : x.name,
            "isbn" : x.isbn_number,
        }
        book_list[c] = book
        c +=1
    return JsonResponse(book_list)

def new_release_code(request):
    query_list = book_detail.objects.filter(new_release = "Yes")
    book_list = {}
    c = 0
    for x in query_list:
        book = {
            "url" : "http://127.0.0.1:8000%s" %x.front_image.url,
            "name" : x.name,
            "isbn" : x.isbn_number,
        }
        book_list[c] = book
        c +=1
    return JsonResponse(book_list)

def all_books_code(request):
    query_list = book_detail.objects.all()
    book_list = {}
    c = 0
    for x in query_list:
        book = {
            "url" : "http://127.0.0.1:8000%s" %x.front_image.url,
            "name" : x.name,
            "isbn" : x.isbn_number,
        }
        book_list[c] = book
        c +=1
    return JsonResponse(book_list)

def our_authors_code(request):
    query_list = author_detail.objects.all()
    author_list = {}
    c = 0
    for x in query_list:
        books = x.list_of_books.split("\n")
        print books
        author = {
            "url" : "http://127.0.0.1:8000%s" %x.main_image.url,
            "name" : x.name,
        }
        author_list[c] = author
        c +=1
    return JsonResponse(author_list)

def delete_files(request):
    if request.method == "POST":
        if request.is_ajax():
            form_type = request.POST.get("form_type")
            if form_type == "author":
                author_name = request.POST.get("author_name")
                file_type = request.POST.get("file_type")
                query = author_detail.objects.get(name = author_name)
                if file_type == "main_image":
                    if query.main_image:
                        x = query.main_image.name
                        path = "media_cdn/%s" %x
                        query.main_image.delete()
                        return HttpResponse("Your request has been completed")
                    else:
                        return HttpResponse("Main image doesn't exists!!")
                elif file_type == "image1":
                    if query.image1:
                        x = query.image1.name
                        path = "media_cdn/%s" %x
                        query.image1.delete()
                        return HttpResponse("Your request has been completed")
                    else:
                        return HttpResponse("Image1 doesn't exists!!")
                elif file_type == "image2":
                    if query.image2:
                        x = query.image2.name
                        path = "media_cdn/%s" %x
                        query.image2.delete()
                        return HttpResponse("Your request has been completed")
                    else:
                        return HttpResponse("Image2 doesn't exists!!")
                else:
                    return HttpResponse("Entered file type doesn't exist")

            elif form_type == "book":
                book_name = request.POST.get("book_name")
                file_type_book = request.POST.get("file_type_book")
                query = book_detail.objects.get(name = book_name)
                if file_type_book == "front_image":
                    if query.front_image:
                        x = query.front_image.name
                        path = "media_cdn/%s" %x
                        query.front_image.delete()
                        return HttpResponse("Your request has been completed")
                    else:
                        return HttpResponse("Front Image pic doesn't exist")
                elif file_type_book == "back_image":
                    if query.back_image:
                        x = query.back_image.name
                        path = "media_cdn/%s" %x
                        query.back_image.delete()
                        return HttpResponse("Your request has been completed")
                    else:
                        return HttpResponse("Back Image pic doesn't exist")
                elif file_type_book == "image1":
                    if query.image1:
                        x = query.image1.name
                        path = "media_cdn/%s" %x
                        query.image1.delete()
                        return HttpResponse("Your request has been completed")
                    else:
                        return HttpResponse("Image1 pic doesn't exist")
                elif file_type_book == "image2":
                    if query.image2:
                        x = query.image2.name
                        path = "media_cdn/%s" %x
                        query.image2.delete()
                        return HttpResponse("Your request has been completed")
                    else:
                        return HttpResponse("Image2 pic doesn't exist")
                elif file_type_book == "image3":
                    if query.image3:
                        x = query.image3.name
                        path = "media_cdn/%s" %x
                        query.image3.delete()
                        return HttpResponse("Your request has been completed")
                    else:
                        return HttpResponse("Image3 pic doesn't exist")
                elif file_type_book == "preview":
                    if query.preview:
                        x = query.preview.name
                        path = "media_cdn/%s" %x
                        query.preview.delete()
                        return HttpResponse("Your request has been completed")
                    else:
                        return HttpResponse("Preview of the book doesn't exist")
                elif file_type_book == "book":
                    if query.book:
                        x = query.book.name
                        path = "media_cdn/%s" %x
                        query.book.delete()
                        return HttpResponse("Your request has been completed")
                    else:
                        return HttpResponse("Book doesn't exist in the database")
                else:
                    return HttpResponse("Entered file type doesn't exist!!!")
    else:
        query = author_detail.objects.all()
        name = []
        for user in query:
            name.append(user.name)
        query1 = book_detail.objects.all()
        book = []
        for x in query1:
            book.append(x.name)
        context = {
            "name_list" : name,
            "book_list" : book,
        }
        return render(request, "delete_files.html", context)
