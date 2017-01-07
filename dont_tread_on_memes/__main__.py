import dont_tread_on_memes
import click


@click.command()
@click.option("--message", prompt="Don't _____ me",
              help=("The word or phrase to substitute for 'tread' in 'don't "
                    "tread on me'"))
@click.option("--format/--no-format", default=True,
              help=("Use the provided message as the entire caption instead of"
                    " formatting it as 'Don't [message] me'"))
@click.option("--save", default=None, help="Where to save the image")
def tread(message, format, save):
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
