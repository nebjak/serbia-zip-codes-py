import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="serbia_zip_codes",
    version="0.0.1",
    author="Nebojsa Jakovljevic",
    author_email="nebojsa@nebjak.net",
    description="Easy access to Serbia zip codes. You can search zip code by city, or city by zip code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nebjak/serbia-zip-codes-py",
    py_modules=["serbia_zip_codes"],
    package_dir={"": "src"},
    packages=[".", "data"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
