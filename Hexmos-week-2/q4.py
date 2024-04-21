from q1 import load_polldata
file_path="polldata.fps"
poll_list=load_polldata(file_path)

def update_poll(poll_list, pollNumber, optionName):

    print("innside function")
    for index,value in enumerate(poll_list):
      if index==pollNumber-1:
         print(value)
         optionvote=value["optionVote"]
         for key in optionvote.keys():
            if key==optionName:
               optionvote[key]=optionvote[key]+1


    return poll_list


# pollNumber=1
# poll_data=update_poll(poll_list, 3,"Python")
# print(poll_data)

# Example: 
# initial data - [{question: ..., optionVote: {puma: 5, ...}, tags: [...]}, ...]
# after- update_poll(polls_data,1,”puma”)
# output data- [{question: ..., optionVote: {puma: 6, ...}, tags: [...]}, ...]