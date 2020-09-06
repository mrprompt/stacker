import click
import glob
from PIL import ImageChops, Image


def get_matching_captures(captures_dir: list, file_pattern: str):
    return glob.glob("{}/**/{}".format(captures_dir, file_pattern), recursive=True)


def generate_stacks(captures: list, output_file: str):
    stack = []

    for capture in captures:
        stack.append(capture)

    stack_captures(stack, output_file)


def stack_captures(data, output_file):
    try:
        stack = Image.open(data[0])

        for i in range(1, len(data)):
            current_image = Image.open(data[i])
            stack = ImageChops.lighter(stack, current_image)

        stack.save(output_file, "JPEG")
    except:
        pass


@click.command('stacker')
@click.argument('input_dir', type=str)
@click.argument('file_pattern', type=str)
@click.argument('output_file', type=str)
def cli(input_dir, file_pattern, output_file):
    click.echo('- Reading captures')
    captures = get_matching_captures(input_dir, file_pattern)

    if len(captures) == 0:
        click.echo("- Nothing to do")
        exit(0)

    click.echo("- Creating stacks")
    generate_stacks(captures, output_file)

    click.echo("- Done :)")
