from setuptools import find_packages,setup

def read_requirements(file_path='requirements.txt'):
    with open(file_path, 'r') as file:
        lines = [
            line.strip()
            for line in file
            if line.strip() and not line.startswith('#') and line.strip() != '-e .'
        ]
    return lines

setup(
    name='mlproject',
    version='0.0.1',
    author='Avronil',
    packages=find_packages(),
    install_requires=read_requirements()
)



# Example usage
requirements = read_requirements()
print(requirements)
