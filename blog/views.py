from datetime import date
from django.shortcuts import render

# Create your views here.
all_posts = [
    {
        'slug':'hike-in-the-mountains',
        'image': 'image_1.png',
        'author': 'Tobi',
        'date': date(2022, 7, 25),
        'title' :'Mountain Hiking',
        'excerpt' : 'There\'s nothing like the views you get when hiking in the mountains! And I wasn\'t even prepared for what happened whilst I was enjoying mountains',
        'content' : ' Lorem ipsum dolor, sit amet consectetur adipisicing elit. Accusamus molestiae aut numquam architecto saepe maxime ea! Deserunt illo illum ut commodi, vel amet adipisci exercitationem laboriosam, excepturi sunt dignissimos eveniet!',
    },
     {
        'slug':'programming-is-fun',
        'image': 'image_2.png',
        'author': 'Tobi',
        'date': date(2022, 7, 1),
        'title' :'Programming Is Great!',
        'excerpt' : 'Did you ever spend hours searching that one error in the code?',
        'content' : ' Lorem ipsum dolor, sit amet consectetur adipisicing elit. Accusamus molestiae aut numquam architecto saepe maxime ea! Deserunt illo illum ut commodi, vel amet adipisci exercitationem laboriosam, excepturi sunt dignissimos eveniet!',
    },
     {
        'slug':'into-the-woods',
        'image': 'image_3.png',
        'author': 'Tobi',
        'date': date(2022, 7, 3),
        'title' :'Nature At Its Best',
        'excerpt' : 'Nature os amazing! The amount if inspiration i get when walking',
        'content' : ' Lorem ipsum dolor, sit amet consectetur adipisicing elit. Accusamus molestiae aut numquam architecto saepe maxime ea! Deserunt illo illum ut commodi, vel amet adipisci exercitationem laboriosam, excepturi sunt dignissimos eveniet!',
    },
]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', 
    {
        'posts': latest_posts
    }
    )

def posts(request): 
    return render(request, 'blog/all-posts.html',
    {
        'all_posts' : all_posts
    }
    )

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug )
    return render(request, 'blog/post-detail.html',
    {
        'post': identified_post
    }
    )
