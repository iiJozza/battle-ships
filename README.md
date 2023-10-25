# Battleship Game Readme
    Welcome to a thrilling game of Battleship with a twist! In this version,
    the playing field features only 1x1 ships, creating an intense and
    strategic challenge.

## How to Play
Battleship is a classic two-player strategy game where the goal is to sink all of your opponent's ships before they sink yours. The game is typically played on a grid, and each player has a set number of ships to place on their grid. In this itteration you play against a computer with an army of 1x1 ships.

### Setup: 
The grids are usually square and can vary in size, but a common grid size is 9x9. In this implementation, you can choose both the size of the grid, up to 9x9 and the amount of ships. The ship are randomly distributed around the grid.

### Scoring:
The game uses a hit/miss system for scoring. Each turn the player guesses a coordiante on where they think a ship might be, hoping to hit the opposing players ship. The player and computer alternate taking turns until someone sinks all of the others ship(s)."

### Winning the Game
The game continues until one player has sunk all of their opponent's ships. In the traditional game, a ship is considered "sunk" when every part of the ship has been hit. 

## Running the Game
To play this Battleship game implementation, follow these steps:

### Start the Game
Run the Python script provided for this game. You can specify the grid size (e.g., 9x9) and the number of ships you want to play with.

## Features

## Deployment

The site was deployed via [Heroku](https://id.heroku.com/login).
This project was developed utilizing the [Code Institute Template](https://github.com/Code-Institute-Org/p3-template).

`pip freeze > requirements.txt` was used to add pyfiglet and Colorama imports to Heroku for deployment.

## Deploying a Python Web Application to Heroku

This guide will walk you through deploying a Python web application to Heroku using the Heroku Dashboard. It doesn't require a command-line interface (CLI). Make sure you have a Heroku account and Git installed on your local machine.

#### Step 1: Prerequisites

- Create a Heroku account at [Heroku's website](https://www.heroku.com/).
- Ensure you have Git installed on your local machine.

#### Step 2: Prepare Your Python Application

- Ensure your Python application is properly set up.
- Create a `requirements.txt` file listing your project's dependencies.
- Include a `Procfile` that tells Heroku how to run your application.

#### Step 3: Deploy Your Application

- Initialize a Git repository for your project if it's not already one:

   ```sh
   git init
   git add .
   git commit -m "Initial commit"

- Install the Heroku CLI if you prefer a command-line interface.
   
#### Step 4: Create and Deploy on Heroku

1. Log in to your Heroku account through the Heroku website.

2. Click the "New" button in the Heroku dashboard and select "Create New App."

3. Give your app a unique name. This name will be a part of your app's URL, so choose wisely. You can also choose a region that's geographically closer to your target audience for better performance.

4. In the "Deploy" tab of your app's dashboard, you have options to connect your GitHub repository or deploy using a Git repository. Choose the one that suits your project. If you're connecting a Git repository, make sure your project is already hosted on Git.

5. If you're using a Git repository, you can enable automatic deploys. This means your app will be automatically redeployed every time you push changes to your Git repository. This is a convenient option for continuous deployment.

6. Finally, deploy your app by clicking the "Deploy Branch" button. Heroku will start building your application. You can see the build progress in the activity tab. Once the build is complete, your application is live.

#### Step 5: Open Your App

1. After your deployment is successful, you can open your app by clicking the "Open App" button in your Heroku dashboard.

2. Heroku will open your application in a new tab. You can also access it directly via the URL provided (e.g., `https://your-app-name.herokuapp.com`).

### Deployment to Github Pages

- The site was deployed to GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository, navigate to the Settings tab
  - From the menu on left select 'Pages'
  - From the source section drop-down menu, select the Branch: main
  - Click 'Save'
  - A live link will be displayed in a green banner when published successfully.

#### Clone the Repository Code Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

## Acknowledgements

- I would like to thank Carolina Leguizamon for helping me kickstart the project, giving me ideas and general encouragement throughout the project. Was a huge help keeping me level-headed and continue coding when times were tough.


