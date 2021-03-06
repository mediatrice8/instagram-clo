from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . forms import ProfileUploadForm,CommentForm,ProfileForm,ImageForm
from django.http  import HttpResponse
from . models import Image,Profile, Likes, Follow, Comment,Unfollow
from django.conf import settings


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
      title = 'Instagram'
      image_posts = Image.objects.all()
      # comments = Comment.objects.all()

      print(image_posts)
      return render(request, 'welcome.html', {"title":title,"image_posts":image_posts})


@login_required(login_url='/accounts/login/')
def comment(request,id):
	
	image = get_object_or_404(Image,id=id)	
	current_user = request.user
	print(image)

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = current_user
			comment.image = image
			comment.save()
			return redirect('welcome')
	else:
		form = CommentForm()

	return render(request,'comment.html',{"form":form})  


@login_required(login_url='/accounts/login/')
def profile(request):
	 current_user = request.user
	 profile = Profile.objects.all()
	 follower = Follow.objects.filter(user = profile)

	 return render(request, 'profile.html',{"current_user":current_user,"profile":profile,"follower":follower})

@login_required(login_url='/accounts/login/')
def timeline(request):
	current_user = request.user 
	Myprofile = Profile.objects.order_by('-time_uploaded')
	comment = Comment.objects.order_by('-time_comment')
	

	return render(request, 'my_account/timeline.html',{"Myprofile":Myprofile,"comment":comment})

# @login_required(login_url='/accounts/login/')
# def single_image(request,image_id):
# 	image = Image.objects.get(id= image_id)

# 	return render(request, 'my_account/single_image.html',{"image":image})

@login_required(login_url='/accounts/login/')
def like(request,image_id):
	image = Image.objects.get(id=image_id)
	like +=1
	save_like()
	return redirect('timeline')

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_profiles = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search_image.html',{"message":message,"images": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search_image.html',{"message":message})


@login_required(login_url='/accounts/login/')
def upload_profile(request):
    current_user = request.user 
    title = 'Upload Profile'
    try:
        requested_profile = Profile.objects.get(user_id = current_user)
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                # # requested_profile.profile_picture = form.cleaned_data['profile_picture']
                # requested_profile.bio = form.cleaned_data['bio']
                # requested_profile.name = form.cleaned_data['name']
                # requested_profile.save_profile()
                return redirect( profile )
        # else:
        #     form = ProfileUploadForm()
    except:
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                # new_profile = Profile(profile_picture = form.cleaned_data['profile_picture'],bio = form.cleaned_data['bio'],name = form.cleaned_data['name'])
                # new_profile.save()
                return redirect('profile')
        else:
            form = ProfileUploadForm()


    return render(request,'upload_profile.html',{"title":title,"form":form})


@login_required(login_url='/accounts/login/')
def displays(request):
    '''
    View function that displays a forms that allows users to upload images
    '''
    current_user = request.user

    if request.method == 'POST':

        form = ImageForm(request.POST ,request.FILES)

        if form.is_valid():
            image = form.save(commit = False)
            image.user_key = current_user
            image.likes +=1
            image.save() 

            return redirect( 'timeline')
    else:
        form = ImageForm() 
    return render(request, 'my_account/send.html',{"form" : form}) 

