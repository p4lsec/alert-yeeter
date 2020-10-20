## Alert Yeeter
* [General info](#general-info)
* [Setup](#setup)
* [Preconfigure](#preconfigure)
* [Example](#example)


## General info
alert-yeeter.py is a script designed to monitor an element on a website, and email when that element is updated. The script is designed to itierate through all of the .ini config files in that directory.  This means that you can monitor multiple sites or XPath values by having multiple .ini files. 

Once your config file(s) are [preconfigured](#preconfigure), this script can be run on a cron job.  To run it once an hour, open your crontab:

```
crontab -e
```

Then insert the following at the bottom on a new line:

```
0 */1 * * * cd /home/$USER/Scripts/alert-yeeter && python3 alert-yeeter.py
```

Note: It's important to cd into the script directory, since the script searches through the directory you specify for .ini files.


## Setup

First, clone this repo:

```
git clone https://github.com/p4lsec/alert-yeeter.git
```

Before running, you will need to install the following dependencies (if you don't already have them:

```
pip3 install lxml requests
```

## Preconfigure
Before starting, you will need to configure your .ini config file.  The template file is self-explanatory, but for a good tutorial on XPath, see [this walkthrough](https://blog.scrapinghub.com/2016/10/27/an-introduction-to-xpath-with-examples).  Your final XPath should look like this:

![config file example](https://p4lsec.files.wordpress.com/2020/10/dar.ini_.jpg)

## Execution

To run the script manually, navigate to the directory, and run:

```
python3 alert-yeeter.py
```
