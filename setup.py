import os

import setuptools

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "pipeline", "__version__.py"), "r") as f:
    exec(f.read(), about)

with open("README.md", "r") as f:
    long_description = f.read()


required_packages = [
    "pydantic",
    "python-dotenv",
]
extras = {
    "dev": ["black", "flake8", "isort", "mypy"],
    "test": ["pytest", "pytest-cov", "black", "flake8", "isort", "mypy"],
}

setuptools.setup(
    name=about["__title__"],
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    description=about["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=about["__url__"],
    license=about["__license__"],
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=required_packages,
    extras_require=extras,
    py_modules=["manage"],
    entry_points={
        "console_scripts": [
            "manage=manage:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
