# Installation

## Local installation
```
virutalenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Heroku deploy
```
heroku login
heroku container:login
heroku create
heroku container:push web
heroku container:release web
```

# Running

## Local run
`python app.py`

## Docker container
`docker-compose up`

# Usage

## Local run or in docker container
http://localhost:8080/

## Heroku
Click "Open app" after following your the link to your app from here: https://dashboard.heroku.com/apps