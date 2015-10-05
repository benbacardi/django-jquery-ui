from setuptools import setup

setup(
    name='django-jquery-ui',
    version='1.11.4',
    url='https://github.com/benbacardi/django-jquery-ui',
    description='jQuery UI packaged in a django app to speed up new applications and deployment.',
    author='Ben Cardy',
    author_email='benbacardi@gmail.com',
    license='MIT',
    keywords='django jquery jqueryui staticfiles'.split(),
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['jquery_ui'],
    package_data={'jquery_ui': ['static/js/*.js', 'static/css/jquery-ui/*/*.css', 'static/css/jquery-ui/*/images/*']},
    install_requires=['django-jquery >= 1.6',],
)
