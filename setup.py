from setuptools import setup, find_packages
import os


def get_version():
    """Read version from package init file (__init__.py)"""
    full_path = os.path.join((os.path.dirname((__file__))), 'okta_jwt_verifier', '__init__.py')
    with open(full_path) as f:
        for line in f:
            if '__version__' in line:
                return line.split('=')[1].strip().strip("'")


setup(
    name="okta_jwt_verifier",
    version=get_version(),
    author="Okta, Inc.",
    author_email="pgleeson@spoton.com",
    url="https://github.com/PatrickGleeson/okta-jwt-verifier-python",
    license="Apache License 2.0",
    description="Okta JWT Verifier",
    long_description=open("LONG_DESCRIPTION.md").read(),
    test_suite="tests",
    packages=find_packages(exclude=("tests",)),
    python_requires="==2.7",
    classifiers=[
    ],
    install_requires=[
        "cachecontrol",
        "python-jose==3.2.0",
        "rsa==4.3",
        "retry"
    ]
)
