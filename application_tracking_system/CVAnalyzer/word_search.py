import glob
import os
import warnings
import textract
import requests
from gensim.summarization import summarize
# from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# from sklearn.neighbors import NearestNeighbors
# from werkzeug import secure_filename
# from autocorrect import spell
# import PyPDF2
from CVAnalyzer.text_parsing import ParsingOfFormats
from CVAnalyzer.KMPStringMatchingAlgorithm import KMP


class AnalyseResume(KMP, ParsingOfFormats):

    def __init__(self, skillsets):

        with open('SkillSet/'+skillsets) as f:
            self.skills = f.readlines()

    def skillSet(self, skillset_list):
        self.skills = skillset_list
        for i in range(len(self.skills)):
            self.skills[i] = self.skills[i].strip()
        # print(skills)

    def wordsFromPDF(self, file_name):
        return self.pdf2text(file_name)

    def wordsFromDocx(self, file_name):
        return self.docxToText(file_name)

    def countSkills(self, words):
        self.skillSummery = {}
        word_stream = ' '.join(words)
        # print(word_stream)
        for skill in self.skills:
            self.skillSummery[skill] = len(self.KMPSearch(skill, word_stream) ) 
        print(self.skillSummery)
        return self.skillSummery

if __name__=="__main__":
    analyse_r = AnalyseResume('skills.txt')
    words = analyse_r.wordsFromPDF('CV/Resume --Rohini Prakash.pdf')
    analyse_r.countSkills(words)
