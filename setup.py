import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="matrix7",
    version="1.1.0",
    author="Mohamed Benkedadra",
    author_email="hammicristo@gmail.com",
    description="Matrix and Vector Manipulation library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LogX7/Matrix7",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Topic :: Education',
        'Natural Language :: English',
    ],
)