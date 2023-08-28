# Zendesk Guide Data Export

## Overview
The python script in this folder will export a .csv file with the following rows:
* Article ID
* Article Title
* URL
* Vote Sum
* Vote Count
* Author ID
* Section ID

These are defined in the [Help Center API docs](https://developer.zendesk.com/rest_api/docs/help_center/articles).

The python script will automatically write the `.csv` file to the current directory from where the script is being executed.

## Instructions 
View this video for video instructions.

1. Go to the command line.
2. Run `pip install requests`.
3. Download the script contained in this repository.
5. Navigate to the directory where the script is located (for example, if it were located on the desktop, run `cd /users/yourname/desktop`).
6. Run `python Zendesk_Guide_Article_Export.py` 
7. The `.csv` file will be created in the current directory.


## Video Instructions
View this [video](https://youtu.be/nGYQwV-kpyE) for video instruction.


## Exporting Internal Articles Using OAuth
You must use an OAuth token to export every article in your Knowledgebase, including non-public ones. To obtain a Zendesk OAuth token visit [their API developer console](https://developer.zendesk.com/requests/new), enter your subdomain, then click "authorize". 

Instead of running Zendesk_Guide_Article_Export.py, run OAuth_Full_Export.py. Enter the token obtained from the developer portal when prompted by the script as opposedto the basic authentication credentials. 
