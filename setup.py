import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="package-name-exporter",
    version="0.0.1",
    author="Allwin Raju",
    author_email="allwindicaprio@gmail.com",
    description="Export python packages installed to txt, pdf and xls format",
    url="https://github.com/Allwin12/package-name-exporter",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "xlwt>=1.3",
        "fpdf>=1.7"
    ]
)
