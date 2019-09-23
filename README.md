# Logs Analysis with SQL

This project is to build a reporting tool which prints out reports in plain text based on the data in the database. It is a Python program using the psycopg2 module to connect to the database.

## How to run：

1. Download the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
2. Ensure Python, the python package [psycopg2](https://pypi.python.org/pypi/psycopg2), [Vagrant](https://www.vagrantup.com/), and [VirtualBox](https://www.virtualbox.org/) are installed. (I used this [vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile).)
3. Download the database dump from [this link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip),unzip, and copy newsdata.sql in the vagrant directory.
4. Open the terminal(I used git bash) and navigate to the vagrant folder, and then enter `vagrant up` to bring the server online and `vagrant ssh` to log in.
5. Navigate to the vagrant directory with `cd /vagrant`  and then enter psql -d news -f newsdata.sql to connect to and run the project database.
6. Enter `python logs_analysis.py` to execute the program.

## Output：
The output of the program will answer the following questions:
1. What are the most popular three articles?
2. Who are the most popular article authors?
3. On which days did more than 1% of requests lead to errors?

You can view the answers in output.txt
