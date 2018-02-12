# ReachLocal
It is a simple django to display news 
## Installation

1. Clone app 
```
git clone https://github.com/thanhtungka91/ReachLocal.git
```
2. Run app (please install python, Virtualenv)  
```
https://virtualenv.pypa.io/en/stable/
```
install package (note the main packages) 
1. python > 2.7 
2. Django > 1.1 
```
pip install requirement.txt 
```

3. Start App 

```bash
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/articles/` to see the page 

## Configuration
### 1. Configue database 
This app is using sqlite3 for store the data 
1. creat the migration sql  
```python manage.py makemigrations articles```
2. mirgate db 
```python manage.py migrate```

3. add newsapi to .env file 
```NEWSAPIKEY="xxxx"```
### 2. get data from news api 
click on the tab at the top for crawl data at the first time, next for the update. 
