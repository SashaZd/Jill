from django.db import models

# Create your models here.

# Table for Users
class CCUser(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)

	def __unicode__(self):
		return self.first_name

	def getResponseData(self):

		#Create Resposne Dictionary
		response_data = {}
		response_data["first_name"] = self.first_name
		response_data["last_name"] = self.last_name
		response_data["email"] = self.email
		response_data["user_id"] = self.id

		projects_worked_on = []

		projects = CCProjects.objects.filter(created_by_user=self.id)
		if projects and len(projects) > 0:
			for proj in projects:
				projects_worked_on.append(proj.getResponseData())

		response_data["projects_worked_on"] = projects_worked_on

		return response_data


class CCProjects(models.Model):
	project_title = models.CharField(max_length=200)
	created_by_user = models.ForeignKey('CCUser', related_name="created_by_user")
	document_body = models.TextField()
	

	def __unicode__(self):
	    return self.name

	def getResponseData(self):

		#Create Resposne Dictionary
		response_data = {}
		response_data["project_title"] = self.project_title
		response_data["created_by_user"] = self.created_by_user.id
		response_data["document_body"] = self.document_body
		response_data['project_id'] = self.id

		return response_data


# Table for Questions asked to Watson
class CCQuestion(models.Model):
	question_text = models.CharField(max_length=200)
	answers = models.ForeignKey('CCAnswer')
	from_project_id = models.ForeignKey('CCProjects', related_name="from_project_id")

	def __unicode__(self):
	    return self.name

	def getResponseData(self):

		#Create Resposne Dictionary
		response_data = {}
		response_data["question_text"] = self.question_text
		# response_data["asked_by_user"] = self.asked_by_user.id
		response_data["from_project_id"] = self.from_project_id.id
		response_data['question_id'] = self.id

		return response_data

class CCReferencePapers(models.Model):
	evidence_text =  models.CharField(max_length=200)
	paper_title =  models.CharField(max_length=200)
	paper_author = models.CharField(max_length=200)
	paper_link =  models.CharField(max_length=200)
	referenced_by_project = models.ManyToManyField(CCProjects)
	question_id = models.ForeignKey('CCQuestion', related_name="question_id")

	def __unicode__(self):
	    return self.name

	def getResponseData(self):

		#Create Resposne Dictionary
		response_data = {}

		response_data["evidence_text"] = self.evidence_text
		response_data["paper_title"] = self.paper_title
		response_data["paper_author"] = self.paper_author
		response_data["paper_link"] = self.paper_link
		response_data['paper_id'] = self.id

		# Need later, maybe? Don't delete the next code segment
		all_associated_projects = self.referenced_by_project.all()
		response_data['referenced_by_project'] = {}

		if len(all_associated_projects) > 0:
			for eachProj in all_associated_projects:
				response_data['referenced_by_project'].append(eachProj.id)

		return response_data


# Table for Answers Obtained
class CCAnswer(models.Model):
	answer_text =  models.CharField(max_length=200)
	confidence =  models.CharField(max_length=200)
	evidence_list = models.ForeignKey('CCReferencePapers')
	question_id = models.ForeignKey('CCQuestion')

	def __unicode__(self):
	    return self.name

	def getResponseData(self):

		#Create Resposne Dictionary
		response_data = {}
		response_data["answer_text"] = self.answer_text
		response_data["confidence"] = self.confidence
		response_data["question_id"] = self.question_id.id
		response_data['answer_id'] = self.id

		response_evidence = []
		evidenceList = CCReferencePapers.objects.filter(answer_id=self.id)

		if evidenceList and len(evidenceList)>0:
			for eachRef in evidenceList:
				response_evidence.append(eachRef.getResponseData())

		response_data["reference_papers"] = response_evidence

		return response_data




