from setuptools import setup

setup(
    name="karenl7testci",
    version="0.0.2",
    description="testing continuous integration",
    author="Karen Leung",
    author_email="karen.ym.leung@gmail.com",
    packages=["karenl7testci"],
    package_dir={"karenl7testci": "src/karenl7-test-ci"},
    install_requires=[
        "numpy",
    ],
)