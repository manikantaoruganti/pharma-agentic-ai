from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pharma-agentic-ai",
    version="0.1.0",
    author="Team P16",
    description="Agentic AI for Pharmaceutical Drug Discovery - EY Techathon 6.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/manikantaoruganti/pharma-agentic-ai",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "fastapi>=0.104.0",
        "uvicorn>=0.24.0",
        "langchain>=0.1.0",
        "openai>=1.0.0",
        "psycopg2-binary>=2.9.0",
        "pymongo>=4.5.0",
        "redis>=5.0.0",
        "aiohttp>=3.9.0",
        "pydantic>=2.0.0",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
        "reportlab>=4.0.0",
    ],
)
