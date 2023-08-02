from flask import (
    Flask,
    flash,
    get_flashed_messages,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
)
import os

from crud_project_ls18.repository import PostsRepository
from crud_project_ls18.validator import validate

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


# Главная страница
@app.route('/')
def index():
    return render_template('index.html')


# Список постов
@app.get('/posts')
def posts_get():
    repo = PostsRepository()
    messages = get_flashed_messages(with_categories=True)
    posts = repo.content()
    return render_template(
        'posts/index.html',
        posts=posts,
        messages=messages,
        )


@app.route('/posts/new')
def new_post():
    post = {}
    errors = {}
    return render_template(
        'posts/new.html',
        post=post,
        errors=errors,
    )


@app.post('/posts')
def posts_post():
    repo = PostsRepository()
    data = request.form.to_dict()
    errors = validate(data)
    if errors:
        return render_template(
            'posts/new.html',
            post=data,
            errors=errors,
            ), 422
    id = repo.save(data)
    flash('Post has been created', 'success')
    resp = make_response(redirect(url_for('posts_get')))
    resp.headers['X-ID'] = id
    return resp


# BEGIN (write your solution here)
@app.route('/posts/<id>/update')
def edit_post(id):
    repo = PostsRepository()
    post = repo.find(id)
    errors = []

    return render_template(
           'posts/edit.html',
           post=post,
           errors=errors,
    )


@app.route('/posts/<id>/update', methods=['POST'])
def patch_post(id):
    repo = PostsRepository()
    post = repo.find(id)
    print(post)
    data = request.form.to_dict()
    print(data)

    errors = validate(data)
    print(errors)
    if errors:
        return render_template(
            'posts/edit.html',
            post=post,
            errors=errors,
        ), 422

    # Ручное копирование данных из формы в нашу сущность
    post['title'] = data['title']
    post['body'] = data['body']
    repo.save(post)
    flash('Post has been updated', 'success')
    return redirect(url_for('posts_get'))
# END
