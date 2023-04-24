from functions import get_yaml, get_md_html, insert_html, read_posts


posts_directory = '/Users/yvesbraeckman/SSG/posts'
post_temlpate = "templates/template_1.html"
about_template = "templates/template_2.html"


def build_website():
    posts = read_posts(posts_directory)
    i = 0
    j = 0
    for post in posts:
        print(post)
        if post == "/Users/yvesbraeckman/SSG/posts/about.md":
            j = i
            i = "about"
            insert_html(get_md_html(post), get_yaml(post), i, about_template)
            i = j
        else:
            insert_html(get_md_html(post), get_yaml(post), i, post_temlpate)
            i += 1


build_website()
