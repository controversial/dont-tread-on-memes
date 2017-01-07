import dont_tread_on_memes
import click


@click.command()
@click.option("--message", prompt="Don't _____ me",
              help=("A message to use as a caption for the flag"),
              metavar="<caption>")
@click.option("--format/--no-format", default=True,
              help=("Whether to format the provided message as 'Don't "
                    "<caption> me' (default) or to use the provided message "
                    "as the entire caption."))
@click.option("--save", default=None, help="Where to save the image")
def tread(message, format, save):
    """Create a Don't Tread on Meme — an image of the Gadsden flag with the
    words "DONT TREAD ON ME" replaced by something else."""
    # Generate the flag
    if format is True:
        flag = dont_tread_on_memes.dont_me(message)
    else:
        flag = dont_tread_on_memes.tread_on(message)

    # Save or show
    if save is not None:
        flag.save(save)
    else:
        flag.show()


if __name__ == "__main__":
    tread()
