from setuptools import setup,find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="infix-postfix",
    version="1.0.0",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ahens | An Initiative to Initial',
    author_email="ahensinitiative@gmail.com",
    url="https://github.com/SoumadeepChoudhury/infixpostfix",
    packages=find_packages(),
    entry_points={
            'console_scripts':['infix-postfix=infix_postfix.infix_postfix:main',
                               ],
        },
)
