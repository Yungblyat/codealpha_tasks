import os
import shutil

def organize_files(source_dir, target_dir):
    # Create target directories if they don't exist
    for folder_name in ['images', 'documents', 'videos']:
        folder_path = os.path.join(target_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    # Iterate through files in the source directory
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)

        # Check file type and move to corresponding directory
        if os.path.isfile(source_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                shutil.move(source_path, os.path.join(target_dir, 'images', filename))
            elif filename.lower().endswith(('.doc', '.docx', '.pdf', '.txt','pptx')):
                shutil.move(source_path, os.path.join(target_dir, 'documents', filename))
            elif filename.lower().endswith(('.mp4', '.avi', '.mkv')):
                shutil.move(source_path, os.path.join(target_dir, 'videos', filename))

    print("Files organized successfully!")


source_directory = 'E:\\Task\\Unorganized'
target_directory = 'E:\\Task\\Organized'
organize_files(source_directory, target_directory)
