class BlogPost:
    def __init__(self,title,content):
        self.title=title
        self.content=content
class Blog:
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

my_blog=Blog()
my_blog.create_post("Post 1", 'Actus hominis, non dignitas iudicetur')
my_blog.create_post("Post 2", "Ad perpetuam rei memoriam")

my_blog.display_posts()