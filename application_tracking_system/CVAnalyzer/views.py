from django.shortcuts import render
from CVAnalyzer.word_search import AnalyseResume 
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json

class PDF(APIView, AnalyseResume):

    def post(self, request):
        skillset = request.data['skillset']
        file_name = request.data['file_name']
        self.skillSet(skillset)
        words = self.wordsFromPDF(file_name)
        return Response(self.countSkills(words))

class Docx(APIView, AnalyseResume):

    def post(self, request):
        skillset = request.data['skillset']
        file_name = request.data['file_name']
        self.skillSet(skillset)
        words = self.wordsFromDocx(file_name)
        return Response(self.countSkills(words))

class CheckAPI(APIView):

    def post(self, request):
        data = request.data['data']
        return Response({"data":data})

class InsertEmployeeDetails(APIView):

    def post(self, request):
        url = 'https://api.airtable.com/v0/appIyBjSX0X2gSaX6/Applicants'
        data = \
        {
            "fields": {
                "Attachments": [
                {
                    "url": "https://dl.airtable.com/xwv2ejXtTBqbTqjcnbQi_Chippypotato.jpg"
                },
                {
                    "url": "https://dl.airtable.com/e6kCK3Z0SUS6hhCUoKcD_chippypotatoresume.docx"
                }
                ],
                "Onsite Interview Score": "2 - worth consideration",
                "Applying for": [
                "recj2CZhrc55kIwIi"
                ],
                "Email Address": request.data['Email Address'],
                "Stage": request.data['Stage'],
                "Phone": request.data['Phone'],
                "Name": request.data['Name']
            }
        }
        api_key = 'keyuzmWgNnw0YlRWd'
        # headers = {"Content-Type": "application/json", "Authorization": "Bearer "+api_key}
        # r = requests.post(url,headers = headers,  data = data)
        r = requests.post(url, headers={"Authorization":"Bearer "+api_key, "Content-Type":"application/json"}, data = json.dumps(data))
        print(r)
        return Response({"response":r})

class InsertJobDescription(APIView):

    def post(self, request):
        url = 'https://api.airtable.com/v0/appIyBjSX0X2gSaX6/Positions'
        api_key = 'keyuzmWgNnw0YlRWd'
        headers={"Authorization":"Bearer "+api_key, "Content-Type":"application/json"}
        data = \
        {
            "fields": {
            "Required Experience": request.data['Required Experience'],
            "Name": request.data['Name'],
            "Description": request.data['Description'],
            "Applying for position": [
                "recSprJ6wVb3wtVtD",
                "recdVfVb6Dj7u5A5N"
                ]
            }
        }
        r = requests.post(url, headers={"Authorization":"Bearer "+api_key, "Content-Type":"application/json"}, data = json.dumps(data))
        print(r)
        return Response({"response":r})