import PyPDF2 
import textract
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import docx2txt
from CVAnalyzer.tokenized_word_process import WordCleaning

nltk.download('punkt')
nltk.download('stopwords')

nltk.download('wordnet')

class ParsingOfFormats(WordCleaning):

    def textCleaning(self, text):
        #The word_tokenize() function will break our text phrases into #individual words
        tokens = word_tokenize(text)
        #we'll create a new list which contains punctuation we wish to clean
        punctuations = ['(',')',';',':','[',']',',','/','|']
        #We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords
        stop_words = stopwords.words('english')
        #We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.
        keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
        # print(keywords)
        return keywords

    def pdf2text(self, pdfFileName):
        #write a for-loop to open many files -- leave a comment if you'd #like to learn how
        # filename = 'Resume --Rohini Prakash.pdf' 
        filename = pdfFileName
        #open allows you to read the file
        pdfFileObj = open('CVAnalyzer/CV/'+filename,'rb')
        #The pdfReader variable is a readable object that will be parsed
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        #discerning the number of pages will allow us to parse through all #the pages
        num_pages = pdfReader.numPages
        count = 0
        text = ""
        #The while loop will read each page
        while count < num_pages:
            pageObj = pdfReader.getPage(count)
            count +=1
            text += pageObj.extractText()
        #This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
        if text != "":
            text = text
        #If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text
        else:
            text = textract.process(fileurl, method='tesseract', language='eng')
        # Now we have a text variable which contains all the text derived #from our PDF file. Type print(text) to see what it contains. It #likely contains a lot of spaces, possibly junk such as '\n' etc.
        # Now, we will clean our text variable, and return it as a list of keywords.
        words = self.textCleaning(text)
        return self. normalize(words)


    def docxToText(self, docxFileName):
        # doc = docx.Document(docxFileName)
        # fullText = []
        # for para in doc.paragraphs:
        #     fullText.append(para.text)
        # return '\n'.join(fullText)
        # extract text
        text = docx2txt.process('CVAnalyzer/CV/'+docxFileName)
        # print(text)
        words = self.textCleaning(text)
        return self.normalize(words)
        # print(self.remove_non_ascii(text))
        # print(self.normalize(words))
        # return text


if __name__ == "__main__":
    ps = ParsingOfFormats()
    ps.pdf2text('CV/Resume --Rohini Prakash.pdf')
    ps.docxToText('CV/180517_Vasanthi Kasinathan.docx')