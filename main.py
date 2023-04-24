from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
import os
import yaml


def read_posts():
    posts = []
    for filename in os.listdir('/Users/yvesbraeckman/SSG/posts'):
        with open(os.path.join('/Users/yvesbraeckman/SSG/posts', filename), 'r') as f:
            article = markdown(f.read())
            posts.append(article)
    return posts


def md_to_html(post):
    template_env = Environment(loader=FileSystemLoader(searchpath='./'))
    template = template_env.get_template('layout.html')
    with open('index.html', 'w') as output_file:
        output_file.write(
            template.render(
                article=post
            )
        )


def parse_meta_data(post):
    fm_yaml = post[post.find("---")+3: post.rfind("---")]
    md = post[post.rfind("---")+3:]
    fm_dict = yaml.load(fm_yaml, Loader=yaml.FullLoader)
    print(fm_dict)
    print(md)


# parse_meta_data(read_posts()[0])

print(read_posts())
