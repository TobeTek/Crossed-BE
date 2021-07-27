from django.shortcuts import render
from django.views import generic
from .models import Transport , TransportType, Supplies

# Create your views here.

# CRUD Transport
class TransportListView(generic.ListView):
	model = Transport
	fields = '__all__'
	template_name = 'transports/transport_list.html' 

class TransportCreateView(generic.CreateView):
	model = Transport
	fields = '__all__'
	template_name = 'transports/transport_create_form.html'

class TransportDeleteView(generic.edit.DeleteView):
	model = Transport
	template_name = 'transports/transport_delete_form.html'

class TransportEditView(generic.edit.UpdateView):
	model = Transport
	template_name = 'transports/transport_edit_form.html'
	fields = '__all__'

# CRUD TransportType
class TransportTypeListView(generic.ListView):
	model = TransportType
	fields = '__all__'
	template_name = 'transports/transport_type_list.html' 

class TransportTypeCreateView(generic.CreateView):
	model = TransportType
	fields = '__all__'
	template_name = 'transports/transport_type_create_form.html'

class TransportTypeDeleteView(generic.edit.DeleteView):
	model = TransportType
	template_name = 'transports/transport_type_delete_form.html'

class TransportTypeEditView(generic.edit.UpdateView):
	model = TransportType
	template_name = 'transports/transport_type_edit_form.html'
	fields = '__all__'

# CRUD Supplies
class SuppliesListView(generic.ListView):
	model = Supplies
	fields = '__all__'
	template_name = 'transports/supplies_list.html' 

class SuppliesCreateView(generic.CreateView):
	model = Supplies
	fields = '__all__'
	template_name = 'transports/supplies_create_form.html'

class SuppliesDeleteView(generic.edit.DeleteView):
	model = Supplies
	template_name = 'transports/supplies_delete_form.html'

class SuppliesEditView(generic.edit.UpdateView):
	model = Supplies
	template_name = 'transports/supplies_edit_form.html'
	fields = '__all__'
