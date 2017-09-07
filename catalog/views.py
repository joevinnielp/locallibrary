from django.shortcuts import render, get_object_or_404
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Authentication
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.views.generic import View


# Create your views here.

class MyView(LoginRequiredMixin,generic.View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = BookInstance
    template_name ='bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


''' def book_detail_view(request,pk):
	    try:
	        book_id=Book.objects.get(pk=pk)
	    except Book.DoesNotExist:
	        raise Http404("Book does not exist")

	    book_id=get_object_or_404(Book, pk=pk)
	    
	    return render(request, "book_detail.html", context={'book':book_id,})'''

class BookDetailView(generic.DetailView):
    model = Book
    def get(self, request, pk):
            book = Book.objects.all()
            author = Author.objects.all()
            context = {
                'book': book,
                'author': author, 
            }

            try:
                book_id=Book.objects.get(pk=pk)
            except Book.DoesNotExist:
                raise Http404("Book does not exist")

            #author_id=get_object_or_404(Author, pk=pk)
                
            return render(request, "book_detail.html", context={'book':book_id,})

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    context_object_name = 'book_list'   # your own name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = "book_list.html"  # Specify your own template name/location

    def get_queryset(self):
        return Book.objects.filter(title__icontains='')[:5] # Get 5 books containing the title war

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class AuthorDetailView(generic.DetailView):
    model = Author
    def get(self, request, pk):
            book = Book.objects.all()
            author = Author.objects.all()
            context = {
                'book': book,
                'author': author, 
            }

            try:
                author_id=Author.objects.get(pk=pk)
            except Author.DoesNotExist:
                raise Http404("Author does not exist")

            #author_id=get_object_or_404(Author, pk=pk)
                
            return render(request, "author_detail.html", context={'author':author_id,})

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10
    context_object_name = 'author_list'   # your own name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = "author_list.html"  # Specify your own template name/location

    def get_queryset(self):
        return Author.objects.filter(last_name__icontains='')[:5] # Get 5 books containing the title war

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context



def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,'num_visits':num_visits}, # num_visits appended
    )