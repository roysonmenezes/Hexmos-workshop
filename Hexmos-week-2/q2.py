from pprint import pprint
from q1 import load_polldata
file_path = "polldata.fps"

poll_list=load_polldata(file_path)

# second question
list_of_tags = ["phones", "apple", "shoes"]
new_list = []
def filter_by_tags(polls_list, tags):

    for i in poll_list:
        if any(tag in i.get("Tags", []) for tag in tags):  # complex line
            new_list.append(i)
            
    print(new_list)

filter_by_tags(poll_list, list_of_tags)  # function call

# simple to understand version
print("\n\n")
list_of_tags = ["phones", "cricket"]
new_list = []


def filter_by_tags(polls_list, tags):

    for i in polls_list:
        tags_list = i.get("Tags", [])
        print("tags list is:")
        print(tags_list)
        tag_found = False
        for tag in tags:
            if tag in tags_list:
                tag_found = True

        if tag_found:
            new_list.append(i)
    print(new_list)


filter_by_tags(poll_list, list_of_tags)  # function call
