from app.views.home import home_view

def register_views(app):
    app.register_blueprint(home_view)
