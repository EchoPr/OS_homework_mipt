import sys
import asyncio
import subprocess


async def run_command(delay, command):
    await asyncio.sleep(delay)

    try:
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        stdout, stderr = await process.communicate()
        print(stderr.decode() + stdout.decode())
    
    except Exception as e:
        print(f"Error while executing {command}: {e}")


async def execute_file(file_path):
    tasks = []

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(maxsplit=1)
    
            if parts == []: continue
            
            if len(parts) != 2:
                print(f"Unavalible command format: {line}")
                continue

            delay, command = parts
            try:
                delay = int(delay)
                tasks.append(run_command(delay, command))
            except ValueError:
                print(f"Unavalible delay value: {delay}")

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Not enough arguments")
        quit()

    filepath = sys.argv[1]
    asyncio.run(execute_file(filepath))
