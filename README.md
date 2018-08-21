# Zendesk Guide Article Data Export

### Summary
Navigating and using the [Zendesk Help Center API](https://developer.zendesk.com/rest_api/docs/help_center/introduction) can be a challenging but often necessary experience.

Exporting Zendesk Guide data requires extracting the information via their API. The Python scripts included in this repository
will export the data to a .csv file. This facilitates more control over Zendesk Help Center information and an expanded ability to obtain actionable data.

This process can be a little rough, so any contributions, notes, feedback, etc. is greatly appreciated!

### Dependencies
* [Python 3](https://www.python.org/downloads/) (preferred)
* Python 2
* [Requests](http://docs.python-requests.org/en/master/)
* [pandas](https://pandas.pydata.org/) (Not required, but helpful for data manipulation if you edit scripts)

### How to Use
The process to use these scripts can be arduous. Once everything is set up, however, it is easy to run the script many times.

As the scripts are currently written in Python, Python is the first necesarry installation (see above).

`pip` is suggested to install the necessary components. There are multiple ways to obtain `pip`, [here is the documentation](https://pip.pypa.io/en/stable/installing/).

With `pip` installed, it is easy to install the necessarry libraries.

1. Go to the command line.
2. Run `pip install requests`.
3. Download the scripts contained in this repository.
4. Edit the components in the script! Most important are the Zendesk credentials.
5. Navigate to the directory where the script is located (for example, if it were located on the desktop, run `cd /users/yourname/desktop`).
6. Run `python articleid.py` (or whatever script you are running).
7. The .csv file with the list of article titles, article id's, etc. will be created in the current directory.


### Notes
The requests library suggests use of Python 3. Scripts will reflect subtle differences. 

!!! - As it currently stands, the scripts print a ONE COLUMN .csv. This means if you run the script to print titles, all that will be returned is a list of titles.

This being said, if you don't change the endpoint (i.e. `/api/v2/help_center/en-us/articles.json?sort_by=updated_at&sort_order=asc`), then the multiple exported csv's WILL LINE UP.

This means that if you run the script for id's, then run the script for titles, all you will need to do is copy and paste the two outputs into a spreadsheet and they will correspond correctly. 

It is therefor possible to build a comprehensive spreadsheet with the id, url, html_url, body, etc. by simply editing the script and running it several times. Then combining the outputs by simply copying and pasting. 

[For script editing purposes, use this guide](https://developer.zendesk.com/rest_api/docs/help_center/articles)
