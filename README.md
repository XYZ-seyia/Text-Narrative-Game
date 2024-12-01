# How to Run the Project

1. **Download the Zip File**:
   - You can find the `Hogwarts_nights-1.0-win.zip` file in the `main` branch of this repository.

2. **Extract the Files**:
   - Extract the downloaded `Hogwarts_nights-1.0-win.zip` file to a directory of your choice.

3. **Run the Program**:
   - Open the extracted `Hogwarts_nights-1.0-win` folder.
   - Double-click the `Hogwarts_nights.exe` file to run the program.
4. **View the Source Code**:
   - The source code is located in the `game` folder inside the extracted `Hogwarts_nights-1.0-win` folder, specifically in the `script.rpy` file.
   - To view and edit the source code, you need to install the `Ren'Py Language` extension in Visual Studio Code (VS Code).
# Game Introduction
## ideas
This is a Wizarding World adventure for Harry Potter fans!
Players are transported to the Wizarding World and are about to start a journey filled with tests of courage and ingenuity, and to realise the true spirit of the four Hogwarts colleges!
## Main storyline
Hogwarts Castle has awakened its own consciousness and taken control of everyone, leaving only Headmaster Dumbledore struggling to hold on. As a warrior from another world, are you willing to help the Headmaster collect the treasures left behind by the four founders to seal the castle's consciousness and save Hogwarts?
## Plot and Choices
A single playthrough lasts about 10mins, and the player needs to find four treasures left behind by the founders , and there are five endings in total, depending on the player's choices and performance in the game.
Click this link!(https://github.com/XYZ-seyia/Text-Narrative-Game/blob/main/choices%20and%20endings.jpg) to view the structure of choice and endings!
I hope you could reach the Perfect Ending!
# Functionality we implement and statements we use**
## Why ren’py?
After consulting various engine documentation and developer forums, we have chosen to learn the Ren'Py platform for developing text-based adventure games for the following reasons:
1. **Python-based Language**:
   - Ren'Py's scripting language is based on Python, which is very user-friendly for us since we have already learned Python.
3. **Mature Narrative Framework**:
   - Ren'Py provides a dialogue system and branching story management, which significantly reduces the workload in developing narrative games. In contrast, using other frameworks like Pygame would require us to build these systems from scratch.
5. **Free and Open Source**:
   - Ren'Py has an active community and a wealth of tutorial resources, which provide valuable support for our development.

##  Text Adventure Game Framework
Understanding the Ren'Py Framework
Ren'Py game scripts consist of numerous files with the extension .rpy located in the game/ directory. Ren'Py checks each file in Unicode code point order and uses their contents as the script.  
For us, we specifically need to write the following documents:  
1.**script.rpy file**:
 - This is the core script file of the game, containing the main logic, storyline, character dialogues, and game flow control. By carefully designing and writing the script.rpy file, developers can create an engaging story and memorable gaming experience.

2.**screens.rpy file**:
 - This is the core file for defining the UI in a Ren'Py project, allowing developers full control over the game's interface appearance and behavior. We will also use it to implement some immersive exploration interaction features in 2D scenes.

3.**options.rpy file**:
  - This is used to define the game's settings menu, allowing players to customize certain game options, such as volume control, display mode, text speed, etc.  

## For implementing the main storyline logic and flow, we primarily use the following statements:
label statement: Label statements allow the given name to be assigned to a program point. They exist solely to be called or jumped to, either from Ren'Py script, Python functions, or from screens.
jump statement: The jump statement is used to transfer control to the given label. Unlike call, jump does not push the next statement onto a stack. As a result, there's no way to return to where you've jumped from.
return statement: The return statement pops the top statement off of the call stack, and transfers control to it. If the call stack is empty, the return statement restarts Ren'Py, returning control to the main menu.
 
## For implementing character dialogue and branching choices, we use the following statements and functions:
Character: A Python function that includes a series of keyword arguments. These keyword arguments control the character's behavior.
say statement: Used in dialogue and narration scenes, the syntax for writing a say statement is a minimized syntax structure.
menu statement: Followed by an indented block of statements. This block may contain a say statement and must contain at least one menu option, presenting choices to the user.
if/else: Enriches player choices, game variables, or game state branching storylines and logic.

## Inserting Multimedia Assets
The four statements related to images are:
image - Defines a new image.
show - Displays an image on a layer.
scene - Clears the layer and optionally displays an image on that layer.
hide - Removes an image from a layer.
Different audio channels:
Ren'Py supports any number of audio channels. There are three general audio channels predefined:
music - The music playback channel.
sound - The sound effects playback channel.
voice - The voice playback channel.

## Motion and Performance
transform statement: Creates a transformation effect, with the following syntax:
atl_transform ::= "transform" qualname ( "(" parameters ")" )? ":"
with statement: Used to apply transition effects during scene changes, making the appearance and disappearance of images less abrupt. The with statement begins with the keyword with.

## Implementing Scene UI Interaction
call statement: The call statement is used to transfer control to the given label. It also pushes the next statement onto the call stack, allowing the return statement to return control to the statement following the call.
User interface statements: Used to create visual components and add them to the interface or a closed visual component. Includes (screen, imagebutton, text, and their related features).

# Difficulties and challenges
After implementing the basic game flow and debugging it, we made the following improvements in order to make the format of the game richer and improve the user experience.
This is more challenging than the original basic flow development

## Difficulty 1 Inserting a video into a text adventure game
In order to enrich the player's playing experience, we decided to incorporate a video element. At first we played our mp4 videos directly using the movie sprite link, but found that it didn't work.
So we checked the official RENPY documentation and found out that it was a video format incompatibility problem. So we used the recommended ffmpeg tool to convert the video encoding format, and used the renpy.movie_cutscene() function to play.

## Difficulty 2 Preventing users from skipping videos
Once we have successfully inserted the video, a second problem immediately follows. When the user clicks too quickly, it will be easy to skip the video content, affecting the integrity of the game story experience. Therefore, we need to think of a way to prevent users from accidentally clicking.
The idea behind our solution is that user clicks are used as a form of input, then we need to disable user input directly while the video is playing. So a Noskip modal screen is defined to disable user input in the modal screen, which is called before the video is played and hidden after the video is finished.

## Difficulty 3 Preventing Users from Missing Guidance Statements
We tried to define a screen, call pause, and so on, but users would still miss the guidance statement when they clicked too fast. In the end, we chose the character method to define a center_narrator to act as a bootstrap interface and set a parameter to display it in the center of the screen.
