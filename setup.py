import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='sharepp',
    version='0.1.1',
    scripts=['sharepp.py'],
    author="Lukas Brauckmann",
    author_email="lukas.brauckmann@gmail.com",
    description="The SharePriceProvider is small script that provides share prices in EUR for a given ISIN.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Plebo13/sharepp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: OS Independent",
    ],
)
