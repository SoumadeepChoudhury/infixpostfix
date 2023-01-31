from setuptools import setup,find_packages

setup(
    name="infix-postfix",
    version="1.0.0",
    author='Ahens | An Initiative to Initial',
    author_email="ahensinitiative@gmail.com",
    packages=find_packages(),
    entry_points={
            'console_scripts':['infix-postfix=infix_postfix.infix_postfix:main',
                               ],
        },
)
