# Python-automation
Small automation projects to handle downloads, backups etc.

## Running the download organizer automatically (macOS)
- Run: chmod 755 filename

- In the Automator app select Application

- Choose "Run Shell Script" and then select shell "/bin/bash"

- Paste the path to the file, for example: /Users/username/Documents/organize_downloads.py

- Save Automator object as "Download organizer"

- Open "Users & Groups" and go to "Login items". Press the plus sign and then add "Download organizer"

(Note: Important to have the shebang "#!/usr/local/bin/python3" as otherwise the Automator will run Python 2 as default)

## Adding custom command to create git repository

- Go to home folder (cd ~/) and run: touch .my_custom_commands.sh ("." will make it invisible and harder to delete)

- Add the following code to .my_custom_commands.sh: 



- Open the /.bash_profile with: subl ~/.bash_profile, then add the following line: source ~/.my_custom_commands.sh

## Adding sublime text as command (subl)

- Run in terminal: sudo ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl

