import markdown
import yaml
from jinja2 import Environment, FileSystemLoader
import os

def get_md_html(article):
    with open(article, "r") as f:
        text = f.read()
    md = text[text.rfind("---") + 3:]
    html = markdown.markdown(md)
    return html


def get_yaml(article):
    with open(article, "r") as f:
        text = f.read()
    yml = text[text.find("---")+3: text.rfind("---")]
    yml_data = yaml.safe_load(yml.replace("---", ""))
    return yml_data


def insert_html(html, yml):
    template_env = Environment(loader=FileSystemLoader(searchpath='./'))
    template = template_env.get_template('templates/template_2.html')
    with open('index.html', 'w') as output_file:
        output_file.write(
            template.render(
                article=html,
                author=yml
            )
        )
    return None


def read_posts(posts_directory):
    posts = []
    for filename in os.listdir(posts_directory):
        f = os.path.join(posts_directory, filename)
        if os.path.isfile(f):
            posts.append(f)
    return posts
