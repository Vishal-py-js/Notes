#Please follow below steps to run this project locally

Step 1: run **git clone https://github.com/Vishal-py-js/Notes.git** to copy the project

Step 2: run **pip install -r requirements.txt** to download packages required in this project.

Step 3: first **run py manage.py makemigrations** and then run **py manage.py migrate** to setup database tables.

Step 4: run **py manage.py runserver** to start server locally.


Endpoints:

1- User Registration[POST]:
    BASE_URL/api/signup/

    body:{
        "username": user,
        "password": password,
        "password2": password
    }


2- User Login[POST]:
    BASE_URL/api/login/

    body:{
        "username": user,
        "password": password
    }
    this request will return a token that will be used to make requests to other APIs


3- Create a new note[POST]:
    BASE_URL/api/notes/create/

    body:{
        "title": title1,
        "description": description1,
        "status": True
    }
    headers:{
        Authorization: Token [your token received from login api]
    }

    note: status is there just keep track of the recorded note, whether it is complete or not


4- Get a note[GET]:
    BASE_URL/api/notes/id/

    headers:{
        Authorization: Token [your token received from login api]
    }


5- Share a note[POST]:
    BASE_URL/api/notes/share/

    body:{
        "user_id": 1,
        "note_id": 2,
    }   

    note: user_id is id of the user the note is being shared to


6- Update a note[PUT]:
    BASE_URL/api/notes/id/

    body:{
        "title": title1,
        "description": description1,
        "status": True
    }
    headers:{
        Authorization: Token [your token received from login api]
    }


7- Get all the changes made to a note[GET]:
    BASE_URL/api/notes/version-history/note_id/

    headers:{
        Authorization: Token [your token received from login api]
    }