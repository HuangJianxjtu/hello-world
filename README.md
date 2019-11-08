# Notes

## How to setup python3 environment in Ubuntu

### 1.set python3, pip3 as the default python,pip

add `alias python=python3` and `alias pip=pip3` to ~/.bashrc
run `source ~/.bashrc`

### 2.install numpy, matplotlib

#### 2.1 use pip to install(Recommended)

`pip install numpy scipy matplotlib`

#### 2.2 use apt-get to install

`sudo apt-get install python3-numpy python3-scipy python3-matplotlib`

#### 2.3 Test

run python in the terminal, and run `import numpy`,`import matplotlib`. if there isn't any warnning, those libraries is well installed.
