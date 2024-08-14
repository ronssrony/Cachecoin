from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from cachecoin.blockchain import *
from textwrap import dedent
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask import Flask
from flask_mail import Mail

# Instantiate our Node
app = Flask(__name__);

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'rhymerayhan@gmail.com'
app.config['MAIL_PASSWORD'] = 'brta ycjq wrub fupl'
app.config['MAIL_DEFAULT_SENDER'] = 'rhymerayhan@gmail.com'

mail = Mail(app)

app.config['SECRET_KEY'] = 'Moe Lester wants to talk to you for a Titty Attack';
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db';
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;
db = SQLAlchemy(app);
migrate = Migrate(app, db)
bcrypt = Bcrypt(app);
loginManager = LoginManager(app);
loginManager.login_view = 'login';
loginManager.login_message_category = 'info';
# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '');

# Instantiate the Blockchain
blockchainObj = Blockchain();
#print(type(blockchain));

from cachecoin import routes;