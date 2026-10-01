import os
print(os.getcwd())#this will print the current working directory
#C:\Users\LENOVO\OneDrive\PYTHON LEARNING
print(os.listdir())#this will print the list of all files and folders in the current working 
'''['day-01', 'day-02', 'day-03', 'day-04', 'day-05', 'day-06', 'day-07', 'day-08', 'day-09', 'day-10',
 'day-11', 'day-12', 'day-13', 'day-14', 'day-15', 'day-16', 'day-17', 'day-18', 'day-19']'''
#os.mkdir("newfolder")#this will create a new folder in the current working directory
#os.makedirs("newfolder1/newfolder2")#this will create a new folder in the current working directory and also create a new folder inside it
print(os.path.exists("day-18"))#this will check if the file exists or not and return True or False
print(os.path.isfile("day-18"))#this will check if the file is a file or not and return True or False
print(os.path.isdir("day-18"))#this will check if the file is a directory or not and return True or False   