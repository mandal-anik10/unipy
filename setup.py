import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unipy",
    version="2023.10.1",
    author="Anik Mandal",
    author_email="mandal.anik10@gmail.com",
    description="A unified module for physics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mandal-anik10/unipy",
    project_urls={
        "Unipy webpage": "https://mandal-anik10.github.io/unipy/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy", 
        "sklearn"
    ],
    package_dir={},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)

    
    
    
    
    
    
    