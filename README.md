# Assignement#1
 A python file that creates bucket, creates object, view object, deletes object, deletes bucket, creates dynamo dbtable, inserts data and query data and another folder where users can upload and view data done in flask

## File name assignment.py

This file contains all the function reqested for S3 and dynamodb.
Simply run the file using terminal "python assignment.py" and the code will execute all the functions.

## Flask Files
The other files aside from assignment.py are the flask files that needs to run via command run flask. Firstly ensure to set FLASK_APP="app.py" then run flask.

For flask due to last minute notice, We've managed to do upload/view/delete object.

The requirements needed are to run the flask files:

boto3==1.9.235
botocore==1.12.235
Click==7.0
docutils==0.15.2
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.1
jmespath==0.9.4
MarkupSafe==1.1.1
python-dateutil==2.8.0
s3transfer==0.2.1
six==1.12.0
urllib3==1.25.6
Werkzeug==0.16.0

### Screenshot
![image](https://user-images.githubusercontent.com/73974236/98271396-dd349e00-1fca-11eb-96a0-fe61fdd2e691.PNG)
![image](https://user-images.githubusercontent.com/73974236/98271643-1bca5880-1fcb-11eb-86cd-cec8ba04acbf.PNG)
![image](https://user-images.githubusercontent.com/73974236/98271675-24bb2a00-1fcb-11eb-8f4a-65784ed3d2b1.PNG)