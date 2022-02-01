from setuptools import setup, find_packages


setup(
    name="api",
    version="0.1.0",
    packages=find_packages(),
    description="Flask RESTful API project",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    url="",
    include_package_data=True,
    install_requires=['flask', 'flask-restful', 'celery', 'redis', 'requests', 'lxml', 'bs4']
)
