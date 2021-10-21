from app import app, db
from app.models import User


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}


def some_other_function():
    pass


if __name__ == "__main__":
    app.run(debug=True)
