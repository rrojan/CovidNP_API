# CovidNP_API

Work in progress.

## Akhir kasari garincha ta install?
- Clone repo, create virtual env, run `pip3 install -r requirements.txt`
- Copy-paste `geckodriver` driver for Firefox (for your OS) into `venv/bin` folder (otherwise Selenium driver won't run on venv)

## API Routes and endpoints

- localhost:8000/daily
- localhost:8000/total
- localhost:8000/area

Filters (add after url)

?province
?date
?gender
?district

Provinces : 1, 2, bagmati, gandaki, ...
date: in formal `2021-05-20`
gender: male female
district: 77 districts 
