"""Main CLI script."""


def main():
    """Docstring explaining why typer messes up if imports arent in the fucntion."""
    import sys
    import typer
    from wasabi import msg
    from repo_template.cli.example import example
    from repo_template.cli.print_fonts import print_fonts

    commands = {
        "run_example": example,
        "print_fonts": print_fonts,
    }
    if len(sys.argv) == 1:
        msg.info("Available commands", ", ".join(commands), exits=1)
    command = sys.argv.pop(1)
    sys.argv[0] = f"repo_template {command}"
    if command in commands:
        typer.run(commands[command])
    else:
        available = "Available: {}".format(", ".join(commands))
        msg.fail("Unknown Command: {}".format(command), available, exits=1)
