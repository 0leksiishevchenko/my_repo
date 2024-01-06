from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.1',
    description='Very strange code',
    url='https://github.com/0leksiishevchenko/sorter',
    author='Oleksii Shevchenko',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main',
        ],
    },
)