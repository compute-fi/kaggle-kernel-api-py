import subprocess
import os

async def run_execute_commands(target_folder):
    commands = [
    'kaggle kernels init -p {}'.format(target_folder)
    ]

    
    for command in commands:
        subprocess.run(command, shell=True)
