from setuptools import setup, find_packages

setup(
    name='stark-osint-v1',
    version='0.1.0',
    author='Stark',
    author_email='',
    description='A command-line tool for various OSINT lookups.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/urSTARK/stark-osint-v1',  # Replace with your GitHub URL
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'colorama',
        'Pillow',
        'pytesseract',
        'numpy',
        'opencv-python',
        'exifread',
    ],
    entry_points={
        'console_scripts': [
            'osint_cli=osint_cli:run_cli',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
