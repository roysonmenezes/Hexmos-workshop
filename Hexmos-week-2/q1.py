from pprint import pprint

file_path = "polldata.fps"


def load_polldata(filepath):
    with open(file_path, "r") as file:
        first_line = True
        poll_list = []
        n = 0
        i = 1
        # newline
        for line in file:
            n = n + 1
            while i < n:
                elements = line.strip().split("::")
                if first_line:
                    first_line = False
                    continue
                if elements:

                    option = elements[1].strip().split("|")
                    vote = elements[2].strip().split("|")
                    vote_int = [int(x) for x in vote]

                    tags = []
                    stripped_elements = elements[3].strip()
                    tags_list = stripped_elements.split("|")

                    for tag in tags_list:
                        tags.append(tag.strip())

                    # fixing errors
                    option_vote = {}
                    option_vote1 = dict(zip(option, vote_int))

                    for key, value in option_vote1.items():
                        stripped_key = key.strip()
                        option_vote[stripped_key] = value

                    # without zip
                    option_vote2 = {}
                    for j in range(len(option)):
                        keys = option[j]
                        values = vote_int[j]
                        option_vote2[keys] = values
                    # without zip
                        
                    # fixing errors
                    dictionary = {
                        "Question": elements[0].strip(),
                        "optionVote": option_vote,
                        "Tags": tags,
                    }
                    poll_list.append(dictionary)
                    i = i + 1

        return poll_list


load_polldata(file_path)
