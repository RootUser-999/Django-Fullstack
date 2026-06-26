from django.views.generic import TemplateView
from django.core.paginator import Paginator
from .models import Post

class MoviesList(TemplateView):
    template_name = "movies/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        posts = Post.objects.all()          # QuerySet
        paginator = Paginator(posts, 3)     # Paginate the QuerySet

        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context["page_obj"] = page_obj
        return context