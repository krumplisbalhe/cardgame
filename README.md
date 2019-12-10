# cardgame

###### Django exam project - A simple cardgame, to start deep conversations and strengthen connections between friends, family or couples.

## Folder structure

```
cardgame_project
│   manage.py
│   requirements.txt
│   tasks.py
│
└───accounts
│
│ 
└───cardgame_project
|
|
└───playcards
   
```

The main folder is the highest `cardgame_project`.  
The project folder is the `cardgame_project` on the second level.  
The app taking care of the users and authentication is in the `accounts` folder.  
The app handling the files related to the game is called `playcards`.  

## Environment

amqp==2.5.2   
billiard==3.6.1.0  
blinker==1.4  
Django==2.2.7  
importlib-metadata==1.0.0  
kombu==4.6.6  
Kuyruk==9.2.2  
more-itertools==8.0.0  
pytz==2019.3  
sqlparse==0.3.0  
uWSGI==2.0.18  
vine==1.3.0  
zipp==0.6.0  

(Note to self: The environment for this project is located: Semester2/django/environments/cardgame )  

To activate the environment: `source cardgame/bin/activate`

## To run the app

After activating the environment, stand in the higher cardgame_project folder and `./manage.py runserver`

## REST API

Located at the end of the playcards/views.py file.

## Middleware

I used `login_required`

## Signals

In playcards/models.py, I used the `post_delete` signal, which prints on the console every time a card has been deleted.


## Task Queue

First, I installed Kuyruk.

https://kuyruk.readthedocs.io/en/latest/gettingstarted.html

The task is being declared in the tasks.py file, on the highest level, in the highest cardgame_project folder.

Then, I installed RabbitMQ

https://www.rabbitmq.com/install-homebrew.html

Open 3 terminal windows, make sure all of them has the correct environment activated! (source xy/bin/activate)

And started it in one terminal window with the command : `rabbitmq-server`

(You might have to do the appending before: export PATH=$PATH:/usr/local/opt/rabbitmq/sbin)

Then, in an other terminal window: `kuyruk --app tasks.kuyruk worker`

Then, in a third window, I started the server: `./manage.py runserver`

After adding a card, in the second window, we can see the worker processing our task and printing on the console.


## Notes

https://www.youtube.com/watch?v=Y4c4ickks2A
