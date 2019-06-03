# Classification (U)

"""Program:  setup.py

    Description:  A setuptools based setup module.

"""

# Libraries and Global Variables

# Standard
import os
import setuptools

# Third-party

# Local
import version


# Read in long description from README file.
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md")) as f_hdlr:
    LONG_DESCRIPTION = f_hdlr.read()

setuptools.setup(
    name="Git_Lib",
    description="Git Libraries and Classes.",
    author="Mark Pernot",
    author_email="Mark.J.Pernot@coe.ic.gov",
    url="https://sc.appdev.proj.coe.ic.gov/JAC-DSXD/git-lib",
    version=version.__version__,
    platforms=["Linux"],
    long_description=LONG_DESCRIPTION,

    py_modules=[
        "git_class",
        "__init__",
        "version"],

    classifiers=[
        # Common Values:
        #  1 - Pre-Alpha
        #  2 - Alpha
        #  3 - Beta
        #  4 - Field
        #  5 - Production/Stable
        "Development Status :: 2 - Alpha",
        "Operating System :: Linux",
        "Operating System :: Linux :: Centos",
        "Git :: Gitlab",
        "Git :: Github",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"])
