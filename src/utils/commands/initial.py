import subprocess

initial_commands = [
    'pip install kaggle',
    'mkdir ~/.kaggle',
    'cp kaggle.json ~/.kaggle/',
    'chmod 600 ~/.kaggle/kaggle.json'
]

def run_initial_commands():
    for command in initial_commands:
        subprocess.run(command, shell=True)
