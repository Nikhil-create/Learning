======================================================================
##### Course Details
Youtube Link: https://www.youtube.com/watch?v=S7XpTAnSDL4
======================================================================

##### What is GitHub
It is a Distributed version control system, it tracks every change
automatically allowing muliple developers to work on same project
seamlessly and lets you navigate through the project history

##### How to check the version of GitHub installed on your system.
###### Command: 
git --version

##### Configure Github on your system
###### Command:
git config --global user.name 'Nikhil Rawal'
git config --global user.email 'nikhilrawal4775@gmail.com'
git config --global init.defaultBranch 'main'

##### How to view git configurations
###### Command:
git config --list

##### How to edit global configurations through editor
###### Command:
git config --global --edit 

##### What are Repositories
This is where git track all the changes in your project

##### How to initialize a folder as repository
###### Command:
git init

##### How to change the default branch
###### Command:
git config --global init.defaultBranch 'main'

##### How to find untrack changes
###### Command:
git status

##### How to track the selective file changes
###### Command:
git add ./GitHub/readme.md

##### With is commiting in github 
Commmiting in github is like taking the snapshot of your
project at the certain point, so that if anything happen
to the project in future you can easily rollback to the
previous version

##### How to commit the changes
###### Command:
git commit -m 'Add readme.md file'
###### Hint:
-m : Required : Add the message with commit

##### How to track all the changes
###### Command:
git add .


