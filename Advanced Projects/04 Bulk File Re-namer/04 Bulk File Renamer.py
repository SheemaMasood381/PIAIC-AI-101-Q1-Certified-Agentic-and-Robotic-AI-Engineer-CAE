import os

def bulk_rename_files(target_directory, prefix, suffix, start_index=1):
    # Change the working directory to the target directory
    os.chdir(target_directory)
    
    # Get a list of all files in the directory
    files = os.listdir(target_directory)
    
    # Filter out directories from the list
    files = [f for f in files if os.path.isfile(f)]
    
    # Loop through each file and rename it
    for index, filename in enumerate(files, start=start_index):
        # Extract the file extension
        file_extension = os.path.splitext(filename)[1]
        
        # Construct the new name
        new_name = f"{prefix}{index}{suffix}{file_extension}"
        
        # Rename the file
        os.rename(filename, new_name)
        
        # Print the old and new names
        print(f"Renamed '{filename}' to '{new_name}'")

# Example usage
target_directory = '/'
prefix = 'file_'
suffix = '_renamed'
start_index = 1

bulk_rename_files(target_directory, prefix, suffix, start_index)
