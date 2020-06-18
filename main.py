from libraryapp import app

def register_blueprints(app):
    from libraryapp.controllers.posts import posts_controller
    app.register_blueprint(posts_controller)

register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True, port='5000', host='0.0.0.0')