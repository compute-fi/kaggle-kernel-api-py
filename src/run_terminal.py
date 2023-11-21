import subprocess

def run_terminal_commands(commands):
    data = ''
    for command in commands:
        try:
            result = subprocess.check_output(command, text=True, shell=True)
            print("COMMAND EXECUTED:", command)
            data = result
        except subprocess.CalledProcessError as error:
            print(f"Error running command {command}: {error}")
    return data
