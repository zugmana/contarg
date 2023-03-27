import click
from .run_hierarchical import contarg
from .run_seedmap import contarg as contargsm
from .run_tans import contarg as contargtans
from .run_pfm import contarg as contargpfm


contarg = click.CommandCollection(sources=[contarg, contargsm, contargtans, contargpfm])

if __name__ == "__main__":
    contarg()
