import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sketches-py",
    version="0.1.0",
    description="Python implementation of DDSketch, a distributed quantile sketch algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/GraphMetrics/sketches-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords=["ddsketch", "quantile", "sketch"],
    install_requires=[
        "numpy>=1.11.0",
    ],
    python_requires=">=3.6",
)
