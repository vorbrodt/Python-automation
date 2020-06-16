# Python-automation
Different automations using Python. Currently: 

- An organizer for the download folder which runs automatically. The Python script is run through the Automator. 

- A shell and Python script, which togheter creates git repository locally and on github. The Python script utilizes web scraping through using selenium. 

## Running the download organizer automatically (macOS)
- Run: chmod 755 filename

- In the Automator app select Application

- Choose "Run Shell Script" and then select shell "/bin/bash"

- Paste the path to the file, for example: /Users/username/Documents/organize_downloads.py

- Save Automator object as "Download organizer"

- Open "Users & Groups" and go to "Login items". Press the plus sign and then add "Download organizer"

(Note: Important to have the shebang "#!/usr/local/bin/python3" as otherwise the Automator will run Python 2 as default)

## Adding custom command to create git repository

- Download .my_custom_commands.sh ("." before filename will make it invisible and harder to delete) to home directory (cd ~/)

- To use chrome with selenium a chromedriver is nedded. Find chromdriver on google and download one for your operating system

- Download create_git_rep.py and make sure all paths in .my_custom_commands.sh and create_git_rep.py are correct, as well as the loggin information (username and password).

- Open the /.bash_profile with: subl ~/.bash_profile, then add the following line: source ~/.my_custom_commands.sh

- To create git repository: creategitrep repository_name

### Tip! Adding sublime text as command in terminal (subl)

- Run in terminal: sudo ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl

- (Note: If no /user/local/bin exists run "mkdir /user/local/bin" in home directory (cd ~/)

