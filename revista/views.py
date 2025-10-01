from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, TemplateView, FormView, View

from .models import Estudiante, Administrador, Publicacion, Comentario
from .forms import ComentarioForm, LoginEstudianteForm

# Estudiantes
class EstudianteListView(ListView):
    model = Estudiante
    template_name = "revista/estudiantes_list.html"

class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = "revista/estudiante_detail.html"

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = ['nombre', 'direccion', 'carne']
    template_name = "revista/estudiante_form.html"
    success_url = reverse_lazy('estudiantes-list')

# Administradores
class AdministradorListView(ListView):
    model = Administrador
    template_name = "revista/administradores_list.html"
    context_object_name = "administradores"

class AdministradorDetailView(DetailView):
    model = Administrador
    template_name = "revista/administrador_detail.html"

class AdministradorUpdateView(UpdateView):
    model = Administrador
    fields = ["nombre", "direccion", "carne"]
    template_name = "revista/administrador_form.html"
    success_url = reverse_lazy("administradores-list")

# Publicaciones
class PublicacionListView(ListView):
    model = Publicacion
    template_name = "revista/publicaciones_list.html"

class PublicacionDetailView(DetailView):
    model = Publicacion
    template_name = "revista/publicacion_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        context['comentarios'] = Comentario.objects.filter(publicacion=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.publicacion = self.object
            estudiante_id = request.session.get('estudiante_id')
            if estudiante_id:
                comentario.estudiante_id = estudiante_id
                comentario.save()
                return redirect('publicacion-detail', pk=self.object.pk)
            return redirect('login')
        return self.render_to_response(self.get_context_data(form=form))

class PublicacionUpdateView(UpdateView):
    model = Publicacion
    fields = ['titulo', 'contenido', 'autor', 'autorizado_por']
    template_name = "revista/publicacion_form.html"
    success_url = reverse_lazy('publicaciones-list')

# Páginas estáticas
class HomeView(TemplateView):
    template_name = "revista/home.html"

class AcercaView(TemplateView):
    template_name = "revista/acerca.html"

# Login de estudiante
class EstudianteLoginView(FormView):
    template_name = "revista/login.html"
    form_class = LoginEstudianteForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        estudiante, created = Estudiante.objects.get_or_create(
            nombre=form.cleaned_data['nombre'],
            direccion=form.cleaned_data['direccion'],
            carne=form.cleaned_data['carne']
        )
        self.request.session['estudiante_id'] = estudiante.id
        return super().form_valid(form)

# Logout de estudiante
class EstudianteLogoutView(View):
    def get(self, request):
        request.session.pop('estudiante_id', None)
        return redirect('home')
