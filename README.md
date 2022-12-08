# Smile Game
Author: Przemyslaw Baj
## Installation
### Backend
Setup Python virtual environment

```bash
cd ./backend
virtualenv venv
source myproject/bin/activate
```
Install requirements
```bash
pip install -r requirements.txt
```

Create DB tables
```bash
python db_init.py
```
Run
```bash
flask --app app run
```

### Frontend
Install packages
```bash
cd ./frontend
npm i
```
Run
```bash
npm run serve
```
