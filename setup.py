import setuptools

# Load the long description from the README
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="SSL-For-Code",
    version="0.0.7",
    author="Nikhil Singh",
    author_email="nikhil.s@students.iiit.ac.in",
    description="A model that learns to predict Python source code",
    long_description=long_description,
    long_description_content_type="markdown",
    url="https://github.com/Nikhil-1920/SSL-For-Code",
    project_urls={
        "Documentation": "https://github.com/Nikhil-1920/SSL-For-Code",
    },
    packages=setuptools.find_packages(
        exclude=(
            "labml_helpers", "labml_helpers.*",
            "labml_nn", "labml_nn.*",
            "labml", "labml.*",
            "test", "test.*",
        )
    ),
    install_requires=[
        "labml>=0.4.103",
        "labml_helpers>=0.4.75",
        "labml_nn>=0.4.88",
        "torch",
        "einops",
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    keywords="code-autocomplete deep-learning",
)
