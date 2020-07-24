from django.views.generic import TemplateView

from meilleur_corpo.apps.estate_adverts.forms import EstateAdvertsSearchForm

class HomeView(TemplateView):

    def get_context_data(self, form, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = form
        return context

    def get(self, *args, **kwargs):
        form = EstateAdvertsSearchForm()

        context = self.get_context_data(form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            pass

        return self.render_to_response(context)
