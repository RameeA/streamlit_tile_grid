from setuptools import setup, find_packages

setup(
    name='my_streamlit_component',
    version='0.1',
    author='Your Name',
    author_email='your_email@example.com',
    description='A custom Streamlit component for rendering tiles',
    packages=find_packages(),
    install_requires=[
        'streamlit>=0.86.0',
        'pandas>=1.3.0',
        'numpy>=1.21.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
