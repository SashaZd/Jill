cc8803
======

Our CC 8803 project with Ashok Goel and IBM Watson

@Aziz : Look at the UserManager or QuestionManager file to understand how to go about making any other API calls. I've mentioned what all are compulsory imports and how to write new API calls. We have a list of API calls to be made on this ReadMe. Just keep making one and adding the details like I've done below. 

@Carl/Shweta : 

	1. All API calls are AJAX calls. 
	2. Once you've installed Django and pulled the latest repo to run the Django Server and make API calls use, 
```
		$ python manage.py runserver  
```
	3. Use whatever the base_URL the runserver gives you and then add the "/api/..." to the end of it to make the calls. 



User 
======
fields: Email, Password, Name, u_id

1. Create New User

```
	URL : api/user/ 
	Type : POST
	Parameters: first_name, last_name, email 
	Sample Response: 
		{"first_name": "Sasha", "last_name": "Azad", "user_id": 1, "email": "sasha172@gmail.com", "projects_worked_on": []}
```

2. Delete User

3. Update User

4. Login

5. Logout

6. Get User

```
	URL : api/user/<user_id>/
	Type : GET
	Sample Response: 
		{"first_name": "Shweta", "last_name": "Raje", "user_id": 3, "email": "sraje@gatech.edu", "projects_worked_on": []}
```


Research Paper 
======
fields : r_id, title, main text, references, qid, uid, reference_style

1. New Research Paper 
2. Update Research Paper with user typed content (Save) 
3. Delete Research Paper 
4. Update Research Paper with References 
5. Update Research Paper with content from studies


Questions
======
fields : q_id, question text, keywords, context, date, uid 

1. Create new question 

```
	URL : api/question/
	Parameters : question_text
	Type : POST
	Sample Response: 
		{
			"evidences": [
				{
					"evidence_text": "In the Mediterranean Basin, species suffer from unfavorable conditions such as recurrent forest fir", 
					"documentPath": "", 
					"trimmed_document": "https://watson-wdc01.ihost.com/instance/522/deepqa/v1/question/document/T_62088F95193880395F6AC70EBBB72B20/0/-1", 
					"paper_title": "Moya Pine Cone 2008 1286492597676 : Anatomic basis and insulation of serotinous cones in Pinus halep", 
					"originalFile": "Moya_Pine_Cone_2008_1286492597676.docx"
				},
		]}
```

2. Find old question by qid 
3. Find all questions from uid
4. Find all questions from r_id 


##Task List

1. Set up Django Project
2. Build login screen
3. APIs for Watson
4. Build Website 
