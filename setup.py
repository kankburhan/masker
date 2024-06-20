from setuptools import setup, find_packages

setup(
    name='masker',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'dev': ['unittest'],
    },
    author='kankburhan',
    author_email='kankburhan@gmail.com',
    description='A library for masking strings with custom characters.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kankburhan/masker',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
