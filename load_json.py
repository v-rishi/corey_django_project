"""
To be written in the shell - python manage.py shell
"""
import json
from blog.models import Post
with open('post.json') as f:
    posts_json=json.load(f)

for post in posts_json:
    post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
    post.save()

