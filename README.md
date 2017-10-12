# odk_demo
Demo for odk, illustrating front end test cases

Please note, there is a log and report file of a previously completed demo test run in this repository, to illustrate the files that are generated upon completion of the demo, if you do not want to go through the below steps of installation and running the tests.


Requirements:

* Python 2.7
* Robot Framework
* Robot Framework - Selenium2Library

Installation instructions:
Install pip via command line (for terminal, add sudo at start):
* python -m pip install -U pip

Install robot framework and selenium2library via command line (for terminal, add sudo at start):
* pip install robotframework
* pip install robotframework-selenium2library


You must install the latest version of Selenium Webdriver's Chromedriver and place it in your Python path. That can be found here: https://sites.google.com/a/chromium.org/chromedriver/downloads

After installation has been completed, open a command line and go to the top folder location of where you placed the downloaded files, like so:
* top folder 
* \_ odk/odk_mobile/shared_resources

Enter the following command in the command line:
* pybot -i demo odk/features/.


The demo will run as expected. As of 10/12/2017, this demo was in full passing state for all tests.
