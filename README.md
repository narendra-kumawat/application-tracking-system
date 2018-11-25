# application-tracking-system
1. Create a virtual environment either using vritualenv or any other virtual environment with python3.5 or python3.6.
If virtualenv is used then "virtualenv venv_name -p python3.6" and activate the vene using "source venv_name/bin/activate"

2. After that install all the required modules from requirements.txt
    pip install -r requirements.txt

3. Start the Django REST API server( manage.py is inside of application_tracking_system)
    python manage.py runserver 128.0.0.1:8000

4. There is a file "application-tracking-system.postman_collection.json". This file contains all the required api calls to the Djanog Server
    
5. Import this postman collection file into Postman and the resumes that are need to be analyzed are copied into application_tracking_system/CVAnalyzer/CV (only .docx and .pdf format are allowed) 

6. There are five api calls are available 

    http://127.0.0.1:8000/cvanalyzer/docx
        This api call will parse the *.docx file and check the resume  with the skillsets
        
    http://127.0.0.1:8000/cvanalyzer/pdf
        This api call will parse the *.pdf file and check the resume  with the skillsets
        
    http://127.0.0.1:8000/cvanalyzer/apply-for-job
        This api call stores the data of the job applicats into the AirTable 
        
    http://127.0.0.1:8000/cvanalyzer/job-description
        This api call stores the job description and basic skillset requirements for a job into AirTable. 
 
 7. Client side, nodeJS server can be used to store applicants information into AirTable and to start node server
    "node app.js" need to be run on terminal(app.js is inside of client_side-NodeJS_Anguler/CVAnalyzerFrontend/)
    
 
