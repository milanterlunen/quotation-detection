#!/usr/bin/env python
# coding: utf-8

# <font size=5>Run Text_Matcher Algorithm</font>

# In[2]:


#Troubleshooting: !jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10 if you 
# get a message about the data rate limit
#from matcher import Text, Matcher
#import json
#import pandas as pd
#import numpy as np
#from IPython.display import clear_output


#get_ipython().system('jupyter nbconvert --to script drop-junk_phrases_test.ipynb')



# In[197]:


#Troubleshooting: !jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10 if you 
# get a message about the data rate limit


# import libraries needed
import sys

import pandas as pd
import numpy as np


# TBD: Some of these libraries are relics of earlier notebooks.
# Reactivate any of the following that are needed, delete any that aren't needed.

try:
   import nltk
except:   
   get_ipython().system('{sys.executable} -m pip install nltk')

try:
   import termcolor
except:   
   get_ipython().system('{sys.executable} -m pip install termcolor')

try:
   from matcher import Text, Matcher
except:
    get_ipython().system('{sys.executable} -m pip install matcher')
    #from matcher import Text, Matcher  
    #🚨 have to look into this
    
try:   
   from IPython.display import clear_output
except:
   get_ipython().system('{sys.executable} -m pip install IPython.display')
   from IPython.display import clear_output


try:
    import re
except:
    get_ipython().system('{sys.executable} -m pip install re')
    import re


try:
    import json
except:
    get_ipython().system('{sys.executable} -m pip install json')
    import json

try:
    import ipywidgets as widgets
except:
    get_ipython().system('{sys.executable} -m pip install ipywidgets')
    import ipywidgets as widgets

#%pip install altair

try:
    import altair as alt
except:
    get_ipython().system('{sys.executable} -m pip install altair')
    import altair as alt


try:
    from pathlib import Path
except:
    get_ipython().system('{sys.executable} -m pip install pathlib')
    from pathlib import Path



# from IPython.display import display

try:
    from IPython.display import display
except:
    get_ipython().system('{sys.executable} -m pip install IPython.display')
    from IPython.display import display

#new viz library for single-column heatmap    

try:
    import matplotlib.pyplot as plt
except:
    get_ipython().system('{sys.executable} -m pip install matplotlib.pyplot')
    import matplotlib.pyplot as plt


try:
    from tabulate import tabulate 
except:
    get_ipython().system('{sys.executable} -m pip install tabulate')
    from tabulate import tabulate


try:
    from ipywidgets import Label
except:
    get_ipython().system('{sys.executable} -m pip ipwidgets')
    from ipywidgets import Label
    from iwidgets import widgets


import os

try:
    import copy as copy
except:
    get_ipython().system('{sys.executable} -m pip copy')
    import copy as copy


try:
    import ast as ast
except:
    get_ipython().system('{sys.executable} -m pip ast')
    import ast as ast


try:
    import csv as csv
except:
    get_ipython().system('{sys.executable} -m pip csv')
    import csv as csv


try:
    import seaborn as sns 
except:
    get_ipython().system('{sys.executable} -m pip install seaborn')
    import seaborn as sns

try:
    from nltk.corpus import names
except:
    get_ipython().system('{sys.executable} -m pip nltk.corpus')
    from nltk.corpus import names

try:
    import nltk as nltk
except:
    get_ipython().system('{sys.executable} -m pip nltk')
    import nltk as nltk

try:
    import tkinter as tk
except:
    get_ipython().system('{sys.executable} -m pip tkinter')
    import tkinter as tk
    from tkinter import ttk

from tkinter import ttk    

#from collections import Counter
#from matplotlib import pyplot as plt
#%matplotlib inline
#plt.rcParams["figure.figsize"] = [16, 6]
#plt.style.use('ggplot')




# In[198]:


from tkinter import filedialog
# returns the seleeted path to  selected folder by using the forlder picker 

def open_folder_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_selected = filedialog.askdirectory()  # Open the folder dialog
    print(f'Folder Selected: {folder_selected}')
    return folder_selected
#print( open_folder_dialog())


# In[199]:


#!{sys.executable} sudo python -m nltk.downloader -d /usr/local/share/nltk_data all
#!{sys.executable} download('stopwords')


# In[200]:


#🚨  to figure out nltk

#from nltk.corpus import brown
#brown.words()


# In[201]:


# writes user preference data, to a csv file
# stores the values of dataDir, authorName, projectName

