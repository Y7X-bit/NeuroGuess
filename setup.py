from setuptools import setup

setup(
    name="GuessTheNumberPro",
    version="1.0.0",
    description="🎯 Premium GUI-based number guessing game built with CustomTkinter",
    author="Y7X",
    author_email="your-email@example.com",
    url="https://github.com/Y7X-bit/GuessTheNumberPro",
    py_modules=["guess_the_number_gui"],
    install_requires=[
        "customtkinter"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7',
)
