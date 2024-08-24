
"""Example CLI code for template repo."""

import typer
import subprocess
from termcolor import colored
from typing_extensions import Annotated

typer.rich_utils.STYLE_METAVAR = "bold"
required_color = "light_red"
optional_color = "light_green"

Arg = typer.Argument
Opt = typer.Option
app = typer.Typer(
    name="repo_template",
    rich_markup_mode="rich",
)

@app.command(
        "example",
        context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def example(
    ctx: typer.Context, # This is only used to read additional arguments
    command: Annotated[
        str, typer.Argument(...,
            help=f"{colored('Required', required_color)} Command to be executed.",
            rich_help_panel=f"{colored("Required", required_color)} Inputs"
        )
    ],
    run_not_echo: Annotated[
        bool, typer.Option("--no-echo/--echo", "--run/--no-run", "-r/-R", 
            help=f"{colored('Optional', optional_color)} Option to run or echo the entered command.",
            rich_help_panel=f"{colored("Optional", optional_color)} Inputs"
        )
    ] = False,
):
    if run_not_echo:
        uninstall_command = command
    else:
        uninstall_command = f"echo '{command}'"

    uninstall_command_return = subprocess.run(
        uninstall_command,
        shell=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )

    # Print results.
    if uninstall_command_return.stderr != b'':
        response = uninstall_command_return.stderr
        print(f"Returned Error: {response}")
    else:
        response = uninstall_command_return.stdout.decode("utf-8")
        print(f"Command that eas executed:\n{response}")
    return 