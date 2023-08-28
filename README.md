# Zendesk Guide Article Data Export

## Summary
Using the [Zendesk Help Center API](https://developer.zendesk.com/rest_api/docs/help_center/introduction) is challenging but often necessary as a Zendesk Guide content curator.

Exporting Zendesk Guide data requires use of this API. The Python scripts included in this repository
exports the data to a `.csv` file. This facilitates more control over Zendesk Guide Help Center information through access to actionable data.

**Feedback is welcome**
The process can be a little arduous, so any contributions, notes, feedback, etc. on this repository is greatly appreciated!

## Dependencies
* [Python 3](https://www.python.org/downloads/) (preferred)
* Python 2
* [Requests](http://docs.python-requests.org/en/master/)
* [pandas](https://pandas.pydata.org/) 

## Instructions
The scripts are currently written in Python. Python is therefore the first necesarry installation (see above).

`pip` is one way to install the necessary components. These instructions assume the use of `pip`. You can install `pip` [by following instructions in the documentation](https://pip.pypa.io/en/stable/installing/).

After  

1. Go to the command line.
2. Run `pip install requests`.
3. Download the scripts contained in this repository.
4. Edit the the scripts in this repository. Most important are the Zendesk credentials.
5. Navigate to the directory where the script is located (for example, if it were located on the desktop, run `cd /users/yourname/desktop`).
6. Run `python articleid.py` (or whatever script you are running).
7. The .csv file with the list of article titles, article id's, etc. will be created in the current directory.


## Notes
The Requests library suggests use of Python 3. 

As it currently stands, the scripts outside of the Article_Information_Export folder returns information as one column within a `.csv` file. For example, if you run the script to print titles then the return is only a list of titles.

If you don't change the endpoint (i.e. `/api/v2/help_center/en-us/articles.json?sort_by=updated_at&sort_order=asc`),then multiple exported csv's will line up.

This means that if you run the script for id's, then run the script for titles, all you will need to do is copy and paste the two outputs in a spreadsheet and they will correspond correctly. 

[For script editing purposes, use this guide](https://developer.zendesk.com/rest_api/docs/help_center/articles)
