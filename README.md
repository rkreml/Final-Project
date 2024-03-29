# Final-Project
EPSY 5200 Fall 2019 Final Project Files

This README shall be a document that will consist of version control. All updates will be listed as version numbers.
Within each version there will be a small explaination of what has changed and what lessons were leanred and which problems are still present.

Current Note: This script will only run and work entirely in Mac OS. If you are a Windows user, it will run but will not export your the csv to your working directory as that is specified differently.

Current Version: 1.1.0

Version 0.0.1 Notes:
Features:
    - Started investigating idea involving weather, user input, and graphing.
    - Looked into establishing connection with the weather API.
    - Looked into connecting with wikipedia as a means of decerning population filtering.
Work in Progress:
    - Figuring out how the graphic/table will be created.
Bugs still Present:
    - 
Lessons Learned:
    - Getting wiki to work will be a bit more challenging. Also implementing user input is tricky. I will want to include some error messages just in case.

Version 0.0.2
Features:
    - Included version control and hooked into github.
    - Changed the weather script from assignment 6 to include a 5 day forcast.
    - Added the mins and maxes for each of the 5 day forcast.
    - Retained current temperature for that particular day.
    - Retained current humidity percentage for current day.
Bugs still Present:
    - Still need to work on slicing the data of dictionary within a dictionary. So no data will currently work.
Lessons Learned:
    - Be careful with url typing to ensure the format of the URL is being followed, otherwise the dreaded 404 error will appear. Parameters may need to change depending on the type of API repository you are pulling information from.
    - Dictionaries can get extremely complicated when subset dictionaries are the same name as each other and the "key" is a unique key identifier.

Version 1.0.0
Features:
    - Includes a day-by-day breakdown of the minimum and maximum average temperature for all 5 days in the forecast.
    - Keep in mind that the minimum and maximum temperature for days 2 - 5 are the same as the weather API cannot accurately predict those temperature ranges.
Bugs still present:
    - (Not a bug): I still want to add additional locations/cities through user input.
    - (Not a bug): I want to add exporting the data into 
Lessons learned:
    - Indexing and slicing large dictionaries is difficult.

Version 1.1.0
Features:
    - Includes exporting the data into a ddataframe and writes into a .csv file in the local directory.
Bugs still present:
    - (Not a bug): I am still working on a loop for user input for additional locations.
Lessons learned:
    - Adding all of the data into a file structure is a bit challenging.

Version 1.2.0
Features:
    - Added NA conditional statement at the start to end script if needed.
Lessons learned:
    - Remembered sys and .exit().
    - Will have to work on conditional loops in a future project.
