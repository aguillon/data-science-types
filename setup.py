"""Package setup"""
from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name="machine-learning-types",
    version="0.1.0",
    author="PAL",
    description="Type stubs for Python machine learning libraries",
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data={
        "matplotlib-stubs": ["__init__.pyi", "artist.pyi", "legend.pyi", "pyplot.pyi", "style.pyi"],
        "numpy-stubs": ["__init__.pyi", "_core.pyi", "random.pyi", "testing.pyi"],
        "pandas-stubs": ["__init__.pyi", "_core.pyi", "testing.pyi"],
        "tensorflow-stubs": [
            "__init__.pyi",
            "_core.pyi",
            "data.pyi",
            "metrics.pyi",
            "optimizers.pyi",
            "random.pyi",
            "summary.pyi",
            "train.pyi",
        ],
        "tensorflow-stubs.keras": ["__init__.pyi", "_core.pyi", "layers.pyi"],
        "tensorflow_probability-stubs": ["__init__.pyi", "bijectors.pyi", "distributions.pyi"],
    },
    packages=["matplotlib-stubs", "numpy-stubs", "pandas-stubs"],
    python_requires=">=3.6",
    zip_safe=False,
)