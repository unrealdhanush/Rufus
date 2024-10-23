from setuptools import setup, find_packages

setup(
    name='RufusAIToolkit',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'beautifulsoup4',
        'aiohttp-socks',
        'requests',
        'tldextract',
        'numpy',
        'pandas',
        'nltk',
        'sentence-transformers',
        'tf-keras',
        'python-dotenv'
    ],
    python_requires='>=3.8',
    author='Dhanush Balakrishna',
    description='An AI-powered tool for intelligent web data extraction.',
    url='https://github.com/unrealdhanush/Rufus',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    entry_points='''
        [console_scripts]
        rufus=Rufus.cli:main
    ''',
)
