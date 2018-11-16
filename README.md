# FSND Repoting Tool (Project1)

  A tool used to analyse server database and provide informatio about:
  - Best writers
  - Best articles
  - Errors occurance

## Getting Started

  This tool is used to analyse database, so it is require a data base first to work on.

  this tool works only on FSND "news" database.

### Prerequisites

  You will need the following:
  * Virtual Machine softwere.
  * Vgrant with Ubuntu installed.
  
  You can download VM from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)  
  And you cand download Vagrant [here](https://www.vagrantup.com/downloads.html)

  Inside your new environment *Ubuntu* you will need:
  * Python 3.6.
  * PostgreSQL.
  
  
### Installing

  After downloading this project add it tou your Vagrant files, run Vagrant 
```
$ vagrant up
```
  and then
```
$ vagrant ssh
```
Switch the path to the files you have just added and run it using Python 3.7
```
$ Python3 [your file name]
```


You should see results like this
```

  -- Most Popular Three Articles --

 "Candidate Is Jerk" — 338647 views
 "Bears Love Berries" — 253801 views
 "Bad Things Gone" — 170098 views


  -- Most Popular Authors --

 "Ursula La Multa" — 507594 views
 "Rudolf Von Treppenwitz" — 423457 views
 "Anonymous Contributor" — 170098 views
 "Markoff Chaney" — 84557 views


  -- Days Have More Then 1% Errors in Requests --

 July 17,2016 — 2.3% errors

```

## Code Styling

Pyhton code is wrtitten according to [pep8](https://www.python.org/dev/peps/pep-0008/)

and the code is tested to be applicable for this styling method using the library [pycodestyle](https://pycodestyle.readthedocs.io/en/latest/)

To run the test use
~~~
$ pycodestyle [your file name]
~~~
and there should be no output if your code is well styled.

## Used Views

Views is important in SQL Queries, in order to make the SQL query more readable.

Four Views are used in this project:

1. **seen**

This view is used in second query, it it shows articles slug and the number of time an artice is requested.

```
CREATE VIEW seen AS
SELECT substring(path from 10) as title,count(*) as counter
FROM log 
WHERE path != '/'
GROUP BY path
;
```

2. **errors**

This view is used in the fourth view, it shows how many fail request were there in each day.

```
CREATE VIEW errors AS
SELECT time::date AS Day, count(*)
FROM log
WHERE status LIKE '%404%'
GROUP BY Day
;
```

3. **allRequests**

This view is used in the forth view, it shows haw many requests were there in each day in total (whether it succeeded or not).

```
CREATE VIEW allRequests AS
SELECT time::date AS Day, count(*)
FROM log
GROUP BY Day
;
```

4. **results**

This view is used in the third query, it shows every day and the percentage of error in that day.

```
CREATE VIEW results AS
SELECT errors.day,(CAST(errors.count AS REAL)/allRequests.count) * 100 AS er
FROM errors JOIN allRequests
ON errors.day = allRequests.day
;
```

## Author

* **Abdullah Alamoodi** - [Github](https://github.com/abady1000)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* **Mashael ElSaeed** - Course instructor