def write_user_data_to_csv_file(dataDir, authorName, projectName):
  # Open (or create) a CSV file in the current working directory

  with open('user_data.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      # Write the data
      writer.writerow([dataDir, authorName, projectName])
  return    




# In[202]:


# Call the function  
pathDataDir= r"C:\Users\bdt\Documents\Data"
authorName= "Joyce"
projectName= "1923_Ulysses" 

write_user_data_to_csv_file(pathDataDir, authorName, projectName)  

print("Data written to CSV file successfully!")   


# In[203]:


#reads uer data from a csv file
# returns: a list of user data

def read_user_data_from_csv_file():
    # Open the CSV file in the current working directory

    if os.path.exists('user_data.csv'):
        with open('user_data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                return row
    else:
        return None

# Use the function
#write_user_data_to_csv_file('dataDir', 'authorName', 'projectName')
#    with open('output.csv', 'r') as file:
#        reader = csv.reader(file)

# Use the function
row = read_user_data_from_csv_file()
if row is not None:
    dataDir=row[0]
    authorName=row[1]
    projectName=row[2]

    print(row)
else:
    print('No matching data found.')


# In[ ]:





# In[204]:


# ACTION: copy path to data directory 


row = read_user_data_from_csv_file()


#🚨  default in developer stage:  pathDataDir=  r"C:\Users\bdt\Documents\Data"


# In[205]:


if not row == None:
    pathDataDir= row[0]
    #path_data = path_data.replace("\\\\", "\\")
    authorName= row[1]
    projectName= row[2]
else:
    pathDataDir= r"C:\Users\bdt\Documents\Data"
    authorName= "Joyce"
    projectName= "1922_Ulysses"

#r"C:\Users\bdt\Documents\Data"
pathDataDir2=Path(pathDataDir)


# In[206]:


# Create a text widget for the path input

pathDataDir_input = widgets.Textarea(
    # 🚨has to be removed 
    value=pathDataDir,
    placeholder="Paste the path here",
    description="Path:",
    rows=6,
    width= 30)
# Add the instruction line above the input field
pathDataDir_instructionLine = widgets.Label("Paste the path below:")

pathDataDir=pathDataDir_input.value
pathDataDir2 =Path(pathDataDir)

# Create the widgets
folderPathLabel = widgets.Label(value="Find data dir folder path by folder dialog:")
folderPathText = widgets.Text(value= pathDataDir, placeholder="Select a folder...")
folderPathButton = widgets.Button(description="Browse")

# Define the event handler for the button click
def browse_button_clicked(button):
    folderPath = open_folder_dialog()
    if not folderPath == None:
        folderPathText.value = folderPath
        pathDataDir_input.value= folderPath

# Attach the event handler to the button click event
folderPathButton.on_click(browse_button_clicked)


folderPath_dialog_panel= widgets.VBox([folderPathLabel, widgets.VBox([folderPathText, folderPathButton])])


# Create the panel layout
panelLayout = widgets.VBox([

    
    folderPathLabel,
    widgets.HBox([folderPathText, folderPathButton])
])

# Display the panel
display(panelLayout)

# Create a VBox layout with the path_input widget
instructionDataDirLine= widgets.Label("Or paste the path below:")

panelDataDirLayout = widgets.VBox([pathDataDir_input])

# Create a button widget for the commit action
commitDataDirButton = widgets.Button(description="Confirm")
textDataDirLabel = widgets.Label(value="")
commit_dataDir_box= widgets.HBox([commitDataDirButton, textDataDirLabel])

panelDataDirLayout.children = (instructionDataDirLine, pathDataDir_input, commit_dataDir_box)

# Define the event handler for the commit button
# Update the commit_button_clicked function


def input_field_changed(change):
    newPath = change['new']
  
    newPath = newPath.replace("\\", "\\\\")
    newPath = newPath.replace("'", "")
    newPath = newPath.replace('"', '')
    if Path(newPath).exists():
        instructionDataDirLine.value = "Paste the path below:"
        textDataDirLabel.value = 'This path exists'
        commitDataDirButton.layout.visibility = 'visible'
        commitDataDirButton.description = 'Confirm'
    else:
        commitDataDirButton.layout.visibility = 'hidden'
        instructionDataDirLine.value = "Please try again. Paste the path below"
        textDataDirLabel.value = 'This path does not exist'
    
    if Path(newPath).exists():
        instructionDataDirLine.value = "Paste the path below:"
        textDataDirLabel.value = 'This path exists'
        commitDataDirButton.layout.visibility = 'visible'

        commitDataDirButton.description = 'Confirm'
    else:
        commitDataDirButton.layout.visibility = 'hidden'
        # commit_button.visible = False
        instructionDataDirLine.value = "Please try again. Paste the path below"
        textDataDirLabel.value = 'This path does not exit' 
    # Perform actions based on the new value
    
# Attach the event handler to the value change event of input_field
pathDataDir_input.observe(input_field_changed, names='value')

def commitDataDirButton_clicked(button):
    global pathDataDir, pathDataDir2
    newPath= str( pathDataDir_input.value).replace("\\","\\\\")
    newPath = newPath.replace("'", "")
    newPath = newPath.replace('"', '')
    exists= Path(newPath).exists()
    if  exists:
        instructionDataDirLine.value="Paste the data root path below:"
        pathDataDir = newPath
        pathDataDir2 = Path(newPath)
        commitDataDirButton.description='Confirmed'
        textDataDirLabel.value='This path exists'
        
        

        
    else:
        instructionDataDirLine.value="Please try again. Paste the path below"
        textDataDirLabel.value='This path does not exist'

# Attach the event handler to the commit button
commitDataDirButton.on_click(commitDataDirButton_clicked)
# Display the panel
display(panelDataDirLayout)


# In[207]:


# a quoatattion is an object containing these  attributes
# location: is a tuple of begin position and end position
# sting : the actual phrase in the source A text defined by the location
# numMatches is the count of quotations in source B corpus
# junk is the boolean value , set true when the phrase is connsoiderde as junk by the user
# index is the index in the quotations_list
# extra is a spare atribute for future use
#   
class quotation:
    def __init__(self, string, loc):
        # nu  zonser attribuut self.text
        self.location = loc
        #self.quotations_list = quotations_list 
        self.string = string
        self.numMatches = 0
        self.junk= False
        self.index = 0
        self.extra = False

    
        
    


# In[208]:


# quotations class contains functionality to create a uniqueQuotationsList by the data belonging 
# to a bookProject 

class quotations:

    def __init__(self, bookProject ):
        #self.bookProj = bookProject

       

        #if bookProject.text is None:
        #    bookProject.read_sourceA()  
        #    print(" bookProject.text is made")
        #else: 
        self.text= bookProject.text
        # print(self.text)
        self.uniqueQuotationsList = None

        self.locationsInA = bookProject.df['Locations in A']
        

        #self.uniqueQuotationsList = None

        print(len(self.locationsInA))
        #self.uniqueQuotationsList= self.make_uniqueQuotationsList()
        self.uniqueQuotationsList = self.make_uniqueQuotationsList()
      
        
        print(f"len uniqueQuotationsList : {len(self.uniqueQuotationsList)}")
        return 

    # creates a sorted unique quotations_list, usisng the data from a bookProject  

    def make_uniqueQuotationsList(self):

        # self is a bookProject instance, with attribute locationsInA

        #locationsInA= self.locationsInA 
        non_empty_locations = [loc for loc in self.locationsInA if loc != []]
        # Flatten the list
        # Using list comprehension
        flattened_locations = [item for sublist in non_empty_locations for item in sublist]
        sorted_locations = sorted(flattened_locations)
        self.sorted_locations= sorted_locations
    
        #print(len(sorted_locations))
        #for loc in sorted_locations:
        #    print( f"{loc[0]},   {loc[1]}")  

        loc1 = sorted_locations[0]
        text=self.text
        string = text[loc1[0]:loc1[1]+1]
                
          
        uniqueQuotationsList = []
        index=0
        new_quotation = quotation(string, loc1)
        new_quotation.index=index
       
        new_quotation.numMatches= 0
        #uniqueQuotationsList.append(new_quotation)
        

        for i in range(0, len(sorted_locations)):     
            if sorted_locations[i]==loc1:
                new_quotation.numMatches += 1       
            else:
                uniqueQuotationsList.append(new_quotation)
                loc1 = sorted_locations[i]
                index+=1
                string= self.text[loc1[0]:loc1[1]+1]
                junk= False
                #all_equal = True
        
                #new_location2= quotation2(string,loc1   )
                string = text[loc1[0]:loc1[1]+1]
                new_quotation = quotation(string, loc1)
                new_quotation.numMatches = 1
                new_quotation.index= index
        #self.uniqueQuotationsList= uniqueQuotationsList

        return uniqueQuotationsList 
    
       
    def add_uniqueQuotationsList(self): 
        pass

    #def read_corpus(self):  
    #    with open(self.corpus_sourceB) as f:
    #        rawProcessedData = f.readlines()
    #    self.data_fulltext_jsonl = [json.loads(line) for line in rawProcessedData]
    #    return self.data_fulltext_jsonl  

    #def remove_quotation(self, quotation):
    #    if quotation in self.quotation_list:
    #        self.quotations_list.remove(quotation)
    #        self.num_quotations = len(self.quotation_list)
    #    return unique_quotation_list

 


# In[209]:


# the class 'book_Project'  contains all functionalitity to create a
# uinique quotations list and  user filtered versions of that list 
# setting or getting user settings for reated user sessions working on this project
# reading and writing these settings from and to csv files

 
 # the class defines project dirs, short filename, make project data
# etc, facilitating the use of these projects in phase 2 and 3   
# 


class Book_Project:
  def __init__(self, dataDir, authorName, pubBookName):
   
    #dataFDir is string of root dir path
    # pubBookName contains string pubicationyear and name of the book 
    self.pubBookName = pubBookName

    # authorName contains sting with name of the author
    self.authorName = authorName

    #projectName cpntains string with authorname and pubBookName 
    self.projectName = f"{self.authorName}_{self.pubBookName}"
   
    # dataDir contains a pathobject of path to the root directory of aall bookprojects data 
    # data     
    self.dataDir = Path(dataDir)
    
    # define all the project dirs

    #projectDir contains the Path object to the root directory of this book project
    self.projectDir= Path(self.dataDir/self.authorName/pubBookName)


    #sourceDir contains the Path object to the source directory of this book project
    
    self.sourceDir= Path(self.projectDir/'SourceText')

    #corpusDir contains the Path object to the corpus directory of this book project
 
    self.corpusDir=Path(self.projectDir/'TargetCorpus')

    #resultsDir contains the Path object to the results directory of this book project
    
    self.resultsDir=Path(self.projectDir/'Results')
     
    # the project directories are created if they don't exist

    self.make_projectDirs()

    #the string hyperparsuffix is created by make_hyperparsuffix()
    self.hyperparsuffix=self.make_hyperparsuffix()

    # the path to the plain text of the book project is defined 
    self.pathPlainText=Path(self.sourceDir/f"{self.projectName}_plaintext.txt")
    
    # the path to the JSONL file of the book project is defined 
    self.pathJSONL=     Path(self.resultsDir/f"{self.projectName}_results_{self.hyperparsuffix}.jsonl")
        
    # the path to the new JSONL file after phase 02 of the book project is defined 
    
    self.pathJSONL_New= Path(self.resultsDir/f"{self.projectName}_results_{self.hyperparsuffix}_new.jsonl")
    
    #the attribute text is initialized
    self.text = None

    #the attribute df is initialized
    self.df = None

    #the attribute dfNew is initialized
    self.dfNew= None

    #the attribute unique_quotations _list is initialized
    #uniqueQuotationsList will be a list of all unique quotations, ordered by locatiuon
    # in ascending order 
    self.uniqueQuotationsList = None

    #the attribute junkphrases is initialized
    #junk phrases will conatain the list of all junk phrases
    self.junkPhrases = []

    #self.uniqueQuotationsList= quotations(self).uniqueQuotationsList

    #self.scan_project_data()
    # check if all the prject dirs exist 
    self.all_projectDirs_exist()

  # make an indepent copy of the original df  
  def make_dfNew(self):
    self.dfNew= copy.copy(self.df)

    return

  # update the approved list of non-junk phrase quotations , in the columns of dfNew

  def update_uniqueQuotationsList(self, new_uniqueQuotationsList):
    self.uniqueQuotationsList = new_uniqueQuotationsList
    return
    
  # create the text object of the book project, by reading the corresponding textfile   
  def read_sourceA(self):
    pathPlainText = self.pathPlainText
    with open(pathPlainText, encoding='utf-8') as f: 
      rawText = f.read()
      self.text=rawText
    return rawText 

  # create de dataframe df by reading the corresponding JSONL file 
  def make_df(self):
    path = self.pathJSONL
    if path.exists():
    # Load results as pandas dataframe
      df = pd.read_json(path, lines=True) 
      self.df=df
    else: 
      print(f"file {path}  does not exist" )
    return df   

   # create de dataframe dfNew by reading the corresponding JSONL file  
  def read_dfNew_from_file(self):

    path = self.pathJSONL_New
    if path.exists():
    # Load results as pandas dataframe
      dfNew = pd.read_json(path, lines=True) 
      self.dfNew= dfNew
    else: 
      print(f"file {path}  does not exist" )
    return dfNew   

  def write_dfNew_to_file(self): 

    path = self.pathJSONL_New
    self.dfNew.to_json(path, orient='records', lines=True)
      
      # Load results as pandas dataframe

    return    

  # writes the unique quotations list to a csv file

  def write_uniqueQuotationsList_to_csv(self):

    if self.uniqueQuotationsList is not None:
      pathQuotationsCSV = os.path.join(self.resultsDir, "quotations.csv")
      print(len(self.uniqueQuotationsList))
      
      print( pathQuotationsCSV )
      with open(pathQuotationsCSV, 'w', newline='', encoding='utf-8') as file:
          writer = csv.writer(file)
          writer.writerow(['junk', 'location', 'string', 'numMatches', 'index'])  # writing headers
          for q in self.uniqueQuotationsList:
              writer.writerow([str(q.junk), q.location, q.string, q.numMatches, q.index])
              print(f"{q.junk}, {q.location},  {q.string}, {q.numMatches}, {q.index}")

    else:
      print("self.uniqueQuotationsList is None")  
    return  

#'junk', 'location', 'string', 'numMatches', 'index'

  # create the uniqueQuotationsList  by reading the coreponding csv file

  def read_uniqueQuotationsList_from_csv(self):
    #self.uniqueQuotationsList=[]
    pathQuotationsCSV = os.path.join(self.resultsDir, "quotations.csv")
    with open(pathQuotationsCSV, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        self.uniqueQuotationsList = []
        i=0
        for row in reader:
          i +=1
          if not len(row)==5:
            print(f"{i}, {len(row)} ")

          location_list = ast.literal_eval(row[1])
          q= quotation(self.text, location_list)
          q.junk= bool( row[0])
          q.location= location_list
          q.string= str(row[2])
          q.numMatches=int(row[3])  # Convert the integer to a string
          q.index= int(row[4])
          self.uniqueQuotationsList.append(q)
    return self.uniqueQuotationsList


  # make the data for this book project by reading and processing the corresponing data files  
  def read_data(self): 
    if self.text is None:
      self.read_sourceA()  
      print(" self.text is made")
    if self.df is None:  
      self.make_df()
      self.make_dfNew()
      print(" bookProject.df is made")
    self.uniqueQuotationsList= quotations(self).uniqueQuotationsList
    return


  # save de  data of the unique _quottions_list tot a csv file
  def write_quotations_list_to_CSV(self):
    
    pathQuotationsCSV = os.path.join(self.resultsDir / "quotations.csv")
              
    with open( pathQuotationsCSV , 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(['junk', 'location', 'string', 'numMatches', 'index'])  # writing headers
    
      for q in self.uniqueQuotationsList:
        writer.writerow([q.junk, q.location, q.string, q.numMatches, q.index])     
          
    return

  # make_projectDirs(self): creates the project directiories if thay do'n't exist yet 

  def make_projectDirs(self):
    if not self.sourceDir.exists():
      self.sourceDir.mkdir(exist_ok=True)
    if not self.corpusDir.exists():
      self.corpusDir.mkdir(exist_ok=True)
    if not self.resultsDir.exists():
      self.resultsDir.mkdir(exist_ok=True)
    return   
    
  # creates a string by using hyperparsuffix default protocol   
  def make_hyperparsuffix(self):    
    thresh = 2
    cut = 3
    ngram = 2
    mindist = 3
    nostops = True
    hyperparSuffix = f"t{thresh}-c{cut}-n{ngram}-m{mindist}-{'nostops' if nostops else 'stops'}"
    return hyperparSuffix

  # all_projectDirs_exist(self) checks if all project directories exist

  def all_projectDirs_exist(self):
    #preetting the value of the return variable exist to False  
    dataDirExists= self.dataDir.exists()
    if not dataDirExists: 
      print( f"The data directory {self.dataDir}  does not exist")
    else:
      dataDirExists = True
      resultsDirExists = self.resultsDir.exists()
      
      if not resultsDirExists:
        print( f"The results directory {self.resultsDir}  does not exist")
      else:
       resultsDirExists = True 
      
      corpusDirExists = self.corpusDir.exists()
      if not corpusDirExists:
        print( f"The corpus directory {self.corpusDir}  does not exist")
      else:
        corpusDirExists = True  
      
      sourceDirExists = self.sourceDir.exists()
      if not sourceDirExists:
        print( f"The source directory {self.sourceDir}  does not exist")
      else:  
        sourceDirExists = True      
    
    allDirsExist = dataDirExists and sourceDirExists and resultsDirExists and corpusDirExists and sourceDirExists
    return allDirsExist


  #  get_junkPhrases(self) runs thouwgh the uniqueQuuuotationsiiid checks if the quotations are 'junk' , 
  # and returns a list of junk phrases

  def get_junkPhrases(self):
    setup(
        name='bookproject',
        version='1.0',
        packages=[''],
        url='',
        license='',
        author='',
        author_email='',
        description=''
    )
    for q in self.uniqueQuotationsList:
      if q.junk:
        junkPhrases.append(q.string) 
        self.junkPhrases=junkPhrases
      return junkPhrases  

  # write_junkPhrases_to_csv(self) writes the list of junk phrases to a csv file
  
  def write_junkPhrases_to_csv(self):
    pathJunkPhrasesCSV = os.path.join(self.resultsDir, "junkPhrases.csv")
    with open(pathJunkPhrasesCSV, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["string"])  # writing header
        for string in self.junkPhrases:  # Removed parentheses
            writer.writerow([string])
    return file
  
  # set_junkPhrases(self) creates a list ofjunkPhrases out of the uniqueQuotationsList 
  # and sets the value of the attribute self.junkPhrases with this 
  # list of junk phrases

  def set_junkPhrases(self):
    junkPhrases=[] 
    for q in self.uniqueQuotationsList:
      if q.junk:
       junkPhrases.append(q.string) 

    self.junkPhrases=junkPhrases
    self.write_junkPhrases_to_csv()
    return junkPhrases  
      
  
  # read_junkPhrases_ from csv(self) fills the attribute self.junkPhrases with list of junk+phrases, 
  # read out of the the corresponding csv file
  # in which this list is stored

  def read_junkPhrases_from_csv(self):
    pathJunkPhrasesCSV = os.path.join(self.resultsDir, "junkPhrases.csv")
    junkPhrases = []
    with open(path_junkPhrases_CSV, 'r', newline='', encoding='utf-8') as file:
      reader = csv.reader(file)
      next(reader)  # Skip the header
    
      i=0
      for row in reader:
        i +=1
        if not len(row)==1:
          print(f"{i}, {len(row)} ")
        string=row[0] 
        junkPhrases.append(string)
    self.junkPhrases =junkPhrases
    return junkPhrases        


  # update_all_items_with_accepted_quotations(self) updates the dataframe dfNew,
  # updateing the columns 'Loçations_in A'and 'Locations in B'

  def update_all_items_with_accepted_quotations(self):
      
    def check_loc(qloc,locs_list):

      # make a sorted list of locs_list, odered by starting index 
      # of the locations in that list

      #locs = sorted(locs_list, key=lambda x: x[0])
      #write('locs_list is sorted')
      # use  the boolean variable check for checking if the object qloc is in that list     
      check = False
      for loc in locs:
        if qloc[0]> loc[0]:
          #check = False
          break
        else:
          if qloc == loc:
            check = True
            break 
      return check

    locsInA = self.df['Locations in A'] 
    locsInB = self.df['Locations in B']
    #print(f"length  locsInB  {len(locsInB)}")
    #initiaaize  new_locsInA and in B 
    new_locsInA = []
    new_locsInB = []


    #maker list of all not junk quatation locations
    locs = []
    for q in self.uniqueQuotationsList: 
      if not q.junk:
        locs.append(q.location)
    
    # locs kist is srted by ascending value of the start position    
    locs = sorted(locs, key=lambda x: x[0])
    print('locs_list is sorted')
    if locs==[]:
      print("no accepted quotations")

      return
    else:
      #iterate over all journal items in the dataframe
      for j, item in enumerate(locsInA):
        new_item_A = []
        new_item_B = []
        if isinstance(item,list) and item != []:
          if isinstance(item[0], list):

            # iterate over all locations in the item
            for k, loc in enumerate(item): 
              if check_loc(loc, locs):
                new_item_A.append(loc)
                #new_item_B.append(locsInB[j,k]) 
          else: 
            loc = item 
            if check_loc(loc, locs):
              new_item_A.append(loc)
              new_item_B.append(locsInB[j,k])             

        new_locsInA.append(new_item_A)
        new_locsInB.append(new_item_B) 

    #df.loc[row_indexer, "col"]
    self.dfNew['Locations in A'] = new_locsInA
    self.dfNew['Locations in B'] = new_locsInB

    # still have to reduce the dfNew where the locations in A are empty []

    return

  #def read_sourcetextA(self):
  #  self.sourceText_name = str(Path(self.sourceDir/f"{self.projectName}_plaintext.txt"))
  #  with open(self.sourceText_name) as f: 
  #    rawText = f.read()
  #  self.plain_sourcetextA = rawtext  # Text(rawText,self.projectName)
  #  return self.plain_sourcetextA

 
  #def read_JSONL(self):
  #  path = self.pathJSONL
  #  if path.exists():
    # Load results as pandas dataframe
  #    self.df = pd.read_json(path, lines=True)  
  #  else: 
  #    print(f"file {path} does not exist" )
  #  return


# Load the corpus you want to find results in
  #def read_corpusA(self):
  #  self.corpusFile_path = Path(self.corpusDir/f"{self.projectName}_fulltext.jsonl")
  #  with open(self.corpusFile_path) as f:
  #    rawProcessedData = f.readlines()
  #  self.data_fulltext_jsonl = [json.loads(line) for line in rawProcessedData]
  #  return self.data_fulltext_jsonl



# In[210]:


import os
#def scan_bookProjects(dataDir, authorName):
#    author_dir = Path(dataDir / authorName)
#    bookProjects_list = [folder.name for folder in os.scandir(str(author_dir)) if folder.is_dir()]
#    return bookProjects_list

#preparatory facilitations for building the Book_Project instances

#for making the Book_Project projectName string

def make_projectName(pub_year,book_title):
    projectName= f"{pub_year}_{book_title}" 
    return projectName

# for making the Book_Project publication year string: pub_year

def make_pub_year(projectName):
    pub_year = projectName.split("_")[0]
    return pub_year

# for getting a list of book project names in the author's directory
def scan_bookProjects(dataDir, authorName):
    author_dir = os.path.join(str(dataDir), authorName)
    bookProjects_list = [folder.name for folder in os.scandir(author_dir) if folder.is_dir()]
    return bookProjects_list


# for making the Book_Project book title string: book_title

def make_book_title(projectName):
    book_title = projectName.split("_")[1]
    return book_title    


# In[211]:


# this class scans all authornames that correspond to subfolders under the data dir path.
class ProjectsData:
    def scan_Subdirs(self, dataDir):
        #dataDir is a pathlib Path object
        authorsList = [folder.name for folder in os.scandir(str(dataDir)) if folder.is_dir()]
        self.authorsList = authorsList
        return authorsList

    def __init__(self, dataDir):
        self.dataDir = dataDir
        self.authorsList = self.scan_Subdirs(self.dataDir)
        


# In[212]:


#🚨  for developpers stage. To be removed 
all_projects = ProjectsData(pathDataDir2)


print(all_projects.authorsList)


# In[213]:


authorName = all_projects.authorsList[1]

   
pubTitleName = scan_bookProjects(pathDataDir, authorName)[0]
bookProj = Book_Project(pathDataDir, authorName, pubTitleName)   #
print( bookProj.pathJSONL)
bookProj.read_data()


# In[214]:


# are emements in locations in A location objects(index-start index-end) or  stringb objects? 



# In[215]:


myQuotationsList = bookProj.uniqueQuotationsList

# Sort the list by decreasing value of q.numMatches

ascending= False

def sort_quotations_list_by_frequency(quotations_list,ascending):

    sortedQuotationsList = sorted(quotations_list, key=lambda q: q.numMatches, reverse= not ascending)
    return sortedQuotationsList




def sort_quotations_list_by_location(quotations_list,ascending):
    sortedQuotationsList = sorted(quotations_list, key=lambda q: q.location[0], reverse= not ascending)
    return sortedQuotationsList


def sort_quotations_list_by_string(quotations_list,ascending):
    sortedQuotationsList = sorted(quotations_list, key=lambda q: q.string, reverse= not ascending)
    return sortedQuotationsList


# In[216]:


ascending = False
sortedQuotationsList= sort_quotations_list_by_frequency(myQuotationsList,ascending)  

for i, q in enumerate(sortedQuotationsList):
    print(f"{i}, {q.location[0]},{q.location[1]}, {q.numMatches},  {q.string}")


# In[217]:


ascending = True
sortedQuotationsList= sort_quotations_list_by_string(myQuotationsList,ascending)  

for i, q in enumerate(sortedQuotationsList):
    print(f"{i}, {q.location[0]},{q.location[1]}, {q.numMatches},  {q.string}")

#for i, q in enumerate(myQuotationsList):
#    print(f"{i}, {q.location[0]}, {q.numMatches},  {q.string}") 


# In[218]:


print(len(quotations(bookProj).uniqueQuotationsList))


# In[219]:


#bookProj.df.columns


# In[220]:


# ACTION: 
#🚨  


instructionLine = widgets.Label("Chose your book project, and press Confirm button:")

# Create a dropdown widget
authors_dropdown = widgets.Dropdown(
    value= authorName,
    options=all_projects.authorsList,
    description='Authors:'
    )

authorName = authors_dropdown.value

books_dropdown = widgets.Dropdown(
    #value= projectName,
    options=scan_bookProjects(pathDataDir, authorName),
    description='Books:'
    )


# Create a VBox layout  with the path_input widget
# panelLayout = widgets.VBox([authors_dropdown, books_dropdown  ])

# Create a button widget for the commit action
commit_button = widgets.Button(description="Confirm")
text_label=widgets.Label(value="")
commit_box= widgets.HBox([commit_button, text_label])
panelLayout=widgets.VBox()
panelLayout.children = (instructionLine,authors_dropdown, books_dropdown, commit_box)

def authorName_changed(change):
    global authorName, books_dropdown
    
    authorName = change['new']
    books_dropdown.options = scan_bookProjects(pathDataDir, authorName)
    books_dropdown.value = books_dropdown.options[0]  # Select the first book by default
    commit_button.description='Confirm'

# Attach the event handler to the value change event of authors_dropdown
authors_dropdown.observe(authorName_changed, names='value')


def commit_button_clicked(button):
    global authorName, pubTitleName,bookProj
   
    authorName = authors_dropdown.value
    pubTitleName = books_dropdown.value

    bookProj = Book_Project(pathDataDir, authorName, pubTitleName)   
    bookProj.read_data()
    
    #print( bookProj.pathJSONL)
    #print( bookProj.pathPlainText)
    commit_button.description='Confirmed'

    #text_label.value='This path exists'
    
# Attach the event handler to the commit button
commit_button.on_click(commit_button_clicked)
# Display the panel
display(panelLayout)


# In[221]:


bookProj.uniqueQuotationsList[0].junk=True


bookProj.set_junkPhrases()
print( bookProj.uniqueQuotationsList[0].junk )
#bookProj.write_uniqueQuotationsList_to_csv()
#bookProj.read_uniqueQuotationsList_from_csv()
print( bookProj.uniqueQuotationsList[0].junk )


#.             .   set_junkPhrases()


# In[222]:


bookProj.make_dfNew()


# In[223]:


len(bookProj.dfNew)


# In[225]:


bookProj.write_dfNew_to_file()


# In[226]:


if len(bookProj.uniqueQuotationsList)>0:
    bookProj.update_all_items_with_accepted_quotations()
else:
    print("The uniqueQuotationsList is empty.")

 


# In[227]:


for i, item in enumerate(bookProj.df['Locations in A']):
    if item != []:
        print(type(bookProj.df['Locations in A'][i][0][0]))
        print(i)
        print(bookProj.df['Locations in A'][i][0][0])
        break



# In[ ]:





# In[228]:


print(len(bookProj.dfNew))


#print(bookProj.dfNew.columns)


for q in bookProj.uniqueQuotationsList:
    if q.location== [168085, 168181]:
        q.junk= True
        print(q.string)
        print(q.location)
        print(q.index)




for i in range(len(bookProj.df)):
    if not bookProj.dfNew['Locations in A'][i]==[]:
        print(bookProj.df['Locations in A'][i])

        print(bookProj.df['Locations in B'][i])

        print(bookProj.dfNew['Locations in A'][i])

        print(bookProj.dfNew['Locations in B'][i])
            #['Locations_in_B']))


# In[ ]:


bookProj.set_junkPhrases()
bookProj.read_junkPhrases_from_csv()

print(len(bookProj.junkPhrases))


# In[ ]:


print(len(bookProj.uniqueQuotationsList))


# In[ ]:


bookProj.read_data()

quotations(bookProj)
print(len(bookProj.uniqueQuotationsList))


# In[ ]:


import csv

if bookProj.uniqueQuotationsList is not None:
    pathQuotationsCSV = os.path.join(bookProj.resultsDir, "quotations.csv")
    with open(pathQuotationsCSV, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['junk', 'location', 'string', 'numMatches', 'index'])  # writing headers
        for q in bookProj.uniqueQuotationsList:
            writer.writerow([q.junk, q.location, q.string, q.numMatches, q.index])
            print(f"{q.junk} , {q.location},  {q.string}, {q.numMatches}, {q.index}")

else:
    print('bookProj.uniqueQuotationsList is none')         

    #bookProj.write_quotations_list_to_CSV()


# In[ ]:


for q in bookProj.uniqueQuotationsList[0:15]:
    q.junk= True


# In[ ]:


bookProj.write_uniqueQuotationsList_to_csv()



# In[ ]:


def read_uniqueQuotationsList_from_csv(self):
    self.uniqueQuotationsList=[]
    pathQuotationsCSV = os.path.join(self.resultsDir, "quotations.csv")
    with open(pathQuotationsCSV, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        self.uniqueQuotationsList = []
        for row in reader:
            q= quotation(self.text, row[1])
            q.junk=row[0]
            q.location=row[1]
            q.string= row[2]
            q.numMatches=int(row[3])  # Convert the integer to a string
            q.index= row[4]
            self.uniqueQuotationsList.append(q)


# In[ ]:


import itertools 

my_uniqueQuotationsList = []
pathQuotationsCSV = os.path.join(bookProj.resultsDir, "quotations.csv")
print(pathQuotationsCSV)
with open(pathQuotationsCSV, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    num_lines = sum(1 for line in reader)
    print(f'The file has {num_lines} lines.')

    #print(len(reader))
    #next(reader)  # Skip the header
    print('hello world')

    for line in itertools.islice(reader, 1, 4):
        print(line)
    print('hello world')    

    #for i,row in enumerate(reader):
    #    if i<=1:
    #        row= reader[i]
    #        print(row)       
    #    else:
   #         break
    #    q= quotation(self.text, row[1])
    #    q.junk=row[0]
    #    q.location=row[1]
    #    q.string= row[2]
    #    q.numMatches=int(row[3])  # Convert the integer to a string
    #    q.index= row[4]
    #    self.uniqueQuotationsList.append(q)


# In[ ]:


bookProj.read_uniqueQuotationsList_from_csv()



# In[ ]:


bookProj.uniqueQuotationsList[10].junk





# In[ ]:


#🗣️🚨

# using pathlib
# dataDir is the main directory of all projects of all authors 
#  


def file_exists(full_filename_string):
  filename_path = Path(full_filename_string)

  if filename_path.exists():        
    if filename_path.is_file():
      return True
    else:
      print(f"{filename_path} exists, but it is not a file.")
      return False    
  else:
    print(f"{filename_path} does not exist.")
    return False



# In[ ]:





# In[ ]:


#my_quotations = quotations(bookProj)



#bookProj.uniqueQuotationsList = my_quotations.uniqueQuotationsList



my_uniqueQuotationsList = bookProj.uniqueQuotationsList

print(len(my_uniqueQuotationsList))
for quot in my_uniqueQuotationsList:
    print(quot.string)




# In[ ]:


bookProj.write_uniqueQuotationsList_to_csv()


# In[ ]:





# In[ ]:


my_quotations = bookProj.uniqueQuotationsList


for quot in my_quotations[285:287]:
    print(quot.string)


# In[ ]:


my_quotations = bookProj.uniqueQuotationsList

quot1= my_quotations[  285]
quot2= my_quotations[  286]

compare_loc1= quot1.location
compare_loc2= quot2.location


compare_len1=compare_loc1[1]- compare_loc1[0]
compare_len2=compare_loc2[1]- compare_loc2[0]
print(quot1.string )
print(quot2.string )

print(len(quot1.string ))
print(len(quot2.string ))

print(f"{compare_loc1[0]},    {compare_loc1[1]},   {compare_len1}   ") 
print(f"{compare_loc2[0]},    {compare_loc2[1]},   {compare_len2}   ") 


# In[ ]:


# Load the text you want to find quotations from.
#bookProj.read_source()


sourceText = bookProj.pathPlainText
with open(sourceText, encoding='utf-8') as f: 
    rawText = f.read()
print(rawText)


# In[ ]:


text= bookProj.read_sourceA()

#🚨  find out: Text
#tx = Text(rawText, bookProj.projectName)    
print(text[0:400])


# In[ ]:


# Building an instance of Book_Project
# create and fill de the data frame df, reading the  JSONL file
# doing a check of the existence of all project dirs

#self.dataDir=dataDir file-exits
path = bookProj.pathJSONL

print(str(path))
if path.exists():
    # Load results as pandas dataframe
    df = pd.read_json(path, lines=True)  
else: 
    print(f"file {path}  does not exist" )




# In[ ]:


#print(tx )
# C:\Users\bdt\Documents\Data\Joyce\1922_Ulysses\Results\Joyce_1922_Ulysses_results_t2-c3-n2-m3-nostops.jsonl
#"C:\Users\bdt\Documents\Data\Joyce\1922_Ulysses\Results\Joyce_1922_Ulysses_results_t2-c3-n2-m3-nostops.jsonl"


# In[ ]:


#print(tx )
#"C:\Users\bdt\Documents\Data\Joyce\1922_Ulysses\Results\Joyce_1922_Ulysses_results_t2-c3-n2-m3-nostops.jsonl"


# In[ ]:


#print(tx )
#"/#C:\Users\bdt\Documents\Data\Joyce\1922_Ulysses\Results\Joyce_1922_Ulysses_results_t2-c3-n2-m3-nostops.jsonl"


# In[ ]:


#print(bookProj.df['Locations_in_A'])


# In[ ]:


quotations_list=bookProj.uniqueQuotationsList

print(len(quotations_list) )


# In[ ]:


uniqueQuotationsList = bookProj.uniqueQuotationsList
rawText= bookProj.text
print(len(rawText) )
print(len(uniqueQuotationsList) )


# In[ ]:


compare_string =  "Cashel Boyle O’Connor Fitzmaurice Tisdall Farrell"
#comapare_loc =



# In[ ]:





# In[ ]:


# # make a list of quoatuon obejcts
#
# make adaptions of locationsinA list and parallel to that: adaptions locationsinB list

# Make adatations in numMatches

#locations_in_A = make_list_of_locationsinA(df)
#locations_in_B = make_iist_of_locationsinB(df)


#return[new_locsA,new_locsB] 


# In[ ]:


# is adapt locationsinA en b verdwenen??non_empty_locations = [loc for loc in self.locationsInA if loc != []]
        # Flatten the list
        # Using list comprehension
#flattened_locations = [item for sublist in non_empty_locations for item in sublist]
#sorted_locations = sorted(flattened_locations)
#self.sorted_locations= sorted_locations

#print(len(sorted_locations))

#loc1 = sorted_locations[0]

        
#uniqueQuotationsList = []
#index=0
#new_quotation = quotation(self.text, loc1)
#new_quotation.index=index
#index+=1
#new_quotation.numMatches= 1
#uniqueQuotationsList.append(new_quotation)


# In[ ]:


# gets a selected set out of a quotations list of  no junk phrase  quotations
# reterns a list of no junkphrase quotations

def get_no_junk_quotations( quotations_list):
    no_junk_quotations=[]  
    for q in quotations_list:
        if not q.junk:
            no_junk_quotations.append(q)  
    return no_junk_quotations                  
                    
# gets a selected set out of a quotations list of junk phrase  quotations 
# reterns a list of junkphrase quotations
#                    
def get_junk_quotations( quotations_list):
    junk_quotations=[]  
    for q in quotations_list:
        if q.junk:
            junk_quotations.append(q)
    return junk_quotations             


# In[ ]:


jpl=get_junk_quotations(bookProj.uniqueQuotationsList)
print(len(jpl))

for jp in jpl:
    print(jp.string) 


# In[ ]:


def make_equal_string_quotations_list (compare_string, quotations_list):
    equal_quotations_list=[]
    ind_list=[]
    for index,q in enumerate(quotations_list):
        if q.string == compare_string:
            ind_list.append(index)
            equal_quotations_list.append(q)
    return  [ind_list,equal_quotations_list]         


# In[ ]:


def update_all_mutations_quotations(qlocs,locsInA_list,all_locsInB_list): 
    for i, locsInA in enumerate(locsInA_list):
        locsInB= locsInB[i]
        update_accepted_quotations(qlocs,locsInA,locsInB) 


def check_loc(loc, qlocs):
    for qloc in qlocs:
        if qloc[1]> loc[1]:
            check = False
            break
        else:
            if qloc == loc:
                check = True
                break
    return check        

def update_accepted_quotations(qlocs, locsInA, locsInB):
    
    new_locsInA= []
    
    new_locsInB = []

    if isinstance(locsInA[0], list):

        for j, item in enumerate(locsInA):
            new_item_A = []
            new_item_B = []
            if isinstance(item[0], list):
                for k, loc in enumerate(item): 
                    if check_loc(loc, qlocs):
                        new_item_A.append(loc)
                        new_item_B.append(locsInB[j,k]) 
            else: 
                loc = item 
                if check_loc(loc, qlocs):
                        new_item_A.append(loc)
                        new_item_B.append(locsInB[j,k])             

            if not new_item_A== []:
                new_locsInA.append(new_item_A)
                new_locsInB.append(new_item_B) 


    elif check_loc(locsInA[0], qlocs):
        
        new_locsInA.append(locsInA[0])
        new_locsInB.append(locsInB[0])    


    return [new_locsInA, new_locsInB]

    








    


# In[ ]:





# In[ ]:


#q = uniqueQuotationsList[0]
quotations_list = bookProj.uniqueQuotationsList
length=len(quotations_list )
print(length)

text= bookProj.text
for i,q in enumerate(quotations_list):
    h_list=quotations_list[i:length]
    result_list= make_equal_string_quotations_list(q.string,h_list)

    h1_list= result_list[1]
    h1_ind_list=  result_list[0]
    if not len(h1_list)==1:
        print(i)
        #rint(f"{i}  ,   {len(h1_list)},  {h1_list[0].string}, {h1_list[1].string}, {h1_ind_list[0]}, {h1_ind_list[1]} ")
        #print(f"{i}  ,   {h1_list[0].location},  {h1_list[1].location} ")
        string1= text[h1_list[0].location[0] : h1_list[0].location[1] ]
        print(string1 )
        string2= text[h1_list[1].location[0] : h1_list[1].location[1] ]
        print(string2 )




# In[ ]:


print(len(bookProj.text))


# In[ ]:


text= bookProj.text
quotations_list = bookProj.uniqueQuotationsList

    
def get_q_context(q, text):
    start = max(0, q.location[0]-100)  # Ensure the start index is not negative
    end = start + 200  # Display 200 characters of context around the quotation
    context = text[start:end]

    return  context

    # Create a scrollable text area widget
widget = widgets.Textarea(
    value= get_q_context(quotations_list[0], text),
    placeholder='Enter text',
    description=  'Context:',
    layout= widgets.Layout(height='400px',width ='500px', overflow_y='auto')
)




#display(widget)



# In[ ]:


#make copy df with adapted locs inA, locsin B h numMatces

#1)make_df_new

#2) use unique_quotaions_list  to build columns in dfNew

#2) write_df_new_to_file

#3) read_df_new_from_File




# In[ ]:


class filter_settings:
    def __init__(self):
        self.most_frequent =True
        self.number=100
        # type options=['All', 'Junk', 'Non-Junk']
        self.type='Non-Junk'
        self.ascending=False
        self. alphabetical= True

f_s= filter_settings()

print(f_s.most_frequent)
print(f_s.type)


# In[ ]:


from IPython.display import display


# Create a label
pre_filter_label = widgets.Label(value="Pre filter Settings")

# Create a button
most_freq_checkbox = widgets.Checkbox(description="filter by most frequently", value= f_s.most_frequent)

# Create a button
commit_button = widgets.Button(description="Use these settings")

# Create an input field for a number
number_input = widgets.IntText(value= f_s.number, description='Number:', width ="50px")

# Create a box to hold the label, button, and number input
most_freq_quoted_label = widgets.Label(value="Number of most frequently quoted: ")
# Create an input field for a number


pre_filter_box= widgets.VBox([pre_filter_label, most_freq_quoted_label, number_input])

type_radio_buttons = widgets.RadioButtons(
    options=['All', 'Junk', 'Non-Junk'],
    description='Quotation type:',
    disabled= False,
    value= f_s.type
)


first_sorting_radio_buttons = widgets.RadioButtons(
    options=['Alphabetical', 'By location'],
    description='sorting option:',
    disabled= False,
)

if f_s.alphabetical:
    first_sorting_radio_buttons.value='Alphabetical'
else:    
  first_sorting_radio_buttons.value='By location'

first_sorting_radio_buttons_box = widgets.VBox([first_sorting_radio_buttons])

    
second_sorting_radio_buttons = widgets.RadioButtons(
    options=['Ascending', 'Descending'],
    description='sorting option:',
    disabled=False
)

if f_s.ascending:
    second_sorting_radio_buttons.value='Ascending'
else:    
    second_sorting_radio_buttons.value='Descending'



second_sorting_radio_buttons_box = widgets.VBox([second_sorting_radio_buttons])


type_box = widgets.VBox([type_radio_buttons])

settings_box = widgets.VBox([pre_filter_box, type_box, first_sorting_radio_buttons_box, second_sorting_radio_buttons_box, commit_button])

# Display the box
display(settings_box)

# Define a function to run when the button is clicked
def on_button_clicked(button):
    f_s.number = number_input. value
    f_s.type = type_radio_buttons.value
    f_s.ascending = second_sorting_radio_buttons.value=='Ascending'
    f_s.alphabetical = first_sorting_radio_buttons.value=='Alphabetical'

    print(f"Button clicked. Number entered: {f_s.most_frequent},  {f_s.number}, {f_s.type}, {f_s.ascending}, {f_s.alphabetical}")
    return f_s
# Set the function to run when the button is clicked
commit_button.on_click(on_button_clicked)




# In[ ]:


from IPython.display import display, HTML

def get_q_color_context(q, text):
    start = max(0, q.location[0]-200)  # Ensure the start index is not negative
    end =  min(q.location[1]+200, len(text)-1)  # Display 200 characters of context around the quotation
    context_before = text[start:q.location[0]]
    context_quotation = text[q.location[0]:q.location[1]]
    context_after = text[q.location[1]:end]

    # Create HTML with the quotation colored red
    html = f"  {context_before}<span style='color:red;'>{context_quotation}</span>{context_after}"

    # Display the HTML
    #display(HTML(html))

    return html

def list_of_colored_context(quotations_list, text):
    result_list =  []
    for i in range(10): 
        result= get_q_color_context(quotations_list[i], text)
        result_list.append(f"<br>, {result}")
    
    # Convert the list into a single string
    list_of_colored_contexts = '<br>'.join(result_list)
    
    return list_of_colored_contexts

text= bookProj.text

sortedQuotationsList= bookProj.uniqueQuotationsList[0:20]

lines_of_colored_contexts = list_of_colored_context(sortedQuotationsList, text)

# Create a scrollable HTML widget
widget = widgets.HTML(
    value=lines_of_colored_contexts,
    placeholder='Enter text',
    description='Context:',
    layout=widgets.Layout(height='400px', overflow_y='auto')
)

#display(widget)
text= bookProj.text
list_of_colored_contexts = list_of_colored_context(sortedQuotationsList, text)
    
# Create a scrollable HTML widget
widget = widgets.HTML(
    value= lines_of_colored_contexts,
    placeholder='Enter text',
    description='Context:',
    layout=widgets.Layout(height='400px')
)

#display(widget)


from ipywidgets import Checkbox, VBox

def create_checkboxes(quotations_list, text):
    checkboxes = []
    
     # has to be rvisited auto the range

    for i in range(min(20, len(quotatations_list))): 
        html_line = get_q_color_context(quotations_list[i], text)
        checkbox = Checkbox(description=html_line, value=False, indent=False)
        checkboxes.append(checkbox)
    return checkboxes

#def create_checkboxes(quotations_list, text):
#    checkboxes = []

    
#    for i in range(min(20, len(quotatations_list))): 
#        html_line = get_q_color_context(quotations_list[i], text)
#        checkbox = Checkbox(description=html_line, value=False, indent=False)
#        checkboxes.append(checkbox)
#    return checkboxes    

def create_quotation_checkboxes(quotations_list, text):

# has to be consedered for longer list 
#
    checkboxes = []
    for i in  range(10): 
        html_line = get_q_color_context(quotations_list[i], text)
        checkbox = Checkbox(description=html_line, value=False, indent=False)
        checkboxes.append(checkbox)
    return checkboxes

def create_quotation_HBox(html_line , q ):
    if q.junk:
        descr =  'junk'
    else:
        descr = 'not junk'    

    checkbox = widgets.Checkbox(description = descr, value=q.junk, indent=False)

    checkbox.observe(lambda change: on_checkbox_change(change, checkbox, q), names='value')

    context_widget = widgets.HTML(
            value = html_line,
            placeholder='',
            description='',
            layout= widgets.Layout(height='430px', width= '1000px')
                                   )
 
    checkbox_all= widgets.Checkbox(description = "with all equal strings", value= False, indent=False)

    quotation_specs_VBox= widgets.VBox([checkbox, checkbox_all ], 
                                       layout= widgets.Layout(height='300x', width= '350px'))

    quotation_HBox = widgets.HBox([ quotation_specs_VBox, context_widget],  layout= widgets.Layout(height0='300x', width= '1000px'))


    return  quotation_HBox 




#html_line = get_q_color_context(q, text)

def on_checkbox_change(change, checkbox, q):
    if change ['name'] == 'value' and change['type'] == 'change':
        q.junk = change['new']
        save_changes_button.description = 'Save changes'
        quotations_list[q.index].junk= q.junk

 
        print(f"{q.index}, {uniqueQuotationsList[q.index].junk},   {q.string}" )
        print(f"{q.index}, {bookProj.uniqueQuotationsList[q.index].junk},   {q.string}" )

        if change['new'] == True:
           checkbox .description = 'junk'
        else:
            checkbox.description = 'not junk'
        print(f"Checkbox changed to: {change['new']}")




# Create a VBox with the checkboxes
#quotation

def make_quotation_Hboxes(quotations_list , text):
    quotation_HBoxes= [] 
    for i, q in enumerate(quotations_list):
        
        html_line = get_q_color_context(q, text)
        quotation_Hbox = create_quotation_HBox(html_line, q)

        quotation_HBoxes.append(quotation_Hbox)

    return quotation_HBoxes


quotations_boxes = make_quotation_Hboxes(sortedQuotationsList[0:10], text)

quotations_Vbox = widgets.VBox(quotations_boxes,layout= widgets.Layout(height='1200px', overflow_y='scraoll') )


# Display the VBox
display(quotations_Vbox)


save_changes_button= widgets.Button(description='Save changes', layout=widgets.Layout(width='400px')) 

def save_changes_button_clicked(button):
    bookProj.write_uniqueQuotationsList_to_csv()    
    save_changes_button.description = 'Changes saved'
    bookProj.uniqueQuotationsList = sortedQuotationsList
    return   

  
# Attach the event handler to the commit button
save_changes_button.on_click(save_changes_button_clicked)
display(save_changes_button)



# 

# In[ ]:


print(bookProj.get_junkPhrases()[0])


# In[ ]:


bookProj. write_junkPhrases_to_CSV()
    
      


# In[ ]:


print(uniqueQuotationsList[1578].junk)


# In[ ]:


def make_equal_string_quotations_list (compare_string, quotations_list):
    equal_quotations_list=[]
    ind_list=[]
    for index,q in enumerate(quotations_list):
        if q.string == compare_string:
            ind_list.append(index)
            equal_quotations_list.append(q)
    return  [ind_list,equal_quotations_list]      


# In[ ]:


def make_all_equal_string_quotations_list (quotations_list):

      all_equal_lists=[]
      
      length=len(quotations_list )
      print(length)

      text= bookProj.text
      for i,q in enumerate(quotations_list):
            h_list=quotations_list[i:length]
            h1_list= result_list[1]
            h1_ind_list=  result_list[0]
            
            equal_list= make_equal_string_quotations_list(q.string,h_list)

      return equal_list

      #h1_list= result_list[1]
      #h1_ind_list=  result_list[0]
      #if not len(h1_list)==1:
      #      print(i) 
      #      #rint(f"{i}  ,   {len(h1_list)},  {h1_list[0].string}, {h1_list[1].string}, {h1_ind_list[0]}, {h1_ind_list[1]} ")
      #      #print(f"{i}  ,   {h1_list[0].location},  {h1_list[1].location} ")
      #      string1= text[h1_list[0].location[0] : h1_list[0].location[1] ]
      #      print(string1 )
      #      string2= text[h1_list[1].location[0] : h1_list[1].location[1] ]
      #      print(string2 )
      


# In[ ]:


buffer_file_path = os.path.join(bookProj.resultsDir, 'buffer.txt')

with open(buffer_file_path, 'w') as f:
    for item in quotations_list:
        # Write each item to the file
        f.write("%s\n" % item)


# In[ ]:


# Open the buffer file in read mode
with open(buffer_file_path, 'r') as f:
    # Read each line from the file, strip the newline character, and add it to the list
    new_uniqueQuotationsList = [line.rstrip('\n') for line in f]


# In[ ]:


import os

def write_quotations_to_file(quotations_list, file_path):
    with open(file_path, 'w') as f:
        for item in quotations_list:
            if isinstance(item, quotation):  # Check if item is of type quotation
                f.write("%s\n" % item)

def read_quotations_from_file(file_path):
    with open(file_path, 'r') as f:
        quotations_list = [line.rstrip('\n') for line in f]
    return quotations_list

# Get the full path to the buffer file
buffer_file_path = os.path.join(bookProj.resultsDir, 'buffer.txt')

# Write quotations to file
write_quotations_to_file(bookProj.uniqueQuotationsList, buffer_file_path)

# Read quotations from file and rebuild uniqueQuotationsList
bookProj.uniqueQuotationsList= read_quotations_from_file(buffer_file_path)


# In[ ]:


write_quotations_to_file(quotations_list, buffer_file_path)
new_quotations_list= read_quotations_from_file(buffer_file_path)
len(new_quotations_list)


# In[ ]:


type(new_quotations_list[0])


# In[ ]:


my_quotations = bookProj.uniqueQuotationsList.copy()
bookProj.uniqueQuotationsList[0].junk= False

print(bookProj.uniqueQuotationsList[0].junk)

print(my_quotations[0].junk)

my_quotations[0].junk= True

print(my_quotations[0].junk)


print(bookProj.uniqueQuotationsList[0].junk)

#bookProj.update_uniqueQuotationsList(my_quotations)
#print(bookProj.uniqueQuotationsList[0].junk)


# In[ ]:


junk_list=[]

quotations_list[2].junk = True

for q in quotations_list:
    junk_list.append(q.junk)

for i in range(10):
    print(quotations_list[i].junk)
    print ( junk_list[i])
   






 


# In[ ]:


# Convert all booleans to strings and join them with commas
buffer_file_path = os.path.join(bookProj.resultsDir, 'junk_buffer.csv')
bool_str = ','.join(map(str, junk_list))

# Write the string to the file
with open(buffer_file_path , 'w') as f:
    f.write(bool_str)


# In[ ]:





# In[ ]:


# Open the file in read mode

def read_junk_list(buffer_file_path): 
    with open(buffer_file_path, 'r') as f:
        # Read the line from the file
        line = f.readline().strip()

    # Split the line into strings and convert each string to a boolean
    bool_list = [s == 'True' for s in line.split(',')]

    print(bool_list[0:10])
    return bool_list



junk_list=read_junk_list(buffer_file_path)

for i, bool in    enumerate(junk_list):
    quotations_list[i].junk= bool

for i, bool in    enumerate(quotations_list[0:10]):
    print(quotations_list[i].junk)




# In[ ]:


for i, q in enumerate(new_uniqueQuotationsList[0:10]):
    print( f"{i},  {q.string}")


# In[ ]:


quotations_list = uniqueQuotationsList
length=len(quotations_list )
print(length)
#for q in quotations_list[0:10]:
# print(q.string)  

for i,q in enumerate(quotations_list):
    h_list=quotations_list[i:length]

    result_list= make_equal_string_quotations_list(q.string,h_list)

    h1_list= result_list[1]
    h1_ind_list=  result_list[0]

    length1=len(h_list)
    if not len(h1_list)==1:

        print(i)
        #rint(f"{i}  ,   {len(h1_list)},  {h1_list[0].string}, {h1_list[1].string}, {h1_ind_list[0]}, {h1_ind_list[1]} ")
        #print(f"{i}  ,   {h1_list[0].location},  {h1_list[1].location} ")
        string1= text[h1_list[0].location[0] : h1_list[0].location[1] ]
        print(string1 )
        string2= text[h1_list[1].location[0] : h1_list[1].location[1] ]
        print(string2 )
      #my_list = [f" { length - length1 +j}, {q.string} " for j,q in enumerate(h1_list)]
      #my_ind_list=[f" { length - length1 +j}, {index} " for j,index in enumerate(h1_ind_list)]

      #result = ', '.join(my_list)
      #print(f"  {i}, {quotations_list[i].string},  {q.string}" for q in  my_list)
      #print(f"  {i}, {quotations_list[i].string},  { ind} " for ind in my_ind_list)


# In[ ]:


#  check if quotation is 

compare_string =  "Cashel Boyle O’Connor Fitzmaurice Tisdall Farrell"
compare_loc1= quotations_list[3783].location
compare_loc2= quotations_list[3784].location

compare_numMatches = bookProj.df['numMatches'].iloc[3784]
compare_len1=compare_loc1[1]- compare_loc1[0]
compare_len2=compare_loc2[1]- compare_loc2[0]

print(f"{compare_loc1[0]},    {compare_loc1[1]},   {compare_len1}   ") 
print(f"{compare_loc2[0]},    {compare_loc2[1]},   {compare_len2}   ") 
print(str(compare_numMatches))

print(quotations_list[3783].string)
print(quotations_list[3784].string)


# In[ ]:


print(bookProj.text[303748:303797])
print(bookProj.text[303864:303905])


# In[ ]:


def find_cases_of_a_location (i, compare_loc, locsInA):
    
    cases=[]

    if isinstance(locsInA, list):
        print("locsInA is a list")
  

        if not locsInA == []:

            if isinstance(locsInA[0], list):

                for j, item in enumerate(locsInA):
            
                    if isinstance(item[0], list):
                        dummy=0
                #     for k, loc in enumerate(item): 
                #         if loc== compare_loc:
                #             cases.append([i, j])
                    else: 
                        loc = item 
                        if loc == compare_loc:
                                cases.append([i, j])   
    else:
        print("locsInA is not a list")                                  

        #elif locsInA == compare_loc:
        #    cases.append([i, j])

        return cases

    
def find_all_cases_of_a_location(compare_loc,locsInA_list): 
    cases_list=[]
    
    for i, locsInA in enumerate(locsInA_list):
        cases = find_cases_of_a_location(i, compare_loc,locsInA) 
        if not len(cases)==0:
            cases_list.append(cases)
    
    return  cases_list

    


# In[ ]:


locsInA_list= bookProj.df['Locations in A']
print(len(locsInA_list))
# 19712

#compare_string =  "Cashel Boyle O’Connor Fitzmaurice Tisdall Farrell"
compare_loc1= quotations_list[3784].location
#compare_loc2= quotations_list[3785].location
        
        

find_all_cases_of_a_location(compare_loc1,locsInA_list)


# In[ ]:


# Define the event handler
#def handle_checkbox_click(change):
#    # Check if the checkbox is checked
#if change['new']:
#        # Update the value of the selected_quotation_scrollb#ox
#        selected_quotation_scrollbox.value = change['owner'].description
()
quotations_list = sortedQuotationsList[0:40]      



label = widgets.Label()
selected_quotation_index_label = widgets.Label("test")

selected_quotation_string_label= widgets.Label("test")

num_equal_quotations_label= widgets.Label("test")

junk_phrase_label= widgets.Label("test")

# Create a scrollable text area widget
# Create the scrollable text area widget

 
junk_button = widgets.Button(description='junk phrase')

# Define a function to handle the select button click event
def handle_junk_button_click(button):
    #selected_quotation = quotations_scrollbox.value
    junk_phrase_label.value= "Selected phrase is junk}"
    quotations_list[index].junk= True  
    
    # Find the quote that matches the selected text
    selected_quote = None

    for i,quote in enumerate(quotations_list):
        if selected_quotation in quote.string:
            selected_quote_string = quote.string
            break
    
    if selected_quote is not None:
        print(f"Selected quote: {selected_quote}.string")
    else:
        print("No matching quote found.")
    selected_quotation_string= quotations_scrollbox.value
    print(f"Selected quotation: {selected_quotation_string}")

# Attach the event handler to the select button
junk_button.on_click(handle_junk_button_click)


equal_string_quotations_list= []

equal_string_quotations_list= make_equal_string_quotations_list(sortedQuotationsList[0].string, sortedQuotationsList)[1]

equal_string_checkboxes = [widgets.Checkbox(value= False, description= q.string) for q in equal_string_quotations_list]

equal_checkboxes_vbox = widgets.VBox(equal_string_checkboxes, layout = widgets.Layout(overflow_y='auto', height='300px'))


equal_button = widgets.Button(description='show equal phrases')

def handle_equal_button_click(button, compare_string):
    equal_string_quotations_list = make_equal_string_quotations_list(compare_string, quotations_list)[1]
    for quote in equal_string_quotations_list:
        if selected_quotation in quote:
            selected_quotation_string = quote.string
            break
    
    if selected_quotation_string is not None:
        print(f"Selected quote: {selected_quotation}")
    else:
        print("No matching quote found.")
    selected_quotation_string= quotations_scrollbox.value
    print(f"Selected quotation: {selected_quotation_string}")

#equal_button.on_click(handle_equal_button_click(selected_quotation_string))

#num_equal_quotations_label
 
quotations_scrollbox = widgets.Textarea(
    value='\n  \n'.join(q.string for q in quotations_list),
    layout=widgets.Layout(height='200px'),
    disabled=True
)

selected_quotations_scrollbox = widgets.Textarea(
    value='\n  \n'.join(q.string for q in uniqueQuotationsList),
    layout=widgets.Layout(height='200px'),
    disabled=True
)


# Create a list of checkboxes, one for each quotation
checkboxes = [widgets.Checkbox(value=False, description=q.string) for q in quotations_list]

#for checkbox in checkboxes:#
#    checkbox.observe(handle_checkbox_click, 'value')

# Create a VBox to hold the checkboxes
#checkbox_vbox = widgets.VBox(checkboxes)  # Remove the extra argument 'label'

# Create a VBox to hold the checkboxes
checkbox_vbox = widgets.VBox(checkboxes, layout=widgets.Layout(overflow_y='auto', height='300px'))


checkboxes = [widgets.Checkbox(value=False, description=q.string) for q in uniqueQuotationsList[0:30]]

#for checkbox in checkboxes:#
#    checkbox.observe(handle_checkbox_click, 'value')

# Create a VBox to hold the checkboxes
#checkbox_vbox = widgets.VBox(checkboxes)  # Remove the extra argument 'label'

# Create a VBox to hold the checkboxes
checkbox_vbox = widgets.VBox(checkboxes, layout=widgets.Layout(overflow_y='auto', height='300px'))


quotation_vbox = widgets.VBox(
    [selected_quotation_index_label ,
    selected_quotation_string_label ,
    num_equal_quotations_label,
    junk_phrase_label,
    junk_button 
    
    ])

quotation_hbox= widgets.HBox([checkbox_vbox, quotation_vbox] )
display(quotation_hbox)




# Define the event handler
def make_checkbox_handler(index):
    def handle_checkbox_click(change):
        # Check if the checkbox is checked
        global selected_index

        if change['new']:
            selected_index = index
            # Update the value of the selected_quotation_scrollbox
            selected_quotation_scrollbox.value = change['owner'].description
            # Show the index of the checkbox that was checked
            label.value = f"Checkbox {index} was checked."
            selected_quotation_index_label.value = f"Checkbox {index} was checked."
            compare_string = checkboxes[index].description
            selected_quotation_string_label .value=f" quatation string:  {checkboxes[index].description}"

            num_equal_quotations = len(equal_string_quotations_list (compare_string, quotations_list))
            num_equal_quotations_label.value= f" num equal quotations: { num_equal_quotations }"


            selected_quotation_scrollbox.value = change['owner'].description
    return handle_checkbox_click

# Attach the event handler to all checkboxes


for index, checkbox in enumerate(checkboxes):
    checkbox.observe(make_checkbox_handler(index), 'value')

#quotation_hbox=widgets.HBox([ checkbox_vbox, quotation_vbox])
#display(quotation_hbox)

# Create the label widget
quotation_label = widgets.Label("Quotation text")

rawText_scrollbox = widgets.Textarea(
    value=rawText,
    layout=widgets.Layout(height='500px', width='400px'),
    disabled=True
)

selected_quotation_scrollbox = widgets.Textarea(
    value='ä quotation text',
    layout=widgets.Layout(height='500px', width='400px'),
    disabled=True)


#checkbox_hbox.children = (*checkbox_hbox.children, selected_quotation_label)

# Create the scrollbox widget for rawText
rawText_scrollbox = widgets.Textarea(
    value=rawText,
    layout=widgets.Layout(height='500px', width='400px'),
    disabled=True
)
commit_button = widgets.Button(description='Junk')

# Define the event handler
def handle_commit_button_click(button):
    # Get the current index from the label
    index = int(label.value.split(' ')[1])
    # Set the junk attribute of the quotation at the current index to True
    quotations_list[index].junk = True
    #selected_quotation_index_label.value = quotations_list[index].junk 

# Attach the event handler to the commit_button
commit_button.on_click(handle_commit_button_click)

# Create the HBox and VBox layout

# problem wruntime loop??: 


#vbox_layout2 = widgets.VBox([quotation_label, quotation_junk_label, select_button, quotations_scrollbox])
#hbox_layout = widgets.HBox([vbox_layout, rawText_scrollbox])

#hbox_layout2 = widgets.HBox([vbox_layout2, rawText_scrollbox])




# Display the panel
#display(hbox_layout2)


#
#






# In[ ]:


with open(file_path, "r") as f:
    content = f.read()

for q in content:
    print(q.string)


# In[ ]:


#quotations_list2= bookProj.unique_quotions_list


my_quotations = quotations(bookProj)
my_uniqueQuotationsList=bookProj.uniqueQuotationsList 

if hasattr(my_quotations, 'uniqueQuotationsList'):
    print(len(my_quotations.uniqueQuotationsList))
    for quot in my_quotations.uniqueQuotationsList:
        print(f"{quot.location[0]},   {quot.location[1]},    {quot.string}")



    #print(len(my_quotations))
    for quot in my_quotations.uniqueQuotationsList:
        print(f"{quot.location[0]},   {quot.location[1]},    {quot.string}")


# Create a scrollable text area widget
# Create the scrollable text area widget
quotations_scrollbox = widgets.Textarea(
    value='\n\n'.join(my_quotations.uniqueQuotationsList ),
    layout=widgets.Layout(height='200px'),
    disabled=True
)

# Create the label widget
quotation_label = widgets.Label("Quotation text")

# Create the scrollbox widget for rawText
rawText_scrollbox = widgets.Textarea(
    value=rawText,
    layout=widgets.Layout(height='500px', width='400px'),
    disabled=True
)
commit_button = widgets.Button(description='Junk')


# Create the HBox and VBox layout

vbox_layout = widgets.VBox([quotation_label,commit_button, quotations_scrollbox] )
hbox_layout = widgets.HBox([vbox_layout, rawText_scrollbox])




# Display the panel
display(hbox_layout)



quotations_scrollbox = widgets.Textarea(
    value='\n  \n'.join(quotations_list),
    layout=widgets.Layout(height='200px'),
    disabled=True
)

# Display the scrollbox


# Create a label widget
quotation_label = widgets.Label("Quotation text")

def handle_click_event(change):
    clicked_item = change['new']

    
    # Perform actions based on the clicked item
    print(f"Clicked item: {clicked_item}")
    quotation_label.value=str(clicked_item)

# Attach the event handler to the value change event of the quotations_scrollbox
quotations_scrollbox.observe(handle_click_event, 'value')

# Define a function to update the label text
def update_quotation_text(change):
    quotation_label.value = f"Selected Item: {scrollbox.value}"

# Attach the event handler to the value change event of the scrollbox
quotations_scrollbox.observe(update_quotation_text, 'value')

# Create the select button
select_button = widgets.Button(description='Select')

# Define a function to handle the select button click event
def handle_select_button_click(button):
    selected_quotation = quotations_scrollbox.value
    print(f"Selected quotation: {selected_quotation}")
    
    # Find the quote that matches the selected text
    selected_quote = None
    for quote in quotations_list:
        if selected_quotation in quote:
            selected_quote = quote
            break
    
    if selected_quote is not None:
        print(f"Selected quote: {selected_quote}")
    else:
        print("No matching quote found.")
    selected_quotation = quotations_scrollbox.value
    print(f"Selected quotation: {selected_quotation}")

# Attach the event handler to the select button
select_button.on_click(handle_select_button_click)

# Create the VBox layout with the select button and quotations scrollbox
vbox_layout = widgets.VBox([quotation_label, select_button, quotations_scrollbox])
hbox_layout = widgets.HBox([vbox_layout, rawText_scrollbox])

# Display the layout
display(hbox_layout)






# In[ ]:


df=bookProj.df


# In[ ]:


# Save as JSONL file for analysis and visualization
#🚨
df.to_json(path_or_buf=bookProj.pathJSONL, orient='records', lines=True)


# 
# # Drop phrases

# In[ ]:


import itertools
# Tally matches

# Calculate length of source text

#print(bookProj.text)

textALength = len(rawText)
print(textALength)

# Make an empty array the size of the text

tally = np.zeros(textALength)
#tally = [0] * textALength

# Read the matched locations from the results dataset, and literally evaluate them into lists. 

locationsInA = df['Locations in A']

# Tally up every time a letter in the text is quoted. 
for article in locationsInA: 
    for locRange in article: 
         for i in range(locRange[0], min(locRange[1]+1, len(tally))):
                tally[i] += 1


# In[ ]:


#table of tally



# In[ ]:


# make a visualrepresentation of tally



# In[ ]:


non_empty_locations = [loc for loc in locationsInA if loc != []]
# Flatten the list

# Using list comprehension
flattened_locations = [item for sublist in non_empty_locations for item in sublist]

#print(flattened_locations)
sorted_locations = sorted(flattened_locations)
print(sorted_locations)

# Using itertools.chain.from_iterable()

#unique_locations = list(set(tuple(loc) for loc in flattened_locations))



unique_locations = []
loc1=[]
for loc in sorted_locations:
    if loc != loc1: 
        loc1=loc 
        unique_locations.append(loc1)
print(unique_locations)

print(len(unique_locations) )


# In[ ]:


for quot in bookProj.uniqueQuotationsList:
    print(quot.string)




# In[ ]:





# In[ ]:


import pandas as pd
# Calculate the frequencies and bins

# Convert sorted_locations to a pandas Series


series = pd.Series(sorted_locations)

# Create the frequency table
frequency_table = series.value_counts().reset_index()

# Rename the columns
frequency_table.columns = ['Value', 'Frequency']

# Print the frequency table
print(frequency_table)


# In[ ]:


quotations_list = [rawText[loc[0]:loc[1]+1] for loc in unique_locations]

for i in range(len(quotations_list)):
    print (quotations_list[i] )





# In[ ]:


options = []  # Define the variable 'options' with an appropriate value.
for quot in bookProj.uniqueQuotationsList:
    print(quot.string)


uniqueQuotationsList = bookProj.uniqueQuotationsList


for quote in uniqueQuotationsList:
    print(f"Attributes of quote:")
    for attr in dir(quote):
        if not attr.startswith('__'):
            value = getattr(quote, attr)
            print(f"{attr}: {value}")







#for q in uniqueQuotationsList:
#    print(q.text)

# Check if uniqueQuotationsList is iterable
#if isinstance(uniqueQuotationsList, (list, tuple, set)):
#    quotations_textarea = widgets.Textarea(
#        value='\n\n'.join(quot.string for quot in uniqueQuotationsList),
#        layout=widgets.Layout(height='200px'),
#        disabled=True
#    )

#    quotations_scrollbox = widgets.Textarea(
#        value='\n  \n'.join(q.string for q in uniqueQuotationsList),
#        options=[],
#        layout=widgets.Layout(height='200px'),
#        disabled=True
#    )
#else:
#    print("uniqueQuotationsList is not iterable.")

#quotations_textarea = widgets.Textarea(
#    value='\n\n'.join(quot.string for quot in uniqueQuotationsList),
#    layout=widgets.Layout(height='200px'),
#    disabled=True
#)


#quotations_scrollbox = widgets.Textarea(
#            value='\n  \n'.join(q.string for q in uniqueQuotationsList),
#            options = [],
#            layout = widgets.Layout(height='200px'),
#            disabled=True
#)

#rawText_scrollbox = widgets.Textarea(
#    value = bookProj.text,
#    layout = widgets.Layout(height ='400px', width = '600px'),
#    disabled = True
)
# Attach the event handler to the value change event of the quotations_scrollbox




# In[ ]:





# In[ ]:


print(bookProj.text[0:400])


# In[ ]:


proj_uniqueQuotationsList5 = bookProj.uniqueQuotationsList[0:100]
text= bookProj.text

def main():
    root = tk.Tk()
    root.title('Scrollable radiobutton list')
    root.geometry("1500x1000")
    tabs = ttk.Notebook(root)
    tabs.pack(fill = "both")
    scrollable_radiobutton_list_frame = ttk.Frame(tabs)
    tabs.add(scrollable_radiobutton_list_frame, text = "Scrollable radiobutton list")
    my_checker = Quotations_Window(window = scrollable_radiobutton_list_frame)
    root.mainloop()
    
class Quotations_Window:
    def __init__(self, window):
        self.main_window = window
        self.mainframe = ttk.Frame(self.main_window, padding='15 3 12 12')
        self.mainframe.grid(column=0, row=0, sticky="W, E, N, S")

        self.file_choice = tk.StringVar()
        self.contents_list = list()
        
        self.display_folder_btn.grid(row=0, column=0)

        self.display_folder_btn = ttk.Button(self.mainframe, text="Display list of choices", width=20)
        self.display_folder_btn.grid(row=1, column=0, columnspan=2)
        self.display_folder_btn.bind("<Button-1>", self.list_folder_contents)

        self.folder_contents_canvas = tk.Canvas(self.mainframe)
        self.scroll_y = tk.Scrollbar(self.folder_contents_canvas, orient="vertical")
        self.scroll_y.pack(fill='y', side='right')
        self.folder_contents_canvas.grid(row=2, column=0, columnspan=2)
        self.folder_contents_frame = tk.Text(self.folder_contents_canvas, height=7, width=50,
                                             yscrollcommand=self.scroll_y.set)
        self.folder_contents_frame.pack(side="top", fill="x", expand=False, padx=20, pady=20)

        self.text_scrollbox = tk.Scrollbar(self.mainframe)
        self.text_scrollbox.pack(side="right", fill="y")

        self.text_box = tk.Text(self.mainframe, yscrollcommand=self.text_scrollbox.set)
        self.text_box.pack(side="right", fill="both", expand=False)

        self.text_scrollbox.config(command=self.text_box.yview)


    def list_folder_contents(self, event):
        try:
            self.contents_list = [q.string for q in proj_uniqueQuotationsList5]

            contents_dict = dict()
            self.folder_contents_frame.delete(1.0, 'end')
            counter = 0
            for i in self.contents_list:
                contents_dict[str(counter + 1)] = i
                counter += 1
            for (text, value) in contents_dict.items():
                ttk.Radiobutton(self.folder_contents_frame, text=value, variable=self.file_choice, value=text,
                                style="TRadiobutton").grid(column=0, columnspan=2, sticky=tk.W)
            self.scroll_y.config(command=self.folder_contents_frame.yview)

            self.text_box.delete(1.0, 'end')
            self.text_box.insert('end', bookProj.text)

        except Exception as exc:
            print(exc)
             
  

class Quotations_Window:
    def __init__(self, window):
        # use text as the text to display in the text box
        self.text =text
        self.main_window = window
        self.mainframe = ttk.Frame(self.main_window, padding = '15 3 12 12')
        self.mainframe.grid(column = 0, row = 0, sticky = "W, E, N, S")

        self.file_choice = tk.StringVar()
        self.contents_list = list()
 
     
        self.display_folder_btn = ttk.Button(self.mainframe, text = "Display list of choices", width = 20)
        self.display_folder_btn.grid(row = 0, column = 0, columnspan = 2)
        #self.display_folder_btn.pack(side='top')
        self.display_folder_btn.bind("<Button-1>", self.list_folder_contents)

        self.folder_contents_canvas = tk.Canvas(self.mainframe)
        self.scroll_y = tk.Scrollbar(self.folder_contents_canvas, orient="vertical")
        self.scroll_y.pack(fill = 'y', side = 'right')
        self.folder_contents_canvas.grid(row=0, column = 0, columnspan = 2)
        self.folder_contents_frame = tk.Text(self.folder_contents_canvas, height = 30, width = 50, yscrollcommand = self.scroll_y.set)
        self.folder_contents_frame.pack(side = "top", fill = "x", expand = False, padx = 20, pady = 20)

        # create a new frame for the new folder
        self.new_folder_frame = ttk.Frame(self.mainframe)
        self.new_folder_frame.grid(column=3, row=0, sticky="W, E, N, S")

        # create a new canvas in the new frame
        self.new_folder_canvas = tk.Canvas(self.new_folder_frame)
        self.new_folder_canvas.grid(row=2, column=0, columnspan=2)
# Create a frame





    def list_folder_contents(self, event):
        try:
            #self.contents_list = ['A dictum nulla auctor id.', 'A porttitor diam iaculis quis.', 'Consectetur adipiscing elit.', \
            #                      'Curabitur in ante iaculis', 'Finibus tincidunt nunc.', 'Fusce elit ligula', \
            #                      'Id sollicitudin arcu semper sit amet.', 'Integer at sapien leo.', 'Lorem ipsum dolor sit amet', \
            #                      'Luctus ligula suscipit', 'Nam vitae erat a dolor convallis', \
            #                      'Praesent feugiat quam ac', 'Pretium diam.', 'Quisque accumsan vehicula dolor', \
            #                      'Quisque eget arcu odio.', 'Sed ac elit id dui blandit dictum', 'Sed et eleifend leo.', \
            #                      'Sed vestibulum fermentum augue', 'Suspendisse pharetra cursus lectus', 'Ultricies eget erat et', \
            #                      'Vivamus id lorem mi.']
            self.contents_list = [ q.string for q in proj_uniqueQuotationsList5[0:100] ]

            contents_dict = dict()
            self.folder_contents_frame.delete(1.0, 'end')
            counter = 0
            for i in self.contents_list:
                contents_dict[str(counter+1)] = i
                counter+=1
            for (text, value) in contents_dict.items():
                #self.folder_contents_frame.insert(1.0, text+"\t"+value+"\n")
                ttk.Radiobutton(self.folder_contents_frame, text = value, variable = self.file_choice, value = text, style = "TRadiobutton").grid(column = 0, columnspan = 2, sticky = tk.W)
            self.scroll_y.config(command = self.folder_contents_frame.yview)

        except Exception as exc:
            print(exc)
            
    
     
if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


len(bookProj.unique_quotions_list)



# In[ ]:


bookProj.unique_quotions_list


# In[ ]:


proj_quotations=bookProj.unique_quotions_list
print([quot.string for quot in proj_quotations])


# In[ ]:


proj_quotations=bookProj.uniqueQuotationsList[0:100]

def main():
    root = tk.Tk()
    root.title('Scrollable radiobutton list')
    root.geometry("500x600")
    tabs = ttk.Notebook(root)
    tabs.pack(fill = "both")
    scrollable_radiobutton_list_frame = ttk.Frame(tabs)
    tabs.add(scrollable_radiobutton_list_frame, text = "Scrollable radiobutton list")
             
    my_checker = Quotations_Window(window = scrollable_radiobutton_list_frame)
    root.mainloop()

class Quotations_Window:
    def __init__(self, window):
        self.main_window = window
        self.mainframe = ttk.Frame(self.main_window, padding='15 3 12 12')
        self.mainframe.grid(column=0, row=0, sticky="W, E, N, S")

        self.file_choice = tk.StringVar()
        self.contents_list = list()

        self.display_folder_btn = ttk.Button(self.mainframe, text="Display list of choices", width=20)
        self.display_folder_btn.grid(row=1, column=0, columnspan=2)
        self.display_folder_btn.bind("<Button-1>", self.list_folder_contents)

        self.folder_contents_canvas = tk.Canvas(self.mainframe)
        self.scroll_y = tk.Scrollbar(self.folder_contents_canvas, orient="vertical")
        self.scroll_y.pack(fill='y', side='right')
        self.folder_contents_canvas.grid(row=2, column=0, columnspan=2)
        self.folder_contents_frame = tk.Text(self.folder_contents_canvas, height=7, width=50,
                                             yscrollcommand=self.scroll_y.set)
        self.folder_contents_frame.pack(side="top", fill="x", expand=False, padx=20, pady=20)

        self.text_scrollbox = tk.Scrollbar(self.mainframe)
        self.text_scrollbox.grid(row=2, column=3, sticky="NS")
        self.text_area = tk.Text(self.mainframe, height=7, width=50, yscrollcommand=self.text_scrollbox.set)
        self.text_area.grid(row=2, column=2, padx=20, pady=20)
        self.text_scrollbox.config(command=self.text_area.yview)

    def list_folder_contents(self, event):
        try:
            #self.contents_list = ['A dictum nulla auctor id.', 'A porttitor diam iaculis quis.', 'Consectetur adipiscing elit.', \
            #                      'Curabitur in ante iaculis', 'Finibus tincidunt nunc.', 'Fusce elit ligula', \
            #                      'Id sollicitudin arcu semper sit amet.', 'Integer at sapien leo.', 'Lorem ipsum dolor sit amet', \
            #                      'Luctus ligula suscipit', 'Nam vitae erat a dolor convallis', \
            #                      'Praesent feugiat quam ac', 'Pretium diam.', 'Quisque accumsan vehicula dolor', \
            #                      'Quisque eget arcu odio.', 'Sed ac elit id dui blandit dictum', 'Sed et eleifend leo.', \
            #                      'Sed vestibulum fermentum augue', 'Suspendisse pharetra cursus lectus', 'Ultricies eget erat et', \
            #                      'Vivamus id lorem mi.']
            self.contents_list = [ q.string for q in proj_quotations.uniqueQuotationsList]

            contents_dict = dict()
            self.folder_contents_frame.delete(1.0, 'end')
            counter = 0
            for i in self.contents_list:
                contents_dict[str(counter+1)] = i
                counter+=1
            for (text, value) in contents_dict.items():
                #self.folder_contents_frame.insert(1.0, text+"\t"+value+"\n")
                ttk.Radiobutton(self.folder_contents_frame, text = value, variable = self.file_choice, value = text, style = "TRadiobutton").grid(column = 0, columnspan = 2, sticky = tk.W)
            self.scroll_y.config(command = self.folder_contents_frame.yview)

        except Exception as exc:
            print(exc)


#-----------------------------------------


# In[ ]:


proj_quotations=bookProj.uniqueQuotationsList[0:100]

def main():
    root = tk.Tk()
    root.title('Scrollable radiobutton list')
    root.geometry("1500x1000")
    tabs = ttk.Notebook(root)
    tabs.pack(fill = "both")
    scrollable_radiobutton_list_frame = ttk.Frame(tabs)
    tabs.add(scrollable_radiobutton_list_frame, text = "Scrollable radiobutton list")
    tabs.add(scrollable_radiobutton_list_frame, text = "second Scrollable radiobutton list")
             
    my_checker = Quotations_Window(window = scrollable_radiobutton_list_frame)

  

    # Place label1 in row 0, column 0
    #label1.grid(row=0, column=0)

    # Place label2 in row 0, column 1
    #label2.grid(row=0, column=1)

    # Place label3 in row 1, column 0, and make it span 2 columns
    #label3.grid(row=1, column=0, columnspan=2)

    tabs2 = ttk.Notebook(root)
    tabs2.pack(fill = "both")
    my_frame = ttk.Frame(tabs2)
    label1 = tk.Label(my_frame, text="My Label")


    tabs2.add(my_frame, text = "my list")

    tabs2.add(my_frame, text = "my list")
    #tabs2.add(scrollable_radiobutton_list_frame, text = "My Scrollable radiobutton list")

    root.mainloop()
    
class Quotations_Window:
    def __init__(self, window):
        self.main_window = window
        self.mainframe = ttk.Frame(self.main_window, padding='15 3 12 12')
        self.mainframe.grid(column=0, row=0, sticky="W, E, N, S")

        self.file_choice = tk.StringVar()
        self.contents_list = list()

        self.display_folder_btn = ttk.Button(self.mainframe, text="Display list of choices", width=20)
        self.display_folder_btn.grid(row=1, column=0, columnspan=2)
        self.display_folder_btn.bind("<Button-1>", self.list_folder_contents)

        self.folder_contents_canvas = tk.Canvas(self.mainframe)
        self.scroll_y = tk.Scrollbar(self.folder_contents_canvas, orient="vertical")
        self.scroll_y.pack(fill='y', side='right')
        self.folder_contents_canvas.grid(row=4, column=0, columnspan=2)
        self.folder_contents_frame = tk.Text(self.folder_contents_canvas, height=7, width=50,
                                             yscrollcommand=self.scroll_y.set)
        self.folder_contents_frame.pack(side="top", fill="x", expand=False, padx=20, pady=20)

        #self.text_scrollbox = tk.Scrollbar(self.mainframe)
        #self.text_scrollbox.grid(row=2, column=3, sticky="NS")
        #self.text_area = tk.Text(self.mainframe, height=7, width=50, yscrollcommand=self.text_scrollbox.set)
        #self.text_area.grid(row=2, column=2, padx=20, pady=20)
        #self.text_scrollbox.config(command=self.text_area.yview)

        #self.text_area.insert(tk.END, bookProj.text)


    def list_folder_contents(self, event):
        try:
            self.contents_list = [q.string for q in proj_quotations]

            contents_dict = dict()
            self.folder_contents_frame.delete(1.0, 'end')
            counter = 0
            for i in self.contents_list:
                contents_dict[str(counter + 1)] = i
                counter += 1
            for (text, value) in contents_dict.items():
                ttk.Radiobutton(self.folder_contents_frame, text=value, variable=self.file_choice, value=text,
                                style="TRadiobutton").grid(column=0, columnspan=2, sticky=tk.W)
            self.scroll_y.config(command=self.folder_contents_frame.yview)

        except Exception as exc:
            print(exc)
   


if __name__ == '__main__':
    main()


# In[ ]:


# how many times is quotation quoted?
from tkinter import scrolledtext

proj_quotations=bookProj.uniqueQuotationsList[0:5]
text= bookProj.text


# In[ ]:


def main():
    root = tk.Tk()
    root.title('Scrollable radiobutton list')
    root.geometry("1500x1000")
    root.mainframe = ttk.Frame(root, padding='15 3 12 12')
    root.mainframe.rowconfigure(0, weight = 1 )
    root.mainframe.rowconfigure(1, weight = 1 )
    root.mainframe.columnconfigure(0, weight = 1 )
    root.mainframe.columnconfigure(1, weight = 1 )     

    scrollable_radiobutton_list_frame = ttk.Frame(root)
    scrollable_radiobutton_list_frame.grid(row=0, column=0, sticky="e")

    scrollable_text_frame = ttk.Frame(root.mainframe)
    scrollable_text_frame.grid(row=0, column=1, sticky="w")

    my_text_frame = ttk.Frame(root.mainframe)
    my_text_frame.grid(row=0, column=1, sticky="w")

    my_checker = Quotations_Window(window = scrollable_radiobutton_list_frame)
    my_text = Text_Window(window = my_text_frame)

    label2 = tk.Label(root.mainframe , text="SourcA ")
    label2.grid(row=1, column=0)

    label3 = tk.Label(root.mainframe, text="something")
    label3.grid(row=1, column=1)

    st1 = scrolledtext.ScrolledText(root, width=30, height=10)
    st1.insert('end', bookProj.text)
    st1.grid(row=2, column=0)

    st2 = scrolledtext.ScrolledText(root, width=30, height=10)
    st2.grid(row=2, column=6)

    root.mainloop()    

    
class Quotations_Window:

    def junk(self, event):

        print(dir(self.file_choice.get()))
        return

    def __init__(self, window):
        self.main_window = window
        self.mainframe = ttk.Frame(window, padding='15 3 12 12')
        self.mainframe.rowconfigure(0, weight = 1 )
        self.mainframe.rowconfigure(1, weight = 1 )
        self.mainframe.columnconfigure(0, weight = 1 )
        self.mainframe.columnconfigure(1, weight = 1 )        

        self.mainframe.grid(column=0, row=0, sticky="w")

        self.file_choice = tk.StringVar()
        self.contents_list = list()

        self.display_folder_btn = ttk.Button(window,
                         text="Display list of choices (click a radiobutton)", 
                         width=40)

        self.display_folder_btn.grid(row=1, column=0, columnspan=1)
        self.display_folder_btn.bind("<Button-1>", self.list_folder_contents)

        
        self.display_folder_btn2 = ttk.Button(window, text="Dispel junk phrase", width=20)
        self.display_folder_btn2.grid(row=1, column=2, columnspan=1)
        self.display_folder_btn2.bind("<Button-1>", self.junk)

        self.folder_contents_canvas = tk.Canvas(self.mainframe)
        self.scroll_y = tk.Scrollbar(self.folder_contents_canvas, orient="vertical")
        self.scroll_y.pack(fill='y', side='right')
        self.folder_contents_canvas.grid(row=4, column=0, columnspan=2)
        self.folder_contents_frame = tk.Text(self.folder_contents_canvas,  width=50, height=10,
                                             yscrollcommand=self.scroll_y.set)

        self.folder_contents_frame.pack(side="bottom", fill="x", expand=False, padx=20, pady=20)

        self.contents_list = [q.string for q in proj_quotations]

        contents_dict = dict()

        self.folder_contents_frame.delete(1.0, 'end')

        counter = 0
        for i in self.contents_list:
            contents_dict[str(counter + 1)] = i
            counter += 1

        for (text, value) in contents_dict.items():
            ttk.Radiobutton(self.folder_contents_frame, text=value, variable=self.file_choice, value=text,
                            style="TRadiobutton").grid(column=0, columnspan=1, sticky= "w")
        self.scroll_y.config(command=self.folder_contents_frame.yview)
        
    def list_folder_contents(self, event):
        try:
            self.contents_list = [q.string for q in proj_quotations]

            contents_dict = dict()
            self.folder_contents_frame.delete(1.0, 'end')
            counter = 0
            for i in self.contents_list:
                contents_dict[str(counter + 1)] = i
                counter += 1
            for (text, value) in contents_dict.items():
                ttk.Radiobutton(self.folder_contents_frame, text=value, variable=self.file_choice, value=text,
                                style="TRadiobutton").grid(column=0, columnspan=1, sticky= "w ")
            self.scroll_y.config(command=self.folder_contents_frame.yview)

        except Exception as exc:
            print(exc)
 
class Text_Window:
    def __init__(self, window):
        self.main_window = window
        self.mainframe = ttk.Frame(window, padding='15 3 12 12')
        self.mainframe.rowconfigure(0, weight = 1 )
        self.mainframe.rowconfigure(1, weight = 1 )
        self.mainframe.columnconfigure(0, weight = 1 )
        self.mainframe.columnconfigure(1, weight = 1 )        

        self.mainframe.grid(column=0, row=0, sticky="W, E")

        self.file_choice = tk.StringVar()
        self.contents_list = list()

        self.display_folder_btn = ttk.Button(window, text="Display text", width=20)
        self.display_folder_btn.grid(row=1, column=0, columnspan=2)
        # self.display_folder_btn.bind("<Button-1>", self.list_folder_contents)

        self.folder_contents_canvas = tk.Canvas(window)
        self.scroll_y = tk.Scrollbar(self.folder_contents_canvas, orient="vertical")
        self.scroll_y.pack(fill='y', side='right')
        self.folder_contents_canvas.grid(row=0, column=0, columnspan=2)
        self.folder_contents_frame = tk.Text(self.folder_contents_canvas, height=50, width=150,
                                             yscrollcommand=self.scroll_y.set)
        self.folder_contents_frame.pack(side="top", fill="x", expand=False, padx=20, pady=20)

        self.contents_list = text

        self.scroll_y.config(command=self.folder_contents_frame.yview)
        self.folder_contents_frame.delete('1.0', 'end')

        self.folder_contents_frame.insert('end',text)

 
      


if __name__ == '__main__':
    main()


# In[ ]:


# Specify the range of frequencies to examine (e.g. 0 to 10 for top 10 most frequent)

freqUpper = 0
freqLower = 50


# In[ ]:


# Identify highest frequencies in descending order
topFreqs = sorted(set(tally), reverse=True)[freqUpper:freqLower]

print(topFreqs)


# In[ ]:


# Make list of all indices matching the specified frequencies

quotedRange = []

for f in topFreqs:
    quotedRange.append(np.where(tally == f)[0].tolist())


# In[ ]:


# Split sublists at non-consecutive indices (i.e. multiple quoted passages coincidentally with the same frequency)

res = []
tmp = []
prv = quotedRange[0][0]
for r in quotedRange:
    for l in r:
        if l-prv > 1:
            res.append(tmp)
            tmp = []
        tmp.append(l)
        prv = l
    res.append(tmp)


# In[ ]:


# Print frequently quoted passages with some context left and right

for n in range(len(res)):
    print(f"""
    {rawText[res[n][0]-100:res[n][0]]}
    \033[1m{rawText[res[n][0]:res[n][-1]]}\033[0m
    {rawText[res[n][-1]:res[n][-1]+100]}
    ---""")


# In[ ]:


# ACTION: specify a phrase to drop here

dropPhrase = "Stately, plump Buck Mulligan"
#"Mrs. Dalloway said she would buy the flowers herself"


# In[ ]:


# Check location(s) of phrase

import re
from setuptools import setup

phraseIndices = []

for match in re.finditer(dropPhrase, rawText, re.IGNORECASE):
    startIndex = match.start()
    endIndex = match.end()
    indexTuple = (startIndex, endIndex)
    phraseIndices.append(indexTuple)
    print(f"""Matched phrase at {startIndex}:{endIndex}\n
    {rawText[startIndex-100:startIndex]}\033[1m{rawText[startIndex:endIndex]}\033[0m{rawText[endIndex:endIndex+100]}""")


# In[ ]:


print(phraseIndices)


# In[ ]:


# NOT YET WORKING

# Find "Locations in A" that contain any tuple from phraseIndices

df2 = df.explode(['Locations in A', 'Locations in B'])

df2[df2["Locations in A"].isin(phraseIndices)]


# In[ ]:


# Explode lists of matches to be new entry each

for row in df['Locations in A']:
    for tuple in row:
        if tuple ==[0, 52]:
            print("Match detected!")
        #else:
           # print("No matches detected!")


# In[ ]:


# Detect character ranges in Locations in A (+-1); report number of hits


# In[ ]:


# Delete character ranges from Locs in A and B
# Append string to existing list; save as csv; coded to work repeatedly as new phrases added


# In[ ]:


# Save results jsonl with _phrasesdropped; coded to work repeatedly

