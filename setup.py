from setuptools import setup, find_packages

setup(
    name='rufus-ai',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'beautifulsoup4',
        # Other dependencies
    ],
    entry_points='''
        [console_scripts]
        rufus=Rufus.cli:main
    ''',
)
