from django.shortcuts import render, get_object_or_404
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.



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
                
            return render(request, "author_detail.html", context={'book':book_id,})

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
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )