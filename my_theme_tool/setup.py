from setuptools import setup, find_packages

setup(
    name='my_theme_tool',
    version='0.1.0',
    description='A tool to find the most similar theme.css file using TF-IDF',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
    ],
    entry_points={
        'console_scripts': [
            'my_theme_tool=my_theme_tool.main:main',
        ],
    },
)
