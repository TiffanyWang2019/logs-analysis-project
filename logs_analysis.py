#!/usr/bin/env python2.7

import psycopg2


DB_NAME = 'news'


def getQuery(query):
    db = psycopg2.connect(database=DB_NAME)
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


QUERY_1 = """SELECT articles.title, COUNT(log.id) as views
             FROM articles
             LEFT JOIN log ON log.path = '/article/' || articles.slug
             GROUP BY articles.title
             ORDER BY views DESC
             LIMIT 3"""


def get_Question1():
    return getQuery(QUERY_1)


QUERY_2 = """SELECT authors.name, COUNT(log.id) as views
             FROM authors
             LEFT JOIN articles ON articles.author = authors.id
             LEFT JOIN log ON log.path = '/article/' || articles.slug
             GROUP BY authors.name
             ORDER BY views DESC"""


def get_Question2():
    return getQuery(QUERY_2)


QUERY_3 = """SELECT to_char(errors.date,'Month DD, YYYY') as date,
                    to_char(((errors.count::decimal/requests.count::decimal)*100),'9.99')
                    || '%' as perc
             FROM (SELECT date(time),count(*) FROM log
                   GROUP BY date(time)) as requests,
                  (SELECT date(time),count(*) FROM log
                  WHERE status LIKE '%404%'
                  GROUP BY date(time)) as errors
             WHERE requests.date = errors.date
             AND ((errors.count::decimal/requests.count::decimal)*100) > 1;"""


def get_Question3():
    return getQuery(QUERY_3)


if __name__ == '__main__':

    articles = get_Question1()
    authors = get_Question2()
    errors = get_Question3()

    print ("1. What are the most popular three articles of all time?")
    for article in articles:
        print ("%s - %d views" % (article[0], article[1]))

    print ("\n2. Who are the most popular article authors of all time?")
    for author in authors:
        print ("%s - %d views" % (author[0], author[1]))

    print ("\n3. On which days did more than 1% of requests lead to errors?")
    for error in errors:
        print ("%s - %s errors" % (error[0], (error[1])))
