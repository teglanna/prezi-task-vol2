from django.views import generic

from prezi.models import Prezi


class PreziListView(generic.ListView):
    template_name = 'prezi/prezi_list.html'
    model = Prezi

    def get_queryset(self):
        self.query = self.request.GET.get('q')
        if self.query:
            qs = Prezi.objects.filter(title__icontains=self.query)
        else:
            qs = super(PreziListView, self).get_queryset()
        return qs


    def get_context_data(self, **kwargs):
        context = super(PreziListView, self).get_context_data(**kwargs)
        context['prezis'] = context['object_list'].order_by('created_on')
        context['q'] = self.query
        return context

prezi_list = PreziListView.as_view()
