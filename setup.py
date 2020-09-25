import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="diff-imitation",
    version="0.0.1",
    author="blurfx",
    author_email="iam@xo.dev",
    description="A tiny imitation thing of unix diff",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blurfx/diff-imitation/",
    packages=setuptools.find_packages(exclude=["example", "tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
