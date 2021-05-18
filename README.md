# CovidNP_API

## Akhir kasari garincha ta install?
- Clone repo: `git clone https://github.com/rrojan20/CovidNP_API.git`
- Create new virtual environment (lets call it venv): `virtualenv venv`
- Activate venv: `source venv/bin/activate`
- Copy-paste your web driver into `venv/bin` folder (otherwise Selenium driver won't run on venv)
- `pip3 install -r requirements.txt`
- In your root folder (where manage.py is) run: `python3 manage.py runserver`
- Enjoy. Or don't. It's still in dev, things can and will crash.

Visit `127.0.0.1:8000/swagger/` for docs.
