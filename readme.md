# CBPen
Cloud Blazers Penetration Testing Tool 

![App demo](screenshots/index.png)

## Local Setup
### Requirements
- Python 3
- Pip
- nmap
- Internet connection

### Install dependencies
- Clone the repository.
- Open a terminal in the cloned repository.
- Create a virtual environment and activate it.
If you are using Linux / Mac:
```commandline
python3 -m venv venv
source venv/bin/activate
```
If you are using Windows (Untested):
```commandline
py -3 -m venv venv
venv\Scripts\activate.bat
```
- Install required packages:
```commandline
pip install -r requirements.txt
```

### Run the project
- To run the project call `flask run` command. It will invoke the environment variables which are set in [.flaskenv](./.flaskenv) file:
```commandline
flask run
```


## Cloud Setup
### Requirements 
- Docker
- Docker compose

### Run the project
- Run the project using the following command:
```commandline
docker-compose build --no-cache
docker-compose up --force-recreate
```
- Access the web application from: [http://localhost:5000/](http://localhost:5000/)
- Down the project:
```commandline
docker-compose down
```

### Clean docker
- Check the running images:
```commandline
docker ps -a
```
- Remove any stopped containers and all unused images:
```commandline
docker system prune -a
```

### Reference
- [Docker compose tutorial](https://docs.docker.com/compose/gettingstarted/)
- [How To Remove Docker Images, Containers, and Volumes](https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes)
- [Writing a Basic Port Scanner in Python](https://westoahu.hawaii.edu/cyber/forensics-weekly-executive-summmaries/writing-a-basic-port-scanner-in-python/)
- [Icons class in template](https://demo-basic.adminkit.io/icons-feather.html)
- [Virtual environments for Flask app](https://flask.palletsprojects.com/en/2.0.x/installation/#virtual-environments)
- [Python3 nmap package](https://pypi.org/project/python3-nmap/)