from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Download\n'
    '********\n'
    )

tests_require = [
    'zope.testing',
    'zope.app.wsgi',
    'grokcore.view',
    'zope.login',
    ]

setup(
    name='grokcore.permission',
    version='1.2dev',
    author='Grok Team',
    author_email='grok-dev@zope.org',
    url='http://grok.zope.org',
    download_url='http://cheeseshop.python.org/pypi/grokcore.json/',
    description='Permission Role Components for Grok.',
    long_description=long_description,
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Framework :: Zope :: 3',
        ],
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages=['grokcore'],
    include_package_data = True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'martian',
        'grokcore.component',
        'grokcore.security',
        'zope.securitypolicy',

        'zope.component',
        'zope.interface',
        'zope.publisher',
        'zope.principalregistry',
        ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
)
