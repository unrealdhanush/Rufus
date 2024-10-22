from setuptools import setup, find_packages

setup(
    name='Rufus',
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
        'tf-keras'
    ],
    entry_points='''
        [console_scripts]
        rufus=Rufus.cli:main
    ''',
)
