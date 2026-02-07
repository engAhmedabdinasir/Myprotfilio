from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Skill, Service, Project, BlogPost, ContactMessage
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.conf import settings

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'portfolio/login.html', {'form': form})


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all().order_by('-id')[:3]  # Show top 3 latest projects on home
    blog_posts = BlogPost.objects.all().order_by('-created_at')[:3]
    return render(request, 'portfolio/home.html', {
        'profile': profile,
        'skills': skills,
        'services': services,
        'projects': projects,
        'blog_posts': blog_posts,
    })

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'portfolio/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'portfolio/blog_detail.html', {'post': post})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Email to YOU (Admin)
        admin_message = f"""
New Contact Message:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
        """

        try:
            # Send to Admin
            send_mail(
                subject=f"New Contact Message: {subject}",
                message=admin_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['ashkayare878@gmail.com'],
                fail_silently=False,
            )

            # Auto-reply to USER
            user_reply = f"""
Hi {name},

Thank you for contacting me!
I have received your message and will get back to you as soon as possible.

Best regards,
Ahmed Abdinasir
            """

            send_mail(
                subject="Message Received Successfully",
                message=user_reply,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=True,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
             # Fallback if email fails (e.g. invalid config), but still show success for the DB save
             print(f"Email sending failed: {e}")
             messages.success(request, 'Your message has been saved! (Email notification failed)')
             
        return redirect('contact')
    return render(request, 'portfolio/contact.html')
