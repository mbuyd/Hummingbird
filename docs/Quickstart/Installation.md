# Installing Hummingbird

## Environment

### Python Version

Hummingbird supports a minimum of Python 3.5 and a maximum of Python 3.7 with all options enabled, and Python 3.8 with machine learning disabled.

### Dependencies

The following distributions will be automatically installed with downloading and installing Hummingbird.

* [Fabric](https://www.fabfile.org/) is a high level Python library designed to execute shell commands remotely over SSH.
* [Flask](https://www.palletsprojects.com/p/flask/) is a lightweight WSGI web application framework.
* [Flask WTF](https://flask-wtf.readthedocs.io/en/stable/) integrates WTForms into Flask. It requires WTForms to be installed as well.
* [Numpy](https://numpy.org/) is the fundamental package for scientific computing with Python.
* [Pandas](https://pandas.pydata.org/) is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
* [SciPy](https://www.scipy.org/) is a Python-based ecosystem of open-source software for mathematics, science, and engineering.
* [statsmodels](https://www.statsmodels.org/stable/index.html) is a Python module that provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests, and statistical data exploration.
* [WTForms](https://wtforms.readthedocs.io/en/stable/) is a flexible forms validation and rendering library for Python web development.

#### Optional Dependencies

* [Coverage](https://github.com/nedbat/coveragepy) helps the Hummingbird team have good code coverage and make sure that our code works as it should.
* [Flask SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and Object Relational Mapper for Flask. It is only necessary if you are using SQL.
* [Keras](https://keras.io/) is a high-level neural networks API, written in Python and capable of running on TensorFlow. It is only necessary if you are using Hummingbird with machine learning.
* [Matplotlib](https://matplotlib.org/) is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. It is only necessary if you are using Hummingbird with machine learning.
* [scikit-learn](https://scikit-learn.org/stable/) is a collection of simple and efficient tools for predictive data analysis in Python. It is only necessary if you are using Hummingbird with machine learning.
* [TensorFlow](https://www.tensorflow.org/) is an end-to-end open source platform for machine learning. It is only necessary if you are using Hummingbird with machine learning.
* [Theano](http://deeplearning.net/software/theano/) is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently. It is only necessary if you are using Hummingbird with machine learning.

### Virtual Environments

You can use a virtual environment to manage the dependencies for your project, both in development and in production. However, it is not necessary as these packages do not often have conflicts (with the exception of machine learning packages) and production is often already containerized.

You can read the [Flask documentation here](https://flask.palletsprojects.com/en/1.1.x/installation/#virtual-environments) on virtual environments if you are curious what problems a virtual environment may solve for you, since they will separate your Python project into its own separate group which may be of benefit to you.

You can use `venv	` in order to initialize a Python virtual environment, since Hummingbird requires Python 3.5 or newer. Do not follow Python 2 instructions for creating a virtual environment as directed by Flask, which is a dependency of Hummingbird.

#### Fast Installation

You can create a quick virtual environment in Python 3 by first creating a project folder with structure:

```bash
mkdir ProjectName
cd ProjectName
python -m venv venv
```

and then you can activate it by running

```bash
. venv/bin/activate
```

In Windows, you would run the same commands to create a project folder, but you activate it with the following script instead:

```bash
venv\Scripts\Activate.bat
```

### Getting Packages

After creating a virtual environment or using your main development environment, you can simply run:

```bash
pip install -r requirements.txt
```

