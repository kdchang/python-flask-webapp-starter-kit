from flask import (
        render_template,
        current_app,
        Blueprint,
        redirect,
        url_for,
        request,
        flash,
        session
)

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates/main'
)

@main_blueprint.route('/')
def index():
    title = 'This is title'
    return render_template('main/index.html', title=title)
