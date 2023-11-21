import subprocess

async def run_status_commands(targetFolder):
    subprocess.run(['kaggle', 'kernels', 'status', str(id)])
