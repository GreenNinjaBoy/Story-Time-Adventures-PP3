

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

### Color Scheme

 - Imported termcolor to change the colors in the terminal. Colors that are available form term color are shown below:

![termcolor options](https://github.com/GreenNinjaBoy/Story-Time-Adventures-PP3/blob/main/assets/readme-images/termcolorpalette.png?raw=true)


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

Pyfiglet was used to design the ASC II text art display for the main game heading, story 1 heading, story 2 heading and "the end" message at the end of the stories.

 - Main game heading
![main game heading](https://github.com/GreenNinjaBoy/Story-Time-Adventures-PP3/blob/main/assets/readme-images/main-game-title.png?raw=true)
 - Story 1 heading 
 
![The Brave Princess](https://github.com/GreenNinjaBoy/Story-Time-Adventures-PP3/blob/main/assets/readme-images/story-1-title.png?raw=true)
 - Story 2 heading
![The Cosmic Space Adventure](https://github.com/GreenNinjaBoy/Story-Time-Adventures-PP3/blob/main/assets/readme-images/story-2-title.png?raw=true)
 - Ending to Story 1
 ![Ending for Story 1](https://github.com/GreenNinjaBoy/Story-Time-Adventures-PP3/blob/main/assets/readme-images/ending-image-2.png?raw=true)
 
 - Ending to Story 2
 - ![Ending for Story 2](https://github.com/GreenNinjaBoy/Story-Time-Adventures-PP3/blob/main/assets/readme-images/endin-1-image.png?raw=true)

 

### Typography

 - Standard terminal output with termcolor to color the text

# Testing

 ### PEP8
 - Pylint was used in Codeanywhere/Gitpod. This was done by doing by entering "pip install pep8" in the console. There were several errors showing when initial work was done on the stories for the game. This was mainly due to text lines being too long. These lines have been corrected which has fixed the presented errors.
 
 ![pep8 test result](https://github.com/GreenNinjaBoy/Story-Time-Adventures-PP3/blob/main/assets/readme-images/pep8-screenshot.png?raw=true)
 
## Bug Testing

Extensive testing was carried out by myself, you can access the test data [here](https://docs.google.com/spreadsheets/d/1vcUQSttZ6TobfRzjVdf8Ig_vR2vrup0FfERo7Dqe_Yo/edit#gid=0).

 - This includes input checks by user.
 - The story progresses correctly depending on user input.
 - Ensure the overall story ending prints.

**Note for future python testing**

 - During the testing stages I came across [Pytest](https://docs.pytest.org/en/7.4.x/). Which allows a developer to write test functions for their code. 
 - To do this type pip install pytest to install the extension.
 - Create test copies of the functions you wish to and place them into a separate .py file with appropriate name. For example for my run.py file for Story-Time-Adventures I would name my test file "test_run.py".
 - Once that is created, the functions that require testing can be inserted and "Test inputs for them can be inserted".
 - When ready to be tested within the terminal the user can type the following "pytest test_run.py" and the terminal will begin to run the tests for the user and returns the results to the user with any faults or errors.

I was unable to implement this during this project, however it will be something I will be looking at in future python projects.  

## Fixed Bugs

- One issue that was present, was that when the user inputted their name, it was not then being imported to the story_index.py file to display the users name within  the desired story.
	- After an exhaustive amount of time and research I was able to implement a function that achieved this outcome.  

- Another problem that was identified was that there was no line breaks between the story text and the choices presented to the user.
	- Again this was resolved by amending the tick() function within my run.py file and tested to ensure it was working correctly.  

# Deployment

**Creating The Repository**

The repository was created using Github. as a student this was done using a template provided by Code Institute.
To do this the following steps were taken:

 - On the browser head over to the [Code Institute Template](https://github.com/Code-Institute-Org/p3-template).
 - Click on the green "Use this template button".
 - Click on "create a new repository".
 ![Create from template](https://github.com/GreenNinjaBoy/Story-Time-Adventures-PP3/blob/main/assets/readme-images/pp3-create-repository-image-1.png?raw=true)
 - The user will be taken to a new page to create the repository.
 - In the box titled "repository name" enter an appropriate name (for this project Story-Time-Adventures-PP3 was used).
 - There is an optional description box if you wish to give a bit more detail to your repository.
 - Then Click on the green "create repository" and Github will create the new repository.
 ![create from template 2](https://github.com/GreenNinjaBoy/Story-Time-Adventures-PP3/blob/main/assets/readme-images/pp3-create-repository-image-2.png?raw=true)

**Cloning the Repository** 
 - Github can also be used to clone a repository so that the code can be altered and pushed back to the main repository using a different IDE.
	 - This can be done by using the following steps.
		 1.  In the " Story-Time-Adventures-PP3" repository, select the  green "code" tab.
		 2. Select HTTPS in the dropdown menu.
		 3. Copy the URL under HTTPS.

![clone repository 1](https://github.com/GreenNinjaBoy/Story-Time-Adventures-PP3/blob/main/assets/readme-images/pp3-clone-repository-image-1.png?raw=true)
		 4. Open the IDE that you are working from for example [CodeAnywhere](https://app.codeanywhere.com/).
		 5. Sign in using your Github details.
![codeanywhere sign in](https://github.com/GreenNinjaBoy/Story-Time-Adventures-PP3/blob/main/assets/readme-images/cloning-repository-image-2.png?raw=true)

6. Click on the create new workspace button.
![create workspace image](https://github.com/GreenNinjaBoy/Story-Time-Adventures-PP3/blob/main/assets/readme-images/cloning-repository-image-3.png?raw=true)
		7.  Paste copied HTTPS and click create (Codeanywhere will now generate the virtual IDE).
![create workspace image 2](https://github.com/GreenNinjaBoy/Story-Time-Adventures-PP3/blob/main/assets/readme-images/pp3-clone-repository-image-4.png?raw=true)
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
- Then at the bottom, you can either choose to deploy your repository manually or have the system do it for you automatically.


** Insert image**

## Credits

**Code**

 - A lot of the code used came from research found on [Stackoverflow](https://stackoverflow.com/)

**Content**

 - The developer wrote all content.

**Media**

 - All ASCII text art came from using [pyfiglet](https://pypi.org/project/pyfiglet/0.7/)
 - All images used for the README.md can be found [here.](https://github.com/GreenNinjaBoy/Story-Time-Adventures-PP3/tree/main/assets/readme-images)

## Acknowledgements

This was my third project that was created and developed for portfolio as a student of  [Code Institute](https://codeinstitute.net/)  currently undertaking their course in Full Stack Software Development.

I would like to thank the following for all of the support throughout the development phase.

-   The Code Institute community, including fellow students and staff.
-   My family, especially my daugher who enjoyed reading along with the stories as they developed. My friends, and peers who have helped during the testing phase and provided valuable feedback.
-   My Mentor lauren-nicole Popich for her continuing advice and support during the development process. I can honestly say without her knowledge and guidence I would not be at the stage iIam at now

Jamie Connell Code Institute Student 2023
