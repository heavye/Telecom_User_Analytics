from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['pandas>=1.1.0', 'numpy>=1.19.0', ]

test_requirements = ['pytest>=3', ]

setup(
    name='telecom user analysis',
    version='0.1.0',    
    description='User Analytics in the Telecommunication Industry - Overview',
    url='https://github.com/heavye/Telecom_User_Analytics',
    author='Euel Fantaye',
    author_email='euelfantaye@gmail.com',
    license='',
    packages=['pyexample'],
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)