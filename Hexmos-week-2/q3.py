from q1 import load_polldata
file_path="polldata.fps"
poll_list=load_polldata(file_path)
'''
def view_list(poll_list,poll_number):
   print(poll_number)
   for index,value in enumerate(poll_list):
      if index==poll_number-1:
        print(value)
        single_list=list(value.items()) #list has only one dictionary
        print(single_list)
        print(single_list[0][1])
        optionvote=list(single_list[1][1].items())
        print(optionvote)
        print(optionvote[0][0])
        print(optionvote[1][0])

        print("Tags:",end="  ")
        print(single_list[2][1])
#list.joint
#accessing keys in dictionary
   
poll_number=3
view_list(poll_list,poll_number)
'''

def view_list(poll_list,poll_number):

   Question=True
   Tags=True
   for index,value in enumerate(poll_list):
      if index==poll_number-1:
         Question=value['Question']
         print(Question)
         tags=value["Tags"]
         Tags_string=', '.join(tags)
         
         optionvote=value['OptionVote']

         for key ,value in optionvote.items():
            print(f"* {key} {value}")

         print("Tags:",Tags_string)
        
poll_number=1
view_list(poll_list,poll_number)

#
# for index,value in enumerate(poll_list):
#       if index==poll_number-1:
#       # print(value)
#          print(value['Question'])
#          print("Tags:",value["Tags"])

         
#          for inner_key,optionvote in value.items():
#                if Question:
#                   Question=False
#                   continue
#                print(optionvote)
#                for key ,value in optionvote.items():
#                   print(f"*{key} {value}")
                  
#          print(value)

# What’s the most liked shoe brand according to you?
# * Puma 1
# * Adidas 2
# * Sparx 3
# * Reebok 4

# Tags: tag1, tag2, … tagN
#          print("Tags:",value["Tags"])