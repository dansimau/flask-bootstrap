"""
fabfile module that provides generic helper functions for other modules.
"""
import os
from fabric.api import env, local, run as fab_run
from fabric.context_managers import cd, lcd


def do(cmd, capture=False, *args, **kwargs):
    """
    Runs command locally or remotely depending on whether a remote host has
    been specified.
    """
    if env.host_string or env.host or env.hosts:
        with cd(env.remote_path):
            if env.get('sudo', False):
                cmd = 'sudo %s' % cmd
            return fab_run(cmd, *args, **kwargs)
    else:
        # project root path is the default working directory
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if env['lcwd']:
            # lcd has already been invoked. If it's with a relative path, let's
            # make that relative to the project root
            if not env['lcwd'].startswith('/'):
                path = '%s/%s' % (path, env['lcwd'])
            else:
                # Honour the current lcd contact if it's an absolute path
                path = env['lcwd']
        with lcd(path):
            # Add shell envs
            for name, val in env.shell_env.iteritems():
                cmd = 'export {name}="{val}" && {cmd}'.format(name=name,
                                                              val=val,
                                                              cmd=cmd)
            # Add command prefixes to local commands
            for prefix in env.command_prefixes:
                cmd = '{prefix} && {cmd}'.format(prefix=prefix, cmd=cmd)
            return local(cmd, *args, capture=capture, **kwargs)
