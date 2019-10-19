import setuptools

setuptools.setup(
    name="kobra",
    version="1.1.0",
    author="agaev1",
    description="Helping you get to data faster",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    install_requires=[
        'QuantLib-Python==1.16.1',
        'pandas==0.25.2'
    ]
)
