# CovidNP_API

### Full docs [here](https://covidnp.xyz/docs/)

### Work in progress

COVID NP: The automated COVID statistics scraper for Nepali data. 

Access data for your web/mobile applications through an API, or query the data with powerful filters like date, province, district, gender, etc for your ML projects!


### Showcase: [https://covidnp.xyz](https://covidnp.xyz)

Note: (WIP) There are some issues with selenium in the production server atm, however both the scraper and API work perfectly fine locally.


## Running the project locally

### Requirements:
- Django 3.2
- DRF 3.12
- bs4
- lxml
- Selenium

### Installation:
- Clone repo
- Create virtual environment and install dependencies (`pip3 install -r requirements.txt`)
- Add the `geckodriver` driver for Firefox (for your OS) into `venv/bin` folder or add the folder to your PATH
- Activate the virtual environment and run the testing server (`python3 manage.py runserver`)

