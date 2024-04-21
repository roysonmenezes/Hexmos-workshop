
from q1 import load_polldata
from q4 import update_poll
file_path="updated_polldata.fps"
poll_list=load_polldata("polldata.fps")

new_data=update_poll(poll_list,4,"puma")

def save_poll(new_data, file_path):
    with open(file_path,"w") as file:
        for item in new_data:
            file.write(f"{item}\n")
        
    print("updation successfull")
    return new_data

saved_file=save_poll(new_data, file_path)
print(saved_file)