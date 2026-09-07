# SparkPipelineFramework
Framework for simpler Spark Pipelines


# Publishing package 
For credentials:

Set up your $HOME/.pypirc file like this (replace password with your real PyPI API token, generated from https://pypi.org/manage/account/token/):

```
[pypi]
  username = __token__
  password = <your-pypi-api-token>
```

Then:

Increment version in VERSION file

Run ```make package```


# Developer Setup

`spark.Dockerfile` pulls its `helix.spark` base image from b.well's private
services-account ECR (`856965016623.dkr.ecr.us-east-1.amazonaws.com`), so the dev/test
container needs AWS access. Log in first:

```
aws sso login --profile services
make ecr-login
```

`make up`, `make devdocker` and `make build` depend on `ecr-login`, so it also runs
automatically. Override the profile name with `AWS_SERVICES_PROFILE=<name>` if yours
differs.

`make run-pre-commit` needs **no** AWS access — `pre-commit.Dockerfile` stays on
`public.ecr.aws`, so linting and formatting still work for forks and outside
contributors. Running the Spark test suite (`make up` / `make tests`) does require
b.well AWS access.

Then run ```make devsetup```

Install following PyCharm plugins:
1. MyPy: https://plugins.jetbrains.com/plugin/11086-mypy


# Installing Spark

1. Install SDKMan
curl -s "https://get.sdkman.io" | bash

2. list Java versions available
sdk list java

2. Install Java SDK
# sdk install java 8.0.265-zulu
# sdk install java 11.0.8-zulu
# sdk install java 11.0.2-open
sdk install java 11.0.8.hs-adpt

3. Close your terminal window so it updates

3. 6. Check your install
echo $JAVA_HOME
java -version
javac -version

4. Install Scala
sdk list scala
sdk install scala 2.12.12

5. Install Spark
(Current version sdkman is still 2.x)

3. install homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

4. Install wget
brew install wget

5. download spark
```
wget http://archive.apache.org/dist/spark/spark-3.0.0/spark-3.0.0-bin-hadoop3.2.tgz
mkdir -p /usr/local/opt/spark
rm -r /usr/local/opt/spark/
mkdir -p /usr/local/opt/spark
tar -zxvf spark-3.0.0-bin-hadoop3.2.tgz -C /usr/local/opt/spark
cp -a /usr/local/opt/spark/spark-3.0.0-bin-hadoop3.2/ /usr/local/opt/spark/
rm -r /usr/local/opt/spark/spark-3.0.0-bin-hadoop3.2
```

6. Update your `~/.bash_profile` to include SPARK_HOME path:
```
export SPARK_HOME="/usr/local/opt/spark"
export PATH="$SPARK_HOME/bin:$PATH"
```

7. Reload bash_profile
```source ~/.bash_profile```

7. Test Spark install
spark-submit --class org.apache.spark.examples.SparkPi /usr/local/opt/spark/examples/jars/spark-examples_2.12-3.0.0.jar
