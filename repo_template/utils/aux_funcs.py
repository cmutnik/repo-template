
"""Utility and auxiliary functions for `repo_template.utils.aux_funcs` module."""

import subprocess

def execute_command(command: str) -> subprocess.CompletedProcess:
    """Execute provided command.
    
    This function exists for sphinx docs demonstration.

    Args:
        uninstall_command (str): Command to be executed.

    Returns:
        subprocess.CompletedProcess: Executed command details.
    """
    uninstall_command_return = subprocess.run(
        command,
        shell=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )

    return uninstall_command_return

def parse_out_response(uninstall_command_return: subprocess.CompletedProcess) -> str:
    """Parse out response from executed command.

    This function exists for sphinx docs demonstration.

    Args:
        uninstall_command_return (subprocess.CompletedProcess): Executed command details.

    Returns:
        str: Response from executing command.
    """
    # Print results.
    if uninstall_command_return.stderr != b'':
        response = uninstall_command_return.stderr
        print(f"Returned Error: {response}")
    else:
        response = uninstall_command_return.stdout.decode("utf-8")
        print(f"Response:\n\n{response}")

    return response