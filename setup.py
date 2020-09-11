from setuptools import (
    setup,
    find_packages
)

about = {}
with open("pysingleton/__about__.py") as fp:
    exec(fp.read(), about)

with open("README.md", "r") as fp:
    long_description = fp.read()

setup(name='python-singleton-metaclasses',
      version=about["__version__"],
      description=about["__summary__"],
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="Zachary Cutlip",
      author_email="uid000@gmail.com",
      url="https://github.com/zcutlip/py-singleton-metaclasses",
      license="MIT",
      packages=find_packages(),
      python_requires='>=3.7',
      install_requires=[],
      package_data={'pysingleton': ['config/*']},
      )
