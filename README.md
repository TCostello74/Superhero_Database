#HERO HQ

Hero HQ is a simple application that allows a user to search through hundreds of heroes and the details about them. After creating an account a user can also compile a list of their favorites.

API: [Link](https://superheroapi.com/?ref=apilist.fun)
Website: [Hero HQ](https://hero-hq.onrender.com/)(Deployed with Render)

##Features

- **Hero Randomizer:** On the home page a user may click a refresh button and 2 random heroes will be displayed, with information about them. I felt this was a fun idea for anyone who just wants to see some of the heroes and give themselves some idea of who they might want to search.
- **Search Hero:** A user may search for a specific hero they might be thinking of and view a page displaying their information with an image. This is a way for users to specifically find who they're looking for.
- **Secure Login:** A user may register and log in and out of their account. 
- **Favorite Hero/Favorite List:** After searching for a hero and creating an account, a user has the ability to favorite a hero and add them to a personlized favorites page. This was a feature I added to provide a more personlized experience.

##Standard User Flow

    First a user will be brought to the home page where they can randomize heros and get a feel for the application. Once they have an idea of who they'd like to search for they can hit search in the nav bar and type in the name of the hero. After being directed to the hero page the user has the option to favorite the hero after creating an account. A user can then repeat this until they have a full personalized list of heros on their favorites page.

##Tech Stack

- **Flask**
- **Python 3.8.12**
- **Bootswatch(styling)**
- **Jinja**
- **WTForms**
- **SQLAlchemy**
