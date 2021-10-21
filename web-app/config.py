import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config(object):
	TESTING = True
	SECRET_KEY=os.environ.get('SECRET_KEY') or 'Hard coded string'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'app.db')
	# SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:rootpassword@localhost:3306/salubreata"
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')


#Mock comment to test commit from web ide


