from flask import Flask, request, jsonify
import os
from src.create_file import download_and_save_file
from src.create_metadata import generate_metadata_file
from src.utils.commands.execute import run_execute_commands
from src.utils.commands.initial import run_initial_commands
from src.utils.commands.push import run_push_commands
from src.utils.getID import get_id
from src.utils.commands.status import run_status_commands
from src.utils.commands.output import run_output_commands
from src.pinata_upload import pin_file_to_ipfs


app = Flask(__name__)
port = 3000

@app.route('/compute', methods=['GET'])
async def compute():
    fileUrl = request.args.get('fileUrl')
    # inputGpu = str(request.args.get('enable_gpu'))
    # inputTpu = str(request.args.get('enable_tpu'))
    # Convert "t" or "true" to "true", and "f" or "false" to "false"
    # enableGpu = "true" if inputGpu.lower() in ['t', 'true'] else "false"
    # enableTpu = "true" if inputTpu.lower() in ['t', 'true'] else "false"
    result_file = await download_and_save_file(fileUrl)
    print(result_file)
    targetFolder = os.path.normpath(result_file['targetFolder'])
    fileExtension = result_file['fileExtension']
    filename = result_file['filename']
    kernel_type = "script" if fileExtension == "py" else "notebook" if fileExtension == "ipynb" else "unknown"
    print("RESULT",targetFolder, fileExtension, filename)
    await run_execute_commands(targetFolder)
    generatedfolder = generate_metadata_file(targetFolder, filename, fileExtension, kernel_type, "true", "false")
    await run_push_commands(generatedfolder)
    return {"generatedfolder": generatedfolder}

@app.route('/status', methods=['GET'])
async def get_status():
    folderID = request.args.get('folderID')
    ID = await get_id(folderID)
    result = await run_status_commands(ID)
    return {"result": result}

@app.route('/output', methods=['GET'])
async def get_output():
    folderID = request.args.get('folderID')
    ID = await get_id(folderID)
    print("ID",ID)
    await run_output_commands(ID, folderID)
    # Read the file
    title = ID.split('/')[1]
    filePath = os.path.join(folderID, title + '.log')
    ipfs_hash = pin_file_to_ipfs(filePath)
    print(ipfs_hash)
    return {"ipfshash": ipfs_hash}

# Start running the terminal commands
run_initial_commands()

# Start the Flask API
if __name__ == '__main__':
    app.run(port=port)
