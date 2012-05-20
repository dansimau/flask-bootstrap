After running `fab virtualenv.build` to install packages from requirements.txt,
you should freeze installed packages at their installed versions by running:

    venv/bin/pip freeze > requirements.txt
