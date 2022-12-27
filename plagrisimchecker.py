import numpy as np
import glob
import os

def CodeClause(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
 
    mm= np.zeros ((size_x, size_y)) 
 
    for x in range(size_x):
        mm [x, 0] = x 
    for y in range(size_y):
        mm [0, y] = y 
    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]: 
                mm[x,y] = min(
                    mm[x-1, y] + 1,
                    mm[x-1, y-1],
                    mm[x, y-1] + 1
                )
 
            else:         
                mm [x,y] = min(
                    mm[x-1,y] + 1,
                    mm[x-1,y-1] + 1,
                    mm[x,y-1] + 1
                )
    return (pp[size_x - 1, size_y - 1])
choice = int(input("Press 1 for comparing folder with masterfile\nPress 2 to check for plagiarism in two files\nPress 3 to check for plagiarism in all files in folder\n"))
 
k=0 
 
if (choice == 1) :
 
 
  plag = int(input("Enter the percentage of plagiarism allowed\n"))
  path1 = input("Enter the path of the folder to scan:\n")
  os.chdir(path1)
  myFiles = glob.glob('*.txt')
  print("\nThe text files available are :\n")
  print(myFiles)
 
  path = input("\nEnter the masterfile path (not in the same folder):\n")
  with open(path, 'r') as file:
      data = file.read().replace('\n', '')
      str1=data.replace(' ', '')
 
  print("\nPlagiarised files are :")
  for i in range (0,len(myFiles)) :
    with open(myFiles[i], 'r') as file:
        data = file.read().replace('\n', '')
        str2=data.replace(' ', '')
    if(len(str1)>len(str2)):
        length=len(str1)
    else:
        length=len(str2)
    
    n = 100-round((CodeClause (str1,str2)/length)*100,2)

    if (n>plag):
      print(path,"and",myFiles[i],n,"% plagiarised")
      k = k+1
 
  if (k==0):
    print("No plagiarised files")
 
elif (choice == 2) :
 
   plag = int(input("Enter the percentage of plagiarism allowed\n"))
   path2 = input("Enter the path of the first file to scan:\n")
   path3 = input("Enter the path of the second file to scan:\n")
 
   with open(path2, 'r') as file:
     data = file.read().replace('\n', '')
     str1=data.replace(' ', '')
 
   with open(path3, 'r') as file:
     data = file.read().replace('\n', '')
     str2=data.replace(' ', '')
 
   if(len(str1)>len(str2)):
        length=len(str1)
 
   else:
       length=len(str2)
 
   n = 100-round((CodeClause (str1,str2)/length)*100,2)
   
   if (n>plag):
     print("\nFor the files",path2,"and",path3,n,"% similarity")
   else :
     print("\nSimilarities are below the given level") 
        
elif (choice == 3) :
 
  plag = int(input("Enter the percentage of plagiarism allowed\n"))
  path1 = input("Enter the path of the folder to scan:\n")
  os.chdir(path1)
  myFiles = glob.glob('*.txt') 
  print("\nThe text files available are :\n")
  print(myFiles)
  print("\n")
 
  for i in range (0,len(myFiles)) :
    for j in range(i,len(myFiles)) :
 
      with open(myFiles[i], 'r') as file:
          data = file.read().replace('\n', '')
          str1=data.replace(' ', '')
 
      with open(myFiles[j], 'r') as file:
          data = file.read().replace('\n', '')
          str2=data.replace(' ', '')
 
      if(len(str1)>len(str2)):
          length=len(str1)
      else:
          length=len(str2)
      if (myFiles[i] != myFiles[j]):
    
        n = 100-round((CodeClause(str1,str2)/length)*100,2)
        if(n>plag):
          print("For the files",myFiles[i],"and",myFiles[j],n,"% plagiarised\n")         
          k = k+1
  
  if k == 0:
    print("No documents are plagiarised")
else :
  print("Enter valid Input")
