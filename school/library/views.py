from django.shortcuts import render, redirect
from .models import Book, Comment
from .forms import CommentForm
from django.urls import reverse

fav_book_list = []
# Create your views here.
def index(request):
    all_books = Book.objects.all().order_by('-library_date')[:2]

    return render(request, 'library/index.html',{
        'books': all_books
    })


def all_books(request):
    all_books = Book.objects.all()
    return render(request, 'library/all-books.html', {
        'books': all_books
    })


def book_detail(request, slug):
    selected_book = Book.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data
            comment = Comment.objects.create(
                user_name = key['user_name'],
                user_text = key['comment'],
            )
            # Once the comment is saved in its model, we now relate it with particular book
            # for which comment was submitted to begin with
            selected_book.comments.add(comment)
            return redirect(reverse('book-detail', args=[slug]))
    
    # GET Method
    form = CommentForm()

    # Check if Favorite Book is pressed.
    # Remember book_id will be STRING type returned by sessions
    fav_book_ids = request.session.get('fav_book_ids')
    if fav_book_ids is not None:
        button_pressed = str(selected_book.id) in fav_book_ids
    else:
        button_pressed = False

    return render(request, 'library/book_detail.html', {
        'book': selected_book,
        'departments': selected_book.department.all(),
        'form': form,
        'comments': selected_book.comments.all(),
        'button_pressed': button_pressed,
    })


def favourite_book(request):
    if request.method == 'POST':
        # Always remeber that session returns STRING data type
        # Therefore, id will not be an Integer
        book_id = request.POST['fav_book']

        # Since we will not have any list in the beginning we could do the following
        # session.get() won't give any error (since there will be no list to begin with)
        # that's the beauty of using it
        fav_book_ids = request.session.get('fav_book_ids')

        # Now here we will create the list only once in beginning because above line of code returns None
        if fav_book_ids is None or len(fav_book_ids) == 0:
            fav_book_ids = []
        
        if book_id in fav_book_ids:
            fav_book_ids.remove(book_id)
        else:
            fav_book_ids.append(book_id)
        
        request.session['fav_book_ids'] = fav_book_ids
        return redirect('home-page')


    # GET Method

    # Since we will not have any list in the beginning we could do the following
    # session.get() won't give any error (since there will be no list to begin with)
    # that's the beauty of using it
    fav_book_ids = request.session.get('fav_book_ids')

    # Now here we will create the list only once in beginning because above line of code returns None
    if fav_book_ids is None or len(fav_book_ids) == 0:
        fav_book_ids = []
        is_list_empty = True
    else:
        is_list_empty = False
    
    # Update the fav_book_ids with sessions
    request.session['fav_book_ids'] = fav_book_ids
    all_fav_books = Book.objects.filter(pk__in=fav_book_ids)
    
    return render(request, 'library/all-fav-books.html', {
        'fav_books': all_fav_books,
        'list_is_empty': is_list_empty,
    })
