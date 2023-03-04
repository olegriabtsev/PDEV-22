from setuptools import find_packages, setup

setup(
    name='my_library',
    packages=find_packages(include='my_library'),
    version='0.0.1',
    description='My python library',
    author='OR',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest>=4.4.1'],
    test_suite='tests'
)
