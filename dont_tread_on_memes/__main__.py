import dont_tread_on_memes
import click


@click.command()
@click.option("--message", prompt="Don't _____ me",
              help=("The word or phrase to substitute for 'tread' in 'don't "
                    "tread on me'"))
@click.option("--save", default=None, help="Where to save the image")
def tread(message, save):
    flag = dont_tread_on_memes.tread_on(message)
    if save is not None:
        flag.save(save)
    else:
        flag.show()


if __name__ == "__main__":
    tread()
