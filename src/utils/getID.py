import aiofiles
import asyncio
import json
import os

async def get_id(folder_path):
    file_name = 'kernel-metadata.json'
    file_path = os.path.join(folder_path, file_name)

    try:
        async with aiofiles.open(file_path, mode='r', encoding='utf-8') as file:
            data = await file.read()
            metadata = json.loads(data)
            id_value = metadata['id']

            print(f"ID value of {file_name}: {id_value}")

            return id_value
    except Exception as error:
        print(f"Error reading or parsing file: {error}")
