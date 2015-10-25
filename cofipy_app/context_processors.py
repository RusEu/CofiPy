from .forms import IdeaForm

def ideea(request):
	ideaform = IdeaForm()
	return {"ideaform":ideaform}