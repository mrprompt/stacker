from click.testing import CliRunner
from stacker.scripts.cli import cli


def test_cli_count():
    runner = CliRunner()
    result = runner.invoke(cli, ['./', '*P.jpg', 'output.jpg'])
    assert result.exit_code == 0
    assert result.output == "- Reading captures\n- Nothing to do\n"
