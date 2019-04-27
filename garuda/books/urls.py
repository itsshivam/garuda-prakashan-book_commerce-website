from django.conf.urls import url, include
from .views import (
    main_page,
    book_page,
    book_code,
    author_page,
    author_code,
    delete_files,

    all_books,
    all_books_code,
    new_release,
    new_release_code,
    competitive_exam,
    competitive_exam_code,
    upcoming_books,
    upcoming_books_code,

    our_authors,
    our_authors_code,
    our_team,
    our_partners,
    advisors_and_benefactors,

    newsletter_page,
    newsletter_page_code,

    get_published,
    career_with_us,
    career_with_us_code,
    join_as_affiliate,
    join_as_affiliate_code,
    join_as_distributor,
    join_as_distributor_code,

    news_feed_code,
    aboutus_page,
    message_us,
    message_us_code,

    books_on_main_page,
    authors_on_main_page,
)

urlpatterns = [
    url(r'^$', main_page),
    url(r'book/$', book_page),
    url(r'book_code/$', book_code),
    url(r'author_code/$', author_code),
    url(r'author/$', author_page),
    url(r'^delete_files/$', delete_files),

    url(r'^all_books/$', all_books),
    url(r'all_books_code/$', all_books_code),
    url(r'new_releases/$', new_release),
    url(r'new_release_code/$', new_release_code),
    url(r'competitive_exam_books/$', competitive_exam),
    url(r'competitive_exam_code/$', competitive_exam_code),
    url(r'upcoming_books/$', upcoming_books),
    url(r'upcoming_books_code/$', upcoming_books_code),

    url(r'our_authors/$', our_authors),
    url(r'our_authors_code/$', our_authors_code),
    url(r'our_team/$', our_team),
    url(r'our_partners/$', our_partners),
    url(r'advisors_and_benefactors/$', advisors_and_benefactors),

    url(r'newsletter/$', newsletter_page),
    url(r'newsletter_page_code/$', newsletter_page_code),

    url(r'get_published/$', get_published),
    url(r'career_with_us/$', career_with_us),
    url(r'career_with_us_code/$', career_with_us_code),
    url(r'join_as_affiliate/$', join_as_affiliate),
    url(r'join_as_affiliate_code/$', join_as_affiliate_code),
    url(r'join_as_distributor/$', join_as_distributor),
    url(r'join_as_distributor_code/$', join_as_distributor_code),

    url(r'about_us/$', aboutus_page),
    url(r'news_feed_code/$', news_feed_code),
    url(r'message_us/$', message_us),
    url(r'message_us_code/$', message_us_code),

    url(r'books_on_main_page/$', books_on_main_page),
    url(r'authors_on_main_page/$', authors_on_main_page),
]
