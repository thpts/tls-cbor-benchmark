from setuptools import setup

setup(
    name='cbor_converter',
    author='Thomas Peterson',
    author_email='nosretep.samoht@gmail.com',
    license='Apache 2',
    packages=['cbor_converter'],
    install_requires=[
        'pyasn1',
        'pyasn1-modules'
    ],
    test_suite='test',
    entry_points={
        'console_scripts': [
            'cbor_converter = cbor_converter.cli:main'
        ]
    }
)
