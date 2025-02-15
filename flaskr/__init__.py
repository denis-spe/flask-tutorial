import os

from flask import Flask

def create_app(test_config=None):
    
    # Create and configure the app.
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    if test_config is None:
        # Load the instance config, it it exists, when not testing.
        app.config.from_pyfile('config.py', silent=True)
    
    else:
        # lLoad the test config if passed in
        app.config.from_mapping(test_config)
        
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)
    
    # A simple page that says hello.
    @app.route("/hello")
    def hello():
        return 'Hello, World!'
    
    # Register the blueprint
    from . import auth
    app.register_blueprint(auth.bp)
    
    return app