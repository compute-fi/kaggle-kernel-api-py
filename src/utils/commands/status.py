import asyncio
import re
import subprocess

async def run_status_commands(id):
    command = ['kaggle', 'kernels', 'status', str(id)]
    process = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, text=False)
    output_bytes, _ = await process.communicate()
    output = output_bytes.decode('utf-8')
        # Extract status using regular expression
    match = re.search(r'has status "([^"]+)"', output)
    status = match.group(1) if match else None
    return status
