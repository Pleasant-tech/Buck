import sys
import json 
import os
import shlex

# Creates the Bucket class 
class Bucket: 
  def __init__(self,name,executor,commandList,description):
    self.name = name
    self.executor = executor
    self.commandList = commandList
    self.description = description
    self.count = 0
    
  #Increments the count property 
  def increment(self):
    self.count += 1


# Creates a New Bucket
def createBucket():
  print(' >> Howdy! Create A New Bucket ')
  
  # Accept inputs from User
  name = input("\n Name : ")
  preCmds = (input ("\n Command's : "))
  cmds = preCmds.split(',')
  executor = str(input("\n Executor: ")) 

      #print ("\n")
      #print(" >> uh oh, a bucket with the exeutor '"+ executor + "' already exists, try again with a different executor.
  detail = str(input("""\n Description: """))
    
  # Instantiate an object of the class with data from input
  data = Bucket(name,executor,cmds,detail)
  
  # Load data object into a new object (spaghetti code❗)
  newData = {
    "name": data.name,
    "executor":data.executor,
    "buck_list":data.commandList,
    "description":data.description,
        "count":data.count
  }
  
   # Coverts object to Json 
  final = json.dumps(newData)
  
   # Write Json to a Json Data File
  
  with open('data.json','a') as f:
    other= '\n'+final+', \n'
    f.write(other)
    f.close()

   # Sucess Message
  print('\n >> yay! it is done ')
  print (f"\n >> Try it out 'buck {data.executor}' ")
  
    # End Process
  sys.exit()
    
#List out buckets
def listBucket():
  
   # Write Json to a Json Data File
 
  #Read data 
  with open('data.json', 'r') as f:
    data = f.read()
    f.close()
  
  # Modifies Data 
  otherData = '{ "bucket" : [' + data + '{} ] } '
    
  #Coverts Data To Json
  jsonData = json.loads(otherData)
   
  # Prints Data To user
  print (' >> Here you go : \n')
  print(json.dumps(jsonData,indent=2))
 
  
# Check if command is cd
def is_cd(command: str) -> bool:
  command_split = shlex.split(command)
  #return command_split[0] == "cd" 
  # this returns True if command is cd or False if not
  
  
# Runs commands if is_cd == True
def run_command(command: str) -> int:
  if is_cd(command):
    split_command = shlex.split(command)
    directory_to_change = ' '.join(split_command[1:])
    os.chdir(directory_to_change)
  else: 
    os.system(command)

#Run Commands From Bucket
def run(arg):
  
  # Fetch Data
 
  with open('data.json', 'r') as f:
    preData = f.read()
    f.close()
    
  
  
  
  # Modify Data
  Datta = preData[:-3]
  otherData = '{ "bucket" : [' + Datta + '] } '
  
 # Coverts modified data to json
  data = json.loads(otherData)
  
  
  
  # Logic
  for i in data['bucket']:
    response = i.get('executor')
    
    
    if arg[1] in response:
      
      buck = i.get('buck_list')
       
      
      if len(arg) > 2 :
        for i in buck:
          #  print (cmd)
          if '$' in i:
            
            cmd = i
            newCmd = cmd.replace('$',arg[2])
     
            for i in range(len(buck)):
              if buck[i] == cmd:
                buck[i] = newCmd
        for i in buck:
          run_command(i)
        
        if len(buck) == 1 :
          print('>> Done! executed 1 command.')
          
        else:
          print('>> Done! executed '+ str(len(buck)) + ' commands.')
          
      else:
        for i in buck:
        
          if '$' in i:
            print(">> This command takes in an extra argument -'" + arg[1] + " <extra argument>'")
            sys.exit()
          
        for i in buck:
          run_command(i)
        
        if len(buck) == 1 :
          print('>> Done! executed 1 command.')
        else:
          print('>> Done! executed '+ str(len(buck)) + ' commands.')
        
    
   # if arg[1] not in response:
     # print('No bucket ' + arg[1])
    
# Main Function

  
  

def main(arg=sys.argv):
  args = ['--create','-c','--list','-l']
  if len(arg) == 1:
    print ('>> Please pass an argument in')
    
  elif arg[1] == '--create' or arg[1] == '-c':
    createBucket()
  elif arg[1] == '--list' or arg[1]=='-l':
    listBucket()
 
  elif arg[1] not in args:
    run(arg)
 
  

   
#if '__name__' == '__main__':
  
  