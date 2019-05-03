# Batch Connect - Example Hello World Server

![GitHub Release](https://img.shields.io/github/release/accre/bc_example_hello.svg)
![GitHub License](https://img.shields.io/github/license/accre/bc_example_hello.svg)

An example Batch Connect app that launches a Hello World server within a
batch job.

The purpose of this app is to provide a relatively simple example of a Batch
Connect app using a small server script requiring only a minimal Python3 install
that can be modified to understand the workings of a Batch Connect application
from the compute node to the browser. A simple Jupyter-like authentication scheme
is also provided.

## Prerequisites

This Batch Connect app requires the following software be installed on the
**compute nodes** that the batch job is intended to run on (**NOT** the
OnDemand node):

- [OpenSSL](https://www.openssl.org/) 1.0.1+ (used to hash the Hello World
  server password)

- [Python 3](https://www.python.org/downloads/) (used to run a the simple
  Hello World server)


## Install

These are command line only installation directions.

We start by downloading a zipped package of this code. This allows us to start
with a fresh directory that has no git history as we will be building off of
this.

```sh
# Download the zip from the GitHub page
wget https://github.com/accre/bc_example_hello/archive/master.tar.gz

# Create a catchy directory
mkdir my_hello_app

# Unzip the downloaded file into this directory
tar xzvf master.tar.gz -C my_hello_app --strip-components=1

# Change the working directory to this new directory
cd my_hello_app
```

From here you will make any modifications to the code that you would like and
version your changes in your own repository:

```sh
# Version our app by making a new Git repository
git init

#
# Make all your code changes while testing them in the OnDemand Dashboard
#
# ...
#

# Add the files to the Git repository
git add --all

# Commit the staged files to the Git repository
git commit -m "my first commit"
```

## Contributing

1. Fork it ( https://github.com/accre/bc_example_hello/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
