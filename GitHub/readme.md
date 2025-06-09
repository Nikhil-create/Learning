======================================================================
##### Course Details
###### Youtube Link: https://www.youtube.com/watch?v=S7XpTAnSDL4
======================================================================

##### > What is GitHub
It is a Distributed version control system, it tracks every change
automatically allowing muliple developers to work on same project
seamlessly and lets you navigate through the project history

##### > How to check the version of GitHub installed on your system.
###### Command: 
git --version

##### > Configure Github on your system
###### Command:
git config --global user.name 'Nikhil Rawal'
git config --global user.email 'nikhilrawal4775@gmail.com'
git config --global init.defaultBranch 'main'

##### > How to view git configurations
###### Command:
git config --list

##### > How to edit global configurations through editor
###### Command:
git config --global --edit 

##### > What are Repositories
This is where git track all the changes in your project

##### > How to initialize a folder as repository
###### Command:
git init

##### > How to change the default branch
###### Command:
git config --global init.defaultBranch 'main'

##### > How to find untrack changes
###### Command:
git status

##### > How to track the selective file changes
###### Command:
git add ./GitHub/readme.md

##### > What is commiting in github 
Commmiting in github is like taking the snapshot of your
project at the certain point, so that if anything happen
to the project in future you can easily rollback to the
previous version

##### > How to commit the changes
###### Command:
git commit -m 'Add readme.md file'
###### Hint:
-m : Required : Add the message with commit

##### > How to track all the changes
###### Command:
git add .

##### > How to check git history
###### Command:
git log

##### > How to rollback to previous version
###### Command:
Step 1: git log 
Step 2: git checkout 094e6b9ceb5f6c4ca09814dfbb4b07059e000349
###### Hint:
from Step 1 command pick the commit hash id of previous version
or you can checkout the branch

##### > How to checkout to current state
###### Command:
git checkout -f main
###### Hint:
-f : Not Required or Recommended : get to the branch by force

##### > How many types of repositeries are there in git
There are 2 types of repositories
###### Local Repository 
- This repository exists on your system
###### Remote Repository
- This is the repository which is stored in cloud server like GitHub

##### > How to change the branch name
###### Command:
git branch -M main

##### > How to link your local repository to the remote repository
###### Command:
git remote add origin https://github.com/Nikhil-create/Learning.git

##### > How to push the changes to the remote repo
###### Command:
git push -u origin main

##### > What are branches
Branches in git allow you to create different versions of your projects,
the main branch will be untouches when you work in new branch

##### > How to create the branch with the name test
###### Command:
git branch test
git checkout test (switch to test branch)
git checkout main (switch to main branch)
###### Hint:
when you creating the branch make sure to check in which branch you are in,
suppose you are in main branch and you run git branch command then the new
branch will be created based on main branch (your current branch)

##### > Directly switch to a new branch without sepratly creating it 
###### Command:
git checkout -b new-branch

##### > How to create branch depending on the source branch
###### Coommand:
git branch new-branch test
###### Hint
the above command will create a new-branch based on test branch

##### > How to map or publish the branch from local to remote-repo
###### Command:
git push --set-upstream origin test
or
git push -u origin test

##### > What is merge conflict
When two people work on same piece of code and we need to choose wich needs
to be pushes in main branch
###### Hint:
You can check rebase command for the same also

##### > Supose you made the changes in same fine simultaneously from branch1 and branch2 and branch2 changes merged first with the main branch
###### Command:
git checkout main
git pull
get checkout branch1
git merge main
(resolve the conflict in the editor)
git add .
git commit -m "resolved merge conflict"
git push

##### > How to discard the changes
###### Command:
Types of reset
1. Soft Reset - stage everything
2. Mixed Rest - unstage everything
3. Hard Reset - it will discard the changes permanently and you will not see them again
###### Command:
git rest <hash-commmit-code>
git rest --soft <hash-commmit-code>
git rest --hard <hash-commmit-code>

##### > How to revert the changes
###### Command:
git revert <hash-commit-code>

##### > How to stash the changes and work on priority work
###### Command:
git stash (stash the changes)
git stash list (view the stash)
git stash apply <stash@{i}> (get your stash)

##### > How to rebase a branch
###### Command:
[rebase-test branch] git rebase main


