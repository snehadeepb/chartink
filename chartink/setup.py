from setuptools import setup,find_packages
setup(
    name='toogle_cell',
    version='0.0.1',
    description='My private package from private github repo',
    url='https://github.com/snehadeepb/chartink.git',
    author='PJ',
    author_email='snehadeep.sb@gmail.com',
    license='unlicense',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'openai',
        'simple_colors'
    ]

)