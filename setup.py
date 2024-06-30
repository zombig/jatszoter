from setuptools import find_packages, setup

setup(
    name='jatszoter',
    packages=find_packages(),
    package_dir={'': 'src'},
    install_requires=[],
    include_package_data=True,
    package_data={},
    extras_require={
        'dev': ['pytest', 'flake8'],
    },
    entry_points={
        'console_scripts': [
            'jatszoter-server-api=jatszoter.server.api.__main__:main',
            'jatszoter-server-web=jatszoter.server.web.__main__:main',
            'jatszoter-agent=jatszoter.agent.__main__:main',
        ],
    },
)
