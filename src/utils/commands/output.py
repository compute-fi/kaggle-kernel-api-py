from ...run_terminal import run_terminal_commands

async def run_output_commands(id, target_folder):
    command = f'kaggle kernels output {id} -p {target_folder}'
    await run_terminal_commands([command])
