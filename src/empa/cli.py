from typer import Argument, Context, Exit, Option, Typer
from rich import print
from rich.console import Console


console = Console()
app = Typer()


def version_func(flag):
    if flag:
        print(__version__)
        raise Exit(code=0)


@app.callback(invoke_without_command=True)
def main(
    ctx: Context, version: bool = Option(False, callback=version_func, is_flag=True)
):
    message = """Bem vindo ao EMPA"""
    if ctx.invoked_subcommand:
        return
    console.print(message)
