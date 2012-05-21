## Quick start

After installing [Vagrant](http://vagrantup.com/), create and boot the VM:

	vagrant up

SSH to the VM:

	vagrant ssh

Run your app:

	fab app.run

## Notes

After initial boot, you should freeze the newly-installed pip packages at their versions:

	pip freeze > requirements.txt
