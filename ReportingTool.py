#!/usr/bin/python3

import psycopg2 as pg

# Task one query
most_popular_article_query = '''
SELECT substring(path from 10),
       count(*) as COUNTER
FROM   log
WHERE  path != '/'
GROUP  BY path
ORDER  BY COUNTER DESC
LIMIT  3
;
'''

# Task two query
most_popular_author_query = '''
SELECT authors.name,
       SUM(seen.counter) AS total
FROM   seen,
       articles,
       authors
WHERE  seen.title = articles.slug
AND    articles.author = authors.id
GROUP  BY authors.name
ORDER  BY total DESC
;
'''

# Task three query
high_errors_query = '''
SELECT *
FROM   results
WHERE  er > 1
;
'''


def most_popular_article(c):

    try:
        c.execute(most_popular_article_query)
        results = c.fetchall()

        for res in results:
            title = res[0].replace('-', ' ').title()
            views = res[1]
            print('      "{}" — {} views'.format(title, views))
    except Exception:
        print('Fail to get data...')


def most_popular_author(c):

    try:
        c.execute(most_popular_author_query)
        results = c.fetchall()

        for res in results:
            name = res[0].replace('-', ' ').title()
            views = res[1]
            print('      "{}" — {} views'.format(name, views))
    except Exception:
        print('Fail to get data...')


def higher_error_day(c):

    try:
        c.execute(high_errors_query)
        results = c.fetchall()

        for res in results:
            date = res[0]
            percent = res[1]
            print("      {:%B %d,%Y} — {:0.1f}% errors".format(date, percent))
    except Exception:
        print('Fail to get data...')


if __name__ == '__main__':

    with pg.connect(dbname='news') as conn:
        c = conn.cursor()

        print('\n  -- Most Popular Three Articles --\n')
        most_popular_article(c)

        print('\n\n  -- Most Popular Authors --\n')
        most_popular_author(c)

        print('\n\n  -- Days Have More Then 1% Errors in Requests --\n')
        higher_error_day(c)
        print()
