# Domain Australia Scraper

[ ![Codeship Status for shannondussoye/domain-au](https://app.codeship.com/projects/dbac8260-a915-0136-761d-2e2cf4f8517e/status?branch=master)](https://app.codeship.com/projects/308716) [![Build Status](https://travis-ci.org/shannondussoye/domain-au.svg?branch=master)](https://travis-ci.org/shannondussoye/domain-au) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/2463d3283dea4ec0891ec2d39ecd71dd)](https://www.codacy.com/app/shannondussoye/domain-au?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=shannondussoye/domain-au&amp;utm_campaign=Badge_Grade) [![Maintainability](https://api.codeclimate.com/v1/badges/c9c3d8f699602f4a2d58/maintainability)](https://codeclimate.com/github/shannondussoye/domain-au/maintainability) [![Known Vulnerabilities](https://snyk.io/test/github/shannondussoye/domain-au/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/shannondussoye/domain-au?targetFile=requirements.txt)


## About project
This is a personal and side project for finding a better place to rent in Sydney taking multiple factors into consideration.

__Factors:__
- Commute time
- Commute Cost
- Number of bedrooms against price
- Suburb Profile from ABS
- POI (shopping places)

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

##### Create branch
1. git checkout -b [name_of_your_new_branch]
2. git push origin [name_of_your_new_branch]

https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv`
