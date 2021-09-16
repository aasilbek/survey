# Survey project 

## Task

Design and develop an API for a user polling system.

## Functionality for the system administrator

- authorization in the system (registration is not required)
- add / change / polls. Poll attributes: title, start date, end date, description. After creation, the field "start date" for the survey cannot be changed
- adding / changing / questions in the survey. Question attributes: question text, question type (answer text, single choice answer, multiple choice answer)

## Functionality for system users

- getting a list of active polls
- taking a survey: surveys can be completed anonymously, a numeric ID is passed to the API as a user identifier, by which the user's answers to questions are stored; one user can participate in any number of surveys
- getting the polls completed by the user with details on the answers (what is selected) by the unique user ID


## Outline
- Prerequisites
- Setup
    - Development
- Documentation


## Prerequisites
This project has the following prerequisites
- python 3.8.5
- docker 19.03.12
- docker-compose 1.25.0


## Setup

### Development

- Install virtual environment:
```
git clone https://github.com/aasilbek/survey.git
cd clyqe-backend
python3.8 -m venv --prompt="v" .env
```

- Load *local environment variables* to virtual environment:
```
cp ./deployments/development/env_example ./deployments/development/.env
change .env_local variable according to your settings
source ./deployments/development/.env
```

- If *pre commit* has not been installed please install by running following command:
```
pip install pre-commit
pre-commit install
```

- If *postgresql database* has not be started please start it by following command:
```
docker-compose -f deployments/development/docker-compose.yml up -d
```

- If *development packages* has not been installed please install by running following commit:
```
pip install -r requirements/development.txt
```

- If *migration* has not been applied please apply it first:
```
cd src
python manage.py migrate
```

- Start development server:
```
python runserver 0.0.0.0:8080
```

- Run tests:
```
pytest -v
```
