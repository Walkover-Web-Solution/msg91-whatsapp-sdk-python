from setuptools import setup, find_packages

setup(
    name='msg91-whatsapp-SDK',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python SDK for interacting with MSG91 WhatsApp API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/msg91-whatsapp-SDK',
    packages=find_packages(),
    install_requires=[
        'requests>=2.20.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
