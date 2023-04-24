from functions import get_yaml, get_md_html, insert_html, read_posts


posts_directory = '/Users/yvesbraeckman/SSG/posts'
template_directory = "/Users/yvesbraeckman/SSG/templates"
insert_html(get_md_html(read_posts(posts_directory)[0]), get_yaml(read_posts(posts_directory)[0]))




