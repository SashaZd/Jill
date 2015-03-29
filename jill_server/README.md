cc8803
======

Our CC 8803 project with Ashok Goel and IBM Watson

Notes for Aziz : Look at the UserManager file to understand how to go about making the QuestionManager. You can put in the API call from Watson there, and then create the JSON response object to return. 


User 
======
fields: Email, Password, Name, u_id

1. Create New User
2. Delete User
3. Update User
4. Login
5. Logout

API Calls for User:

You can find all the URLs in the URL file in the Server folder. We'll try to keep this updated too if we can. 

1. 	URL : api/user/ 
	Type : POST
	Parameters: first_name, last_name, email 

2. 	URL : api/user/<user_id>/
	Type : GET

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
2. Find old question by qid 
3. Find all questions from uid
4. Find all questions from r_id 
5. 

##Task List

1. Set up Django Project
2. Build login screen
3. APIs for Watson
4. Build Website 
