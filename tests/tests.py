from click.testing import CliRunner
from autoflow.main import new, git_cli, jump, start
import os
import collections 


# Start: Test incorrect usage
def test_start_wrong():
    runner = CliRunner()
    result = runner.invoke(start.start)
    assert result.output.rstrip('\n') == "Usage: start [OPTIONS] DIR\nTry 'start --help' for help.\n\nError: Missing argument 'DIR'."

# Start: test when the project doesn't exist
def test_start_noproj():
    runner = CliRunner()
    result = runner.invoke(start.start, ['testproj'])
    assert result.output.rstrip('\n') == "😅 Project doesn't exist"

# Start: test when project exists but af-config.json doesn't
def test_start_proj_noconfig():
    runner = CliRunner()
    result = runner.invoke(start.start, ['myproject'])
    assert result.output.rstrip('\n') == "🤦 af-config.json doesn't exist"

# Start: test when both the project and local configuration file exists, check if invoked
# Testing locally using commands is better to see output
def test_start_proj_config():
    runner = CliRunner()
    result = runner.invoke(start.start, ['myproject2'])

# Git-cli: test command normally used
# This should be tested locally, and not within Github Actions due to credentials

# Jump: test normal af jump with existing repository
def test_jump_existing():
    runner = CliRunner()
    result = runner.invoke(jump.jump, ['myproject2'])
    assert result.exit_code == 0
    assert os.getcwd() == os.path.expandvars('$GITHUB_WORKSPACE/myproject2')

# Jump: test with non-existing project
def test_jump_nonexisting():
    runner = CliRunner()
    result = runner.invoke(jump.jump, ['example'])
    assert result.output.rstrip('\n') == "😅 Project doesn't exist"

# Jump: test incorrect usage
def test_jump_wrong():
    runner = CliRunner()
    result = runner.invoke(jump.jump)
    assert result.output.rstrip('\n') == "Usage: jump [OPTIONS] DIR\nTry 'jump --help' for help.\n\nError: Missing argument 'DIR'."

# New: test normal usage with python, no dependencies
def test_new_python_nodep():
    runner = CliRunner()
    result = runner.invoke(new.new, ['-l', 'python', '-n', 'newproject'])
    assert os.getcwd() == os.path.expandvars('$GITHUB_WORKSPACE/newproject')

# New: test normal usage with react, no dependencies
def test_new_react_nodep():
    runner = CliRunner()
    result = runner.invoke(new.new, ['-l', 'react', '-n', 'newproject1'])
    assert os.getcwd() == os.path.expandvars('$GITHUB_WORKSPACE/newproject1')
    assert collections.Counter(os.listdir('.')) == collections.Counter(['package.json', 'node_modules', 'src', 'README.md', 'yarn.lock', 'public', '.gitignore'])

# New: test normal usage with node, no dependencies
def test_new_node_nodep():
    runner = CliRunner()
    result = runner.invoke(new.new, ['-l', 'node', '-n', 'newproject2'])
    assert os.getcwd() == os.path.expandvars('$GITHUB_WORKSPACE/newproject2')

##
# Rest of options for 'af new' should be tested locally, in a virtual environment in order for proper
# configuration of projects and proper output given.
