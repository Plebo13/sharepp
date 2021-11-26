import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='sharepp',
    version='1.0',
    author="Lukas Brauckmann",
    author_email="lukas.brauckmann@gmail.com",
    description="Library for getting ETF and cryptocurrency prices.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Plebo13/sharepp",
    packages=setuptools.find_packages(where="sharepp"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
        'bs4',
    ],
)
