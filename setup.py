from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variable as per your requirements -
REPO_NAME = "End-to-End-Book-Recommender-System"
AUTHOR_NAME = "Shariq"
SRC_REPO = "book_recommender"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Shariq",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shariq-0/End-to-End-Book-Recommender-System",
    author_email="isrqdv@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)



