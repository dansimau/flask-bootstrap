"""
fabfile module that provides a helper for other modules to programmatically
execute a task on the remote server (as specified by the git branch/server
configuration mapping).
"""
import os
import json
from fabric.api import env, task
from fabric.utils import abort

# Read server config from JSON file.
fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'servers.json')
try:
    env.servers = json.load(open(fp, 'r'))
except:
    env.servers = {}


def remote():
    """
    Returns the current remote server (host_string). If there is none, look up
    the remote server from the current git branch and branch/server config.
    """
    if env.host_string:
        # If host_string is already specified, use that. This allows the user to
        # override the target deploy server on the command-line.
        return env.host_string
    else:
        branch = env.branch
        if branch not in env.servers:
            abort('Branch does not correspond to server and no host specified.')
        return env.servers[branch]


def save():
    """
    Write server config to JSON file.
    """
    json.dump(env.servers, open(fp, 'w'), indent=4)
