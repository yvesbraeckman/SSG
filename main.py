from functions import get_yaml, get_md_html, insert_html, read_posts


posts_directory = '/Users/yvesbraeckman/SSG/posts'
template_directory = "templates/template_1.html"


def build_website():
    posts = read_posts(posts_directory)
    i = 0
    for post in posts:
        insert_html(get_md_html(post), get_yaml(post), i,)
        i += 1


build_website()
