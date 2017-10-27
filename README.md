# odk_demo
Demo for odk, illustrating front end test cases

* Please note, there is a log and report file of a previously completed demo test run in this repository, to illustrate the files that are generated upon completion of the demo, if you do not want to go through the below steps of installation and running the tests. 
* To view the log and report properly, you must download them and open them in a web browser, as opening them for viewing in a git repository will usually show them in HTML markup.


Architecture/layout:
The architecture of this demo is built primarily using a 3 folder structure: features, step_definitions, page_objects. It is a keyword driven framework using Robot Framework.
* Features:
  * High level files that are the actual test suites/test cases run.
  * Human readable in Gherkin syntax, they are written in plain English for ease of understanding, and can be written by non-technical members of a team for automation engineers to program them.
* Step Definitions:
  * Mid level files that are called by the feature files.
  * They have minimal amount of scripting and are meant to be a clean filter of procedural steps between the high level feature files and low level page object files.
  * The idea is these step definition keywords would allow other team members to easily build their own feature file tests by having step definition keywords to choose from and assemble them.
* Page Objects: 
  * Low level files that store the test data.
  * Called by the step definition files and thus twice removed from the feature files, this is where data such as element locator variables and several keywords/functions with required logic is found.
  * Page object files are also designed to be unique to certain pages on the site. 
    * For example, if you have a test that has part of the test in the login area and then part of the test in the homepage area, you would have 2 separate page object files: 1 for login, 1 for homepage. 
    * The variables and function keywords related to the login area (login fields, login button, etc) would be stored in the login page object file, while the variables and function keywords related to the homepage area (homepage banner, homepage welcome text, etc) would be stored in the homepage page object file.
    * This greatly assists with maintenance and keeping the code base orderly and easier to locate where updates need to be made.



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
