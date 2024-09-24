import os
import shutil

def organize_files(directory):
  """Organizes files in the specified directory based on their extensions.

  Args:
    directory: The path to the directory to organize.
  """

  for filename in os.listdir(directory):
    # Ignore directories
    if os.path.isdir(os.path.join(directory, filename)):
      continue

    # Get the file extension
    file_extension = os.path.splitext(filename)[1]

    # Create a new directory for the file type if it doesn't exist
    new_dir = os.path.join(directory, file_extension[1:])
    if not os.path.exists(new_dir):
      os.makedirs(new_dir)

    # Move the file to the new directory
    shutil.move(os.path.join(directory, filename), new_dir)

# Replace 'path/to/your/directory' with the actual path to the directory you want to organize
directory_to_organize = './'
organize_files(directory_to_organize)
