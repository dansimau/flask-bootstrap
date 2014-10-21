# Flask-Bootstrap

Welcome to my opinionated, lightweight Flask project template.

## Quick start

1. After installing [Vagrant](http://vagrantup.com/), create and boot the VM inside this directory:

    vagrant up

2. SSH to the VM:

    vagrant ssh

3. Run your app:

    fab run

You will have a running app listening on http://localhost:5000/ at this point.

## Notes

After initial boot, you should:

* Freeze the newly-installed pip packages at their versions:

      pip freeze > requirements.txt

* Set the `SECRET_KEY` for each environment in `app/config/`.

## Requirements

*nix-flavoured OS.

## What's included

The following software will be installed and configured automatically:

* [Alembic](http://alembic.readthedocs.org/en/latest/)
* [cssmin](https://pypi.python.org/pypi/cssmin)
* [Fabric](http://www.fabfile.org/) (deployment scripts included)
* [Flask](http://flask.pocoo.org/)
* [Flask-AssetsLite](https://github.com/tobiasandtobias/flask-assetslite)
* [New Relic](http://newrelic.com/)
* [nginx](http://nginx.org/)
* [PostgreSQL](http://www.postgresql.org/)
* [Puppet](http://puppetlabs.com/) (manifests included)
* [uWSGI](https://uwsgi-docs.readthedocs.org/en/latest/)
* [Vagrant](http://www.vagrantup.com/) VM running Ubuntu 14.04 LTS

## Licence

Licenced under the MIT licence (see LICENCE), so go ahead and fork this!

## Credits

Originally based on https://gist.github.com/urschrei/2666927.
