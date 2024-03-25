# Structure for a simple python module

Source : https://www.freecodecamp.org/news/build-your-first-python-package/

# Notes 

In the instructions, they tell us to run:

    python3 setup.py sdist bdist_wheel

Ther is a depracation warning that comes up:

    /opt/homebrew/lib/python3.11/site-packages/setuptools/_distutils/cmd.py:66: SetuptoolsDeprecationWarning: setup.py install is deprecated.
    !!

            ********************************************************************************
            Please avoid running ``setup.py`` directly.
            Instead, use pypa/build, pypa/installer or other
            standards-based tools.

            See https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html for details.
            ********************************************************************************

    !!

But this is fine, as the article also talks about uploading to pypy, but this is not what I want to do.
