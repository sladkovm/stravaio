import io
import os
import sys
from shutil import rmtree
from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'stravaio'
DESCRIPTION = 'Python client for Strava API with a focus on fluent data handling'
URL = 'https://github.com/sladkovm/stravaio'
EMAIL = 'sladkovm@gmail.com'
AUTHOR = 'Maksym Sladkov'
# What packages are required for this module to be executed?
REQUIRED = [
    'pandas',
    'urllib3',
    'maya',
    'certifi',
    'pyarrow==0.14.0',
    'requests',
    'loguru'
]

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Load the package's __version__.py module as a dictionary.
about = {}
with open(os.path.join(here, '__version__.py')) as f:
    exec(f.read(), about)


class CleanCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds")
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        try:
            self.status("Removing previous builds")
            rmtree(os.path.join(here, 'build'))
        except OSError:
            pass

        sys.exit()


class BuildCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds")
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        try:
            self.status("Removing previous builds")
            rmtree(os.path.join(here, 'build'))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution")
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        sys.exit()


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds")
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        try:
            self.status("Removing previous builds")
            rmtree(os.path.join(here, 'build'))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution")
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status("Uploading the package to PyPi via Twine")
        os.system('twine upload dist/*')

        sys.exit()


class UploadTestCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds")
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        try:
            self.status("Removing previous builds")
            rmtree(os.path.join(here, 'build'))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution")
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status("Uploading the package to TestPyPi via Twine")
        os.system('twine upload --repository-url https://test.pypi.org/legacy/ dist/*')

        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests', 'examples',)),
    # If your package is a single module, use this instead of 'packages':
    py_modules=['stravaio'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
    ],
    # $ setup.py publish support.
    cmdclass={
        'clean': CleanCommand,
        'bbuild': BuildCommand,
        'upload': UploadCommand,
        'test_upload': UploadTestCommand,
    },
)
