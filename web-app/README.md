## How to setup this project

Prerequisites:

1. Python
2. pip3
3. install virtualenv from pip using 
```bash
pip install virtualenv
```
4. The above command installs utility to create a virtual environment
5. Check on google how to activate venv on windows
6. After venv is activated we can then enter the command 
```bash
pip3 install -r requirements.txt
```


## How to run this project

### Due to limitations in the code we need to create a user explicity from the flask shell

### The following are the commands to add a user via the flask shell into the db but before we can do that we need to delete the migrations folder and app.db from the current repo


## Commands after removing the migrations directory

```bash
flask db init
flask db migrate
flask db upgrade
flask shell
```
### Next command is inside the shell
```python
from app import models,db
user = models.User(username="demo",email="demo")
user.set_password("pass")
db.session.add(user)
db.session.commit()
```


## After the above configurations we can run the project using: 
```bash
flask run
```
