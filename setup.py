from setuptools import setup, find_packages

setup(
    name="github-activity",                     
    version="0.1.0",                       
    author="ry00sh1",                    
    description="CLI for GitHub user activity.",  
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown", 
    url="https://github.com/Ry00sh1/GitHub-User-Activity-CLI",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "github-activity=github_activity.main:main", 
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
