import setuptools

setuptools.setup(
    name="flaskPythonApp",
    version="0.0.1",
    author="Daryl Hughes",
    author_email="dhughesni",
    description="A small example package",
    packages=setuptools.find_packages(),
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        'flaskPythonApp',
    ],
    entry_points={
        'console_scripts': [
            'flaskPythonApp = flaskPythonApp.cli:cli'
        ]
    },
)
