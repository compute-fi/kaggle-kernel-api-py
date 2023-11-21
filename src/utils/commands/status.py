from ...run_terminal import run_terminal_commands  # Assuming run_terminal_commands is defined in run_terminal.py

async def run_status_commands(id):
    await run_terminal_commands(['kaggle', 'kernels', 'status', str(id)])
