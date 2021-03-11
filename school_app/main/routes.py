from flask import render_template, request, Blueprint
from school_app.models import Post
from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/blog')
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('blog.html', title='Blog', posts=posts)