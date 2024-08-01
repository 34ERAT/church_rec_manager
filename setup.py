from setuptools import setup, find_packages
from setuptools.command.install import install


setup(
    name='church_rec_manager',
    version='0.3.0',
    description='python application to manage your records of the church',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='philip kanuti',
    author_email='kanutiphilip24@gmail.com',
    url='https://github.com/34ERAT/church_rec_manager.git',
    packages=find_packages(),
    install_requires=[
        "attrs==23.2.0",
        "autopep8==2.3.1",
        "Babel==2.15.0",
        "contextlib2==21.6.0",
        "CTkMessagebox==2.7",
        "CTkTable==1.1",
        "customtkinter==5.2.2",
        "darkdetect==0.8.0",
        "execnet==2.1.1",
        "greenlet==3.0.3",
        "iniconfig==2.0.0",
        "jsonschema==4.23.0",
        "jsonschema-specifications==2023.12.1",
        "mock==5.1.0",
        "msgpack==1.0.8",
        "mysql-connector-python==9.0.0",
        "packaging==24.1",
        "path==17.0.0",
        "path.py==12.5.0",
        "pillow==10.4.0",
        "pluggy==1.5.0",
        "psutil==6.0.0",
        "pycodestyle==2.12.0",
        "PyMySQL==1.1.1",
        "pynvim==0.5.0",
        "pytest==8.3.2",
        "pytest-shutil==1.7.0",
        "python-dotenv==1.0.1",
        "referencing==0.35.1",
        "rpds-py==0.19.0",
        "six==1.16.0",
        "termcolor==2.4.0",
        "tk==0.1.0",
    ],
    entry_points={
        'console_scripts': [
            'church_rec_manager=Church_rec_manager.church_rec:Main',

        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    # cmdclass={
    #     'install': CustomInstallCommand,
    # }
)

