from setuptools import setup, find_packages


def get_reqs() -> list[str]:
    # Determine requirements from requirements.txt
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()

setup(
    name='DashSchema',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_reqs(),
)
