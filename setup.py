import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="infix-postfix",
    version="1.2.0",
    description="Converts Infix to Postfix and vice versa...",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/SoumadeepChoudhury/infixpostfix",
    author="Ahens | An Initiative to Initial (Soumadeep Choudhury)",
    author_email="ahensinitiative@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    keywords=[
        'python',
        'arithmetic',
        'tools',
        'arith-tools',
        'arithmetic operations',
        'Math',
        'python3',
        'pip',
        'pip3',
        'fibonacci',
        'armstrong',
        'boiled-egg',
        'terrace',
        'unique',
        'amicable',
        'infix',
        'postfix',
        'infix2postfix',
        'infixtopostfix',
        'infix-postfix',
        'infix_postfix'
    ],
    entry_points={
        'console_scripts': ['infix-postfix=infix_postfix.infix_postfix:main',
                            ],
    },
)
