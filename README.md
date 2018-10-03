# Domain Australia Scraper

## About project
This is a personal and side project for finding a better place to rent in Sydney taking multiple factors into consideration.

__Factors:__
- Commute time
- Commute Cost
- Number of bedrooms against price

#### Motivation
Sydney is one of the most expensive cities to live in the world. Public transport isn't great and the cost to commute is increasing everytime. 
The purpose of this project is to find a "bang for your buck" place to rent using:
 - commuting time: Property might be within 30 Km from the city but commuting time might be the same as living 50km away (better properties).
 - commuting cost: Catching multiple transport modes (train+bus) might increase the cost.
  

## How to use this code:
1. clone repo
2. Install libraties `pip install -r requirements.txt`
3. Linux/Max: `./startup.sh`

### Commute time
Commute time is calculated using the trip planner api through [NSW Open Data Platform](https://opendata.transport.nsw.gov.au/).
A developer account is required to use the APIs. The [documentation](https://opendata.transport.nsw.gov.au/get-started) contains all the required information to get started. 
Once the account and Application is created, the request can be tested [online](https://opendata.transport.nsw.gov.au/node/601/exploreapi).


 



link to Jira board: https://shannondussoye.atlassian.net/browse/DOMAIN

##### Personal note
##### Exporting pycharm virtual environment
1. cd to venv location `cd ~/venv/domain-au`
2. `source bin/activate`
3. `pip3.6 freeze -l > ~/Github/domain-au/requirements.txt` 
4. `deactivate

https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv`