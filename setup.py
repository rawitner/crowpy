from setuptools import setup

setup(
    name='crowpy',
    version='0.2.0',
    author='Jason Capili',
    author_email='jcapili@alumni.scu.edu',
    packages=['crowpy'],
    include_package_data=True,
    install_requires=[
        'geopy==2.2.0',
        'pandas==1.4.1',
        'lxml==4.6.5',
        'requests==2.20.1',
        'tqdm==4.46.0',
        'usps-api==0.5'
    ],
    url='https://github.com/jcapili/crowpy',
    license='MIT',
    description='Python code for calculating travel distance of USPS shipments',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: MacOS :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ],
    keywords='usps shipping carbon offsets miles carbon estimation air ground',
    long_description=open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)