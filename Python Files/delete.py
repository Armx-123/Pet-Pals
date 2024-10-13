import os

def delete_all_files_in_folder(folder_path):
    # Get the list of all files in the folder
    file_list = os.listdir(folder_path)

    # Iterate over the files and delete each one
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

# Specify the folder path
folder_path = 'Videos'
pp="Videoss"
# Call the function to delete all files in the folder
delete_all_files_in_folder(folder_path)
delete_all_files_in_folder(pp)

os.remove("video.mp4")
