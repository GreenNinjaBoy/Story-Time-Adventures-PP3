# Story Time Adventures

**Story Time Adventures is a text based story game where the story changes depending on the user's choices.**

**The link to the game can be found here**

*Insert responsive Image here!!

## Content:

 - **Wireframes and Goals**
	 - Lucid Chart
	 - Project Goals and Target Audience
 - Design and UX
	 - Design and Features
	 - Color Scheme
	 - User Experience
		 - User Stories
			 - First Time Player
			 - Returning Player
		- Game Graphics
	- Typography
	- Imagery
 -   ### Technologies Used
    
	 - Frameworks, Packages & Programs Used 

### Testing
    
   -  [PEP8]   
    - [W3 HTML Checker]    
    - [CSS Checker]   
    - [Contrast Checker] 
    - [Lighthouse  
    - Bug testing    
    - [Responsiveness]    
    - [Fixed bugs]
    
 ### Deployment
  - Generating template from github
  - Setting up Virtual Code Space
	  - Code Anywhere
	  - GitPod  
  - Deploy to Heroku

### Credits    
  -   Code   
   -  Content   
   -  Media
    -  Acknowledgements


## Lucid Chart

### The Lucid chart was generated with the help of [LucidChart](https://www.lucidchart.com/pages/).

**The finish code is different to the initial chart shown.**
	   
![Fluid Image](https://github.com/GreenNinjaBoy/story-time-adventures-PP3/blob/main/assets/readme-images/s-t-a-fluidchart.jpeg?raw=true)

**This is the chart of the final game**

### Insert new image here!!


## Project Goals an Target Audience.

### Goals achieved:

 - Build a fun story based adventure game with different options and outcomes.
 - Be easy and understand to navigate.

### Future Goals:

 - Add more stories and available content to the game.

## Target Audience:

Being a father of a 3 year old daughter I enjoy my nights reading stories to her before she goes to bed. I thought it would be more fun if she was able to help chose which way the story goes instead of what is already printed in a book.

With that I decided have my target audience be parents with children aged 3-10, or just the children if they are able to read who enjoy a good story before bedtime.

## Design and Features

### If CSS/HTML used insert here!

## Color Scheme

 - Imported termcolor to change the colors in the terminal. Colors that are available form term color are shown below:

### Insert Image here


## User Experience (UX)

**First-Time Visitor**

 - As a first time user, I want to understand the website's purpose clearly.
 - That the main point of the site introduces the game well.
 - Let the visitor start the game when they are ready.
 - That the game has different outcomes and is fun and captivating.

**Returning Visitor**

 - Play the game again choose another path, try different inputs.
 - See if new content has been added to the game.

### Game Graphics

*Insert game graphics here when figured out the code

### Typography

 - Standard terminal output with termcolor to color the text

# Testing

 ### PEP8
 - Pylint was used in Codeanywhere/Gitpod. This was done by doing by entering "pip install pep8" in the console. There were several errors showing when initial work was done on the stories for the game. This was mainly due to text lines being too long. These lines have been corrected which has fixed the presented errors.
### Lighthouse
 - Desktop

*Insert Desktop image here.

## Bug Testing

Extensive testing was carried out by myself; a chart of these tests are available for viewing  on the Google SHEET.

 - This includes input checks by user.
 - The story progresses correctly depending on user input.
 - Ensure the overall story ending prints.

## Fixed Bugs

- One issue that was presented was that the text from the .txt file were not printing to the terminal.
	- This was amended by carefully reading through my game_logic.py code and there was if statements missing from my tick function. Once the corrections were done the desired text was printing to the terminal along with the correct choices.  

# Deployment

**Creating The Repository**

The repository was created using Github. as a student this was done using a template provided by Code Institute.
To do this the following steps were taken:

 - On the browser head over to the [Code Institute Template](https://github.com/Code-Institute-Org/p3-template).
 - Click on the green "Use this template button".
 - Click on "create a new repository".
 - The user will be taken to a new page to create the repository.
 - In the box titled "repository name" enter an appropriate name (for this project Story-Time-Adventures-PP3 was used).
 - There is an optional description box if you wish to give a bit more detail to your repository.
 - Then Click on the green "create repository" and Github will create the new repository.

**Cloning the Repository** 
 - Github can also be used to clone a repository so that the code can be altered and pushed back to the main repository using a different IDE.
	 - This can be done by using the following steps.
		 1.  In the " Story-Time-Adventures-PP3" repository, select the  green "code" tab.
		 2. Select HTTPS in the dropdown menu.
		 3. Copy the URL under HTTPS.
		 4. Open the IDE that you are working from for example [CodeAnywhere](https://app.codeanywhere.com/).
		 5. Sign in using your Github details.
		 6. Click on the create new workspace button.
		 7.  Paste copied HTTPS and click create (Codeanywhere will now generate the virtual IDE).
		 8.  Once IDE has Loaded create inital index.html page and add test text.
		9.  Once test text is added press  `Ctrl + S`  to save.
		10.  Click terminal tab at top of screen and click new terminal.
		11.  Once new terminal has opened test that content is being pushed back to github.
		12.  In the terminal type  `git add .`  and press enter (this will add all new content).
		13.  Then type  `git commit -m "add test text"`  and press enter (this lets anyone seeing your commits know what you have done).
		14.  Once you have done that type  `git push`  and press enter (this will push all changes made to the github repository).
		15.  Navigate to github.
		16.  Choose the repository you were working on.
		17.  Check the changes have been successfully pushed.



**Forking The Repository**
 - Github can also be used to fork a repository.
	 - This can create a copy of the repository which can be edited without effecting the main repository branch.
	 - The steps to fork the repository can be done as follows:
		 - When in the " Story-Time-Adventures-PP3" repository click on the "Fork" tab located at the top right hand corner.
		 - Click on "create a new fork"
		 - You will be sent to another page to name your forked repository.
		 - Once Named click create fork and you will have a copy of the repository that you can now access and change without affecting the original main repository.

![Fork Image 1](https://github.com/GreenNinjaBoy/Star-Wars-Trivia-PP2/blob/main/assets/readme-images/fork-image-1.png?raw=true)

![Fork Image 2](https://github.com/GreenNinjaBoy/Star-Wars-Trivia-PP2/blob/main/assets/readme-images/fork-image-2.png?raw=true)
*Please note that the images taken were from a friends Github repository who consented to the use of these images for educational purposes.

## **Deploying Using Heroku**
The  Story-Time-Adventures-PP3 repository was deployed using [Heroku.](https://id.heroku.com/login)

The following steps were used:

 - Login or create an account with [Heroku](https://id.heroku.com/login)
 - On the dashboard click on the "Create new app."
 - Write a name for the app being deployed and choose your region and click "Create App".
 - In the settings tab for the new application, create ome Config named PORT and make sure it has the value of 8000
 - Add two build pack scripts, these packs are:
	 - Python
	 - Nodejs
	Ensure that they are listed in this order (if they aren't you can move them freely to ensure they are in this order)
- Connect your Heroku with your GitHub account and select the repository you are working on.

