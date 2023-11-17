# flask-firebase-hackoss
Basic CRUD Project for Flask and Firebase for HackOSS workshop

# Pre-requisites
   - Python 3.8+ (https://www.python.org/downloads/release/python-3120/) 
   - Visual Studio Code (https://code.visualstudio.com/Download)
   - Firebase Account

# Install virtual env
    - pip install virtualenv ( needs to done with adminstrator rights on terminal)
    
# Set up python virtual environment for project
    set up virtual environment
    - py -3.12 -m venv .venv
    - python -m venv .env/Scripts/activate
    
    install flask / firebase modules
    - pip install flask
    - pip install firebase_admin
    
# Set up firebase api json file
    - login firebase, create new project
    - goto project overview -> project settings -> service accounts -> generate new private key (python)
    - put file into project as firebase-api-key.json

    - goto backend/firebase_service.py -> change databaseURL to 'https://<project-name>.firebaseio.com'

# Run flask project
    - flask --app main run --debug

# Helpful documentations   
   - [Firebase Code Documentation](https://firebase.google.com/docs/firestore/manage-data/add-data)
   - [Flask Code Documentation](https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application)
   - [HTML Template - Jinja Documentation](https://palletsprojects.com/p/jinja/)
