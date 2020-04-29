
# Developer Guide
1. install mysql  
    make sure use legecy password authentication  
2. run the `database_script.sql` 
3. install dependencies:  
    `conda install django`  
    `pip install djangorestframework`  
    `conda install mysqlclient`  
    `pip install google-api-core`  
    `pip install dialogflow`  
    `pip install pandas`

4. instal pyknow:  
    clone the repo from "https://github.com/buguroo/pyknow.git"  
    go to the project directory and run `pip install .`  

5. create the database based on   
    `0_database_creation.sql`


7. load data into tables by 
    `python 1_table_load.py`

8. debugging:  
    `python3 manage.py runserver 0.0.0.0:8000`  
    or add debug configuration for your preferred IDE
9. zip the folder dialogflow_objects and import the zip file into Google DialogFlow   
10.  generate a json key file in the Google Dialoge page:   
        General --> Service Account    
        Click the 3 dots --> generate key file   
    name file as 'project_key.json', put it into /SystemCode folder     

11. test the api response by postman:  

        GET http://127.0.0.1:8000/university_list/  

        POST http://127.0.0.1:8000/recommendation/
        {
            "name": "Norman",
            "preferred_country": "UK",
            "ielts_score": 3.8
        }  

        POST http://127.0.0.1:8000/chat/
        {
            "enquiry": "where on earth is Lancaster University "
        }

    or by curl  
        `curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/university_list/`  
        `curl -H 'Accept: application/json; indent=4' -X POST -d '{"name": "Norman","preferred_country": "UK","ielts_score": 3.8}' http://127.0.0.1:8000/recommendation/`  
        `curl -H 'Accept: application/json; indent=4' -X POST -d '{"enquiry": "where on earth is Lancaster University "}' http://127.0.0.1:8000/chat/`