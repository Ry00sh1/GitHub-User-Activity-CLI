from setuptools import setup, find_packages

setup(
    name="github-activity",                     
    version="0.1.0",                       
    author="ry00sh1",                    
    description="CLI for GitHub user activity.",  
    url="https://github.com/Ry00sh1/GitHub-User-Activity-CLI",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "github-activity=github_activity.main:main", 
        ],
    }
)
