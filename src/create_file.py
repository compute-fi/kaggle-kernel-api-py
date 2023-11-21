import os
import requests
import uuid
from datetime import datetime

async def download_and_save_file(url):
    try:
        root_folder = './'
        # Create a new target folder with a random name
        target_folder = os.path.join(root_folder, str(uuid.uuid4()))
        os.mkdir(target_folder)

        # Download the file
        response = requests.get(url)

        # Extract file extension
        url_parts = url.split('.')
        file_extension = url_parts[-1]

        # Check if the file extension is .py or .ipynb
        if file_extension in ['py', 'ipynb']:
            # Generate a new name for the file based on timestamp
            timestamp = int(datetime.now().timestamp())
            filename = f'file-{timestamp}'
            new_name = f'{filename}.{file_extension}'

            # Save the file to the specified folder
            file_path = os.path.join(target_folder, new_name)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f'File downloaded and saved as {new_name} in {target_folder}')
            return {'targetFolder': target_folder, 'fileExtension': file_extension, 'filename': filename}
        else:
            print('File has an unsupported extension. Not saving.')
    except Exception as error:
        print('Error downloading and saving file:', str(error))

