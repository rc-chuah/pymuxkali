#!/bin/env python

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name="pymuxkali",
      version="1.6",
      description="This is a python script by which you can install Kali Nethunter (Kali Linux) in your termux application without rooted phone.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/rc-chuah/pymuxkali",
      author="RC Chuah",
      author_email="raynersec@gmail.com",
      license="GNU General Public License v3 (GPLv3)",
      keywords=["kali", "kalilinux", "kalinethunter", "infosec", "cybersec", "infosecurity", "cybersecurity"],
      packages=["pymuxkali"],
      entry_points={
          "console_scripts": [
                "pymuxkali = pymuxkali.pymuxkali:main",
          ]
      },
      project_urls={
          "Source": "https://github.com/rc-chuah/pymuxkali",
          "Source": "https://github.com/RaynerSec/pymuxkali",
      },
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "Intended Audience :: Information Technology",
          "Intended Audience :: System Administrators",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Natural Language :: English",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 3",
          "Operating System :: Android",
          "Topic :: Security",
          "Topic :: Utilities",
      ],
      zip_safe=False
)
