with open('input.txt') as f:
    package_list = f.readlines()

packages = []
for package in package_list:
    packages.append(int(package))

print(len(packages))