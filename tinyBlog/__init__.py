from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB' : 'my-tiny-blog'}
app.config["SECRET_KEY"] = "ThisIsS3cr3t"
db = MongoEngine(app)

def register_blueprints(app):
    from tinyBlog.views import posts
    from tinyBlog.admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
