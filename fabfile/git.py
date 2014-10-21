"""
fabfile module for common git commands - used as a helper by other fabfile
modules.
"""
from fabric.api import local
from fabric.context_managers import hide


def branch():
    """
    Returns the name of the local branch that we're currently on.
    """
    with hide('running'):
        result = local('git symbolic-ref -q HEAD', capture=True)
        try:
            return result.split('/')[2]
        except IndexError:
            return None
