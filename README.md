# Nashville SkillShare Hub

This mobile-first application allows users to search for skill-sharing events in the Nashville area. Users can search by cost and date, bookmark events, and have full CRUD of events.

## Motivation 

As someone who believes in mutual aid as a better way to strengthen communities, I have wanted to see and use this application for years. Usually I have to search through social media accounts and sign up for email lists to find different workshops and skill-sharing events, then I have to track down where I saw them to get more details. It's a hassle. This application allows users to post their events and to bookmark events so they can easily manage different workshops and classes they would like to attend or that they are hosting. 

## Tech Stack

*Built With:*

- ReactJS
- Python
- Django
- SQL

## Features

- The user can log in and log out.
- They can create skill-sharing events they are hosting.
- They can edit and delete their own events.
- They can search all of the events by date and cost.
- They can bookmark and unbookmark events they are interested in.
- They can view the events they are hosting.
- They can view the events they have bookmarked.


## Application Demo

![gif of demo](images/Video_nashvilleskillshare.gif)


## Moqup/Wireframe

![wireframe/moqup](images/wireframe.png)


## ERD

![erd](images/erd.png)


## Dependency Chart 

![dependency chart](images/dependencychart1.png)

![dependency chart](images/dependencychart2.png)


## Installation

### Front End:
```
git clone git@github.com:kylieanyce/nashville-skillshare-hub-client.git
npm install
npm start
npm install moment --save 
```
### Back End:
```
git clone git@github.com:kylieanyce/nashville-skillshare-hub-server.git
pip3 install --user pipx
pipx install pipenv
pipenv install django autopep8 pylint djangorestframework django-cors-headers pylint-django
python3 manage.py migrate
```

## How To Use

Clone the front and back ends down and do all the installations. Register as a new user and you can use the app as you please. 

After logging in, the user comes to the home page which lists all upcoming events. They can click on the title to get more information about the event from the details page. There they can choose to bookmark an event they are interested in. From the home page, the user can create an event and save it. They can navigate to the *__'My Events'__* view and see the events they have created. They can also navigate to the *__'Bookmarks'__* view and see the events they have bookmarked. 

The user can search events by to parameters: *cost* and *date*. By entering a number or a word into the *cost* search affordance, events will be searched accordingly. By choosing a date from the drop down calendar in the *date* affordance, events will be search for that specific date.


## Credits

I could not have done this without the amazing leadership and support of Nashville Software School, as well as my incredible teammates in Cohort 46!


## Authentication

The authentication in this project was given to us by our instruction team and is completely false.
