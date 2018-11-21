from setuptools import setup
from setuptools import find_packages

setup(
    name='astrotk',
    version='0.10.0',
    packages=['astrotk', 'astrotk.nbody', 'astrotk.nbody.simulator', 'astrotk.tests', 'astrotk.AE4878',
              'astrotk.twobody', 'astrotk.twobody.utils'] + find_packages(),
    package_dir={'': 'src'},
    url='',
    license='MIT',
    author='Geoffrey Garrett',
    author_email='g.h.garrett13@gmail.com',
    description='',
    install_requires=[
        'numpy',
        'sympy',
        'pandas',
        'poliastro',
        'pytest',
        'prettytable'
    ]
)
