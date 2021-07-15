from setuptools import setup, find_packages

setup(
    name='django-sage-streaming',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    version='0.1.0',
    license='GNU',
    description='video streaming based on Django',
    author='Sage Team',
    author_email='mail@sageteam.org',
    url='https://github.com/sageteam-org/django-sage-streaming',
    download_url='https://github.com/sageteam-org/django-sage-streaming/archive/refs/tags/0.1.0.tar.gz',
    keywords=['django', 'python', 'streaming', 'video streaming'],
    install_requires=[
        'Django',
        'djangorestframework'
    ]
)
