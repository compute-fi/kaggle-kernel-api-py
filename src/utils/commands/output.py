import subprocess

async def run_output_commands(id, target_folder):
    subprocess.run(['kaggle', 'kernels', 'output', str(id), '-p', str(target_folder)])

