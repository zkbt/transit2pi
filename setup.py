# The template for this setup.py came from Tim Morton,
#  who I understand took it from Dan F-M. Thanks guys!

# import our ingredients
from setuptools import setup, find_packages
import os,sys

# running `python setup.py release` from the command line will post to PyPI
'''
if "release" in sys.argv[-1]:
    os.system("python setup.py sdist")
    # uncomment the next line to test out on test.pypi.com/project/tess-zap
    #os.system("twine upload --repository-url https://test.pypi.org/legacy/ dist/*")
    os.system("twine upload dist/*")
    os.system("rm -rf dist/transit2pi*")
    sys.exit()
'''

# return the README as a string
def readme():
    with open('README.md') as f:
        return f.read()

# a little kludge to get the version number from __version__
exec(open('transit2pi/version.py').read())

setup(name = "transit2pi",
    version = __version__,
    description = "Python toolkit for visualizing transit light curves in a planetarium dome.",
    long_description = readme(),
    author = "Zachory K. Berta-Thompson",
    author_email = "zach.bertathompson@colorado.edu",
    url = "https://github.com/zkbt/transit2pi-experiments",
    packages = find_packages(),
    package_data = {'transit2pi':[]},
    include_package_data=False,
    scripts = [],
    classifiers=[
      'Intended Audience :: Science/Research',
      'Programming Language :: Python',
      'Topic :: Scientific/Engineering :: Astronomy'
      ],
    install_requires=['numpy', 'astropy', 'scipy',
                      'matplotlib', 'astroquery', 'lightkurve'],
    zip_safe=False,
    license='MIT',
)
