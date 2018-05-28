from django.shortcuts import render
from Blogs.forms import PostAdminForm
# Create your views here.
from Blogs.models import Post
def add_post(request):
	if request.method == "POST":
		form=PostAdminForm(request.POST)
		if form.is_valid():
			post_item = form.save(commit=False)
			post_item.save()
			return redirect('/')
	else:
		form = PostAdminForm()
	return render(request,'Blogs/post_form.html',{'form':form})


def index(request):
	showarticle=Post.objects.all()
	context = {'showarticle':showarticle}
	return render(request,'Blogs/index.html',context)