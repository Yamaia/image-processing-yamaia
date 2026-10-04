from pathlib import Path
from setuptools import find_packages, setup

page_description = Path("README.md").read_text(encoding="utf-8")
requirements = Path("requirements.txt").read_text().splitlines()

setup(
    name="image-processing-yamaia",
    version="0.1.0",
    author="Yamaia",
    author_email="seu-email@exemplo.com",
    description="Pacote de processamento de imagens: diferença, histograma e redimensionamento.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SEU-USUARIO/image-processing-yamaia",
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
