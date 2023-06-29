"""
Automatically set up the project for development.
"""

from setuptools import find_packages, setup

setup(
    name="environ",
    packages=find_packages(),
    install_requires=[
        "requests",
        "numpy",
        "pandas",
        "matplotlib",
        "tqdm",
    ],
    extras_require={
        "dev": [
            "pylint",
            "black",
        ]
    },
)
