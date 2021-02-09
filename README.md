# Basket Ball Tournament Information Management System #


## Installing ##

1. clone following git repository  https://github.com/ldasun/basketballInfo.git or download the and extract the content.
2. open shell and install the Dependencies by 

	```
	pip install -r requirements.txt
	```
	
3. execute following commands on a shell to migrate model to db.
	
	```
	 python manage.py makemigrations
	 python manage.py migrate
	```
	
4. create data from following command 

	```
	 python manage.py populate_data
	```
	
5. create super user by following command and remember the login information.

	```
	python manage.py createsuperuser
	```
	
## Running Server and Admin portal ##

	```	
	python manage.py runserver	
	```
	
	* Admin portal can be accessed by following URL

		http://127.0.0.1:8000/

	
## Rest End points ##

	1)To get player information
		http://127.0.0.1:8000/basketballinfo/api/players/<<player_id>>
	
		e.g. http://127.0.0.1:8000/basketballinfo/api/players/3
		
	2)To get list if players by team	
		http://127.0.0.1:8000/basketballinfo/api/players/getByTeam/?team_id=<<team_id>>
	
		e.g. http://127.0.0.1:8000/basketballinfo/api/players/getByTeam/?team_id=1
		
	3)To get list if players by given percentile
		http://127.0.0.1:8000/basketballinfo/api/teams/<<team_id>>/getPlayersByPercentile/?percentile=<<percentile>>
		
		e.g. http://127.0.0.1:8000/basketballinfo/api/teams/1/getPlayersByPercentile/?percentile=90 