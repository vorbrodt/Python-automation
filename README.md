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





