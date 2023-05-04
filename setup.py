from setuptools import setup, find_packages

setup(
    name='hi_package',
    version='1.0.0',
    description='A simple package that says hi',
    author='Your Name',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'sayhi = hi_package.hello:sayHi'
        ]
    }
)
