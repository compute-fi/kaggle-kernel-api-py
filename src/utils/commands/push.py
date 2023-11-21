import subprocess

async def run_push_commands(targetFolder):
    subprocess.run(['kaggle', 'kernels', 'push', '-p', f'{targetFolder}'])
