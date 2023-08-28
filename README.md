# Zendesk Guide Article Data Export

## Summary
Using the [Zendesk Help Center API](https://developer.zendesk.com/rest_api/docs/help_center/introduction) is challenging but often necessary as a Zendesk Guide content curator.

Exporting Zendesk Guide data requires use of this API. The Python scripts included in this repository
exports the data to a `.csv` file. This facilitates more control over Zendesk Guide Help Center information through access to actionable data.

**Feedback is Welcome**\
The process can be a little arduous, so any contributions, notes, feedback, etc. on this repository is greatly appreciated!

## Dependencies
The scripts are currently written in Python. Python is therefore the first necesarry installation (see above).

`pip` is one way to install the necessary components. These instructions assume the use of `pip`. You can install `pip` [by following instructions in the documentation](https://pip.pypa.io/en/stable/installing/).

* [Python 3](https://www.python.org/downloads/) (preferred)
* Python 2
* [Requests](http://docs.python-requests.org/en/master/)
* [pandas](https://pandas.pydata.org/) 

## Instructions
Select the script to run. There are specific instructions in the script's corresponding directory. The `Article_Information_Export` script will export all data into one `.csv`. The other scripts export specific types of data(i.e. only "titles") into a `.csv`.

To run a script:
1. Go to the command line.
2. Run `pip install requests`.
3. Download the scripts contained in this repository.
4. Edit the the scripts in this repository. Most important are the Zendesk credentials.
5. Navigate to the directory where the script is located (for example, if it were located on the desktop, run `cd /users/yourname/desktop`).
6. Run `python articleid.py` (or whatever script you are running).
7. The .csv file with the list of article titles, article id's, etc. will be created in the current directory.

*Feel lost?*
If you are unsure of where to start, use the `Article_Information_Export` script. There is a corresponding YouTube video walkthrough. 

## Notes
The Requests library suggests use of Python 3 over Python 2. 

[Follow the Zebdesk API guide to edit the scripts](https://developer.zendesk.com/rest_api/docs/help_center/articles)
