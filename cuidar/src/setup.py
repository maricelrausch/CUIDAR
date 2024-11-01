"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
readme_path = path.join(here, "README.md")

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()


install_reqs = [
    "pandas",
    "requests"
]

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install sampleproject
    #
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    name="cuidar",  # Required
    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version="0.1.0",  # Required
    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description="Proyecto perteneciente a la materia prácticas profesionalizantes con la colaboración de la empresa CUIDAR.Por medio de este proyecto se pretende crear visualizaciones que permitan acceder de manera eficaz a información sobre los servicios realizados por la empresa en los ultimos dos años. De esta manera, se podra analizar sencillamente el registro de rotaciones y horas de trabajo e los prestadores, como asi tambien el volumen de prestaciones de las obras sociales.",  # Required
    # This is an optional longer description of your project that represents
    # the body of text which users will see when they visit PyPI.
    #
    # Often, this is the same as your README, so you can just read it in from
    # that file directly (as we have already done above)
    #
    # This field corresponds to the "Description" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=Proyecto perteneciente a la materia prácticas profesionalizantes con la colaboración de la empresa CUIDAR.Por medio de este proyecto se pretende crear visualizaciones que permitan acceder de manera eficaz a información sobre los servicios realizados por la empresa en los ultimos dos años. De esta manera, se podra analizar sencillamente el registro de rotaciones y horas de trabajo e los prestadores, como asi tambien el volumen de prestaciones de las obras sociales.,  # Optional
    # Denotes that our long_description is in Markdown; valid values are
    # text/plain, text/x-rst, and text/markdown
    #
    # Optional if long_description is written in reStructuredText (rst) but
    # required for plain-text or Markdown; if unspecified, "applications should
    # attempt to render [the long_description] as text/x-rst; charset=UTF-8 and
    # fall back to text/plain if it is not valid rst" (see link below)
    #
    # This field corresponds to the "Description-Content-Type" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    # This should be a valid link to your project's main homepage.
    #
    # This field corresponds to the "Home-Page" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#home-page-optional
    url="",  # Optional
    # This should be your name or the name of the organization which owns the
    # project.
    author="equipo 10- cuidar",  # Optional
    # This should be a valid email address corresponding to the author listed
    # above.
    author_email="giovlara8@gmail.com",  # Optional
    classifiers=[  # Optional
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3.7"
    ],
    packages=find_packages(exclude=["contrib", "docs", "tests"]),  # Required
    # This is what we need installed
    install_requires=install_reqs,
    setup_requires=["pytest-runner"] + install_reqs,
    tests_require=["pytest"] + install_reqs,
)
