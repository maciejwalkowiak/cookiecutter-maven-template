import os

directory = '{{ cookiecutter.groupId.replace('.','/') + '/' + cookiecutter.artifactId }}'
srcDir = 'src/main/java/' + directory
testDir = 'src/test/java/' + directory

os.makedirs(srcDir, exist_ok=True)
os.makedirs(testDir, exist_ok=True)

os.rename("Main.java", srcDir + '/Main.java')

os.system('mvn wrapper:wrapper')

os.system('./mvnw package')

