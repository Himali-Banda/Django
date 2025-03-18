 class SignUp(CreateView):
    froms_class = CustomerUserCreationFrom
	success_url = reverse_lazy('login')
	template_name = 'register.html'