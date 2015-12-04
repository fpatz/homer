from setuptools import setup, find_packages

NAME = "homer"
DESCRIPTION = "cross-platform dot file manager"
AUTHOR = "Frank Patz-Brockmann"
AUTHOR_EMAIL = "frank.patz@gmail.com"
URL = "http://github.com/fpatz/homer"
VERSION = "0.0"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=open("README.rst").read(),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'homer = homer:main',
        ],  gg
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    zip_safe=False,
)
