class BlogPost:
    def __init__(self,title,content):
        self.title=title
        self.content=content
class Post:
    def __init__(self):
        self.posts=[]

    def create_post(self,title,content):
        post=BlogPost(title,content)
        self.posts.append(post)

    def display_posts(self):
        for post in self.posts:
            print("Title: ",post.title)
            print("Content: ",post.content)
            print("")

my_blog=BlogPost()
my_blog.create_post
