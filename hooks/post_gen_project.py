import os

directory = '{{ cookiecutter.__package.replace('.','/') }}'
srcDir = 'src/main/java/' + directory
testDir = 'src/test/java/' + directory

os.makedirs(srcDir, exist_ok=True)

if '{{ cookiecutter.junit }}' == 'yes':
	os.makedirs(testDir, exist_ok=True)

os.rename("Main.java", srcDir + '/Main.java')

os.system('mvn wrapper:wrapper')

os.system('./mvnw verify')

