#!/bin/bash


"""
Run the python script which creates a git repository and then create connect to a local git repository. Also starts sublime text so work can begin!
$1 - name of repository
"""
function creategitrep() {

  #navigate to right folder
  cd
  cd /Users/maximilianvorbrodt/Documents/PROGRAMMING/Simple\ python\ projects/Automation

  #run script to create git repository
  python create_git_rep.py $1

  #create git repository locally
  cd ../../GitRepositories/$1
  touch README.md
  git init
  git remote add origin https://github.com/vorbrodt/$1.git #use SSH
  git add .
  git commit -m "Initial commit"
  git push -u origin master

  #start sublime text
  subl

}
