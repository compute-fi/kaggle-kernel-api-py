import json
import os

with open('kaggle.json', 'r') as file:
    raw_data = file.read()

json_data = json.loads(raw_data)

# Extract the username from kaggle.json
username = json_data['username']

def generate_metadata_file(target_folder, kernel_slug, extension, kernel_type, enable_gpu, enable_tpu):
    metadata = {
        'id': f'{username}/{kernel_slug}',
        'title': f'{kernel_slug}',
        'code_file': f'{kernel_slug}.{extension}',
        'language': 'python',
        'kernel_type': kernel_type,
        'is_private': 'true',
        'enable_gpu': enable_gpu,
        'enable_tpu': enable_tpu,
        'enable_internet': 'true',
        'dataset_sources': [],
        'competition_sources': [],
        'kernel_sources': [],
        'model_sources': []
    }

    json_string = json.dumps(metadata, indent=2)
    file_path = os.path.join(target_folder, 'kernel-metadata.json')

    with open(file_path, 'w') as json_file:
        json_file.write(json_string)

    print('kernel-metadata.json generated successfully!')
    return target_folder
