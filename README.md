# Harpia_API
Microservice to register and list Users on the Database

resource = https://github.com/shipay-pag/backend-challenge

<hr>

<p align="center">
  <a href="#projeto">About the project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#tecnologias">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#instalacao">How to install</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#execução">How to execute it</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#response">Response</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#deploy">Deploy with Docker</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

## <a id="projeto"> 💻 ABOUT THE PROJECT </a>

This API can register an user with name, email, role, and password (not required, it will generate a password in case you don't put it).
It also list all the users inside the database.

<br>

🟩 PROJECT STATUS: <b>IN PROGRESS</b> <br>

<hr>

## <a id="tecnologias"> 🧪 TECHNOLOGIES </a>

- Python
- FLASK
- Postgres with SqlAlchemy
- API Consumer
- Pytest (to be implemented)
- Mutation Tests (to be implemented)

<hr>

## <a id="instalacao"> HOW TO INSTALL IT </a> 

<b>- Download it or clone the repo.

<hr> 

#### On Windows

<b>- Create your virtual environment:</b> `python -m venv venv`<br>
<b>- Activate your virtual environment: </b>`. venv\Scripts\Activate.ps1`<br>
<b>Obs: If for any reason occurs and error:</b> on powershell execute the following command: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`<br>
<b>- Execute requirements with the command: </b>`pip install -r requirements.txt`<br>

<hr> 

#### On Linux:

<b>- Create your virtual environment:</b> `python -m venv venv`<br>
<b>- Activate your virtual environment:</b> `source venv/bin/activate`<br>
<b>- Execute requirements with the command:</b> `pip install -r requirements.txt`<br>

<hr>

Create a project root `.env` file and change your local strings connections to do the proper connection <br>

```commandline
HOST_POSTGRES=''
PORT_POSTGRES=''
DATABASE_POSTGRES=''
USER_POSTGRES=''
PASSWORD_POSTGRES=''
```

<hr>

## <a id="execução"> EXECUTE UVICORN </a> 

- To Execute the application run the command: `uvicorn main:app --reload` or manually run the `main.py` file. It will
expose the localhost:8000.

<hr>

## <a> REQUISITION ROUTER </a> 

- Use the routers on your Postman/Insomnia:

`http:{HOST_AND_PORT}/get_list_of_users` ; <br>
`http:{HOST_AND_PORT}/post/register_user` ; <br>

## <a> QUERY PARAMS </a> 

To register an user you need to put the following body on your Insomnia/Postman/etc. It is not needed to put a password.

```commandline
{
    "name": "Ricardo Lucindo",
    "email": "ricardo@outlook.com",
    "role": "Silver",
    "password": "1234556"
}
```

<hr>

## <a id="response"> API RESPONSES: </a> 

- Expected return of the route `/get_list_of_users` when right passing body:
```
{
    "result": [
        {
            "Name": "Lala Maciel",
            "Email": "lala@gmail.com",
            "User Role": "Gold",
            "Claim": "Create"
        },
        {
            "Name": "Adolfo Vigario",
            "Email": "adolfo@outlook.com",
            "User Role": "Silver",
            "Claim": "Read"
        }
    ],
    "message": "SUCCESS",
    "success": true,
    "internal_code": 200
}
```

- Expected return of the route `/post/register_user` when passing right body:

```
{
    "result": {
        "DATABASE": "Data Inserted on System"
    },
    "message": "OK",
    "success": true,
    "internal_code": 200
}

```

## <a id="response"> API ERRORS: </a> 

Examples of expected response of the route when an error happened:

- When passing wrong params:

```
{
    "result": null,
    "message": "THE BODY PARAMS ARE NOT FITTING THE API REQUIREMENTS",
    "success": false,
    "internal_code": 99
}

```

## <a id="deploy"> DEPLOY WITH DOCKER: </a>

To deploy with docker run the following command on you local:

- docker build -t flask-api .
- docker run -d -p 8000:8000 --name my-flask-api flask-api

Make sure you have docker dependencies installed.

