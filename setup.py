from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='dictionary-file-lib',
    version='0.0.4',
    license='MIT License',
    author='Kaio Cândido Santiago',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='kaio.santiago.13@hotmail.com',
    keywords='dictionary lib',
    description=u'Keywords lib to read a txt file',
    packages=['dictionary_file'],
    install_requires=['robotframework', 'generate-lib'],)