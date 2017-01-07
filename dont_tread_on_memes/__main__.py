import dont_tread_on_memes
import click


@click.command()
@click.option("--message", prompt="Don't _____ me: ",
              help=("The word or phrase to substitute for 'tread' in 'don't "
                    "tread on me'"))
def tread(message):
    dont_tread_on_memes.tread_on(message).show()


if __name__ == "__main__":
    tread()
