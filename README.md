Koding Challenge
=====================

Welcome to Koding Challenge. Before getting into details of the problem,
please be aware that the challenge is designed to identify the strongest skills
of engineers with different backgrounds. As a result, it is an end-to-end problem
with different tasks you can pick from. We strongly suggest you only pick one or two
tasks. We expect you to spend **2-4 hours** and that the implemented parts are production-ready. If it is not the
case, please explain the underlying reasons.

Imagine you inherited this project from someone that has left the company and you
have no idea how the service was deployed. Maybe he used good old FTP to copy files
to a server! The code provided is intentionally crap. You may need a better algorithm.
It is in python, but you may use any language of your choice as long as you provide
a good way to run the tests.

We would like to improve this service in the following areas:

* We would like a solution that is stable, scalable and maintainable.
* We would like to have some kind of monitoring that helps us in identifying issues.
* We would like a production ready HTTP server and a good API.
* We would like an efficient (fast) algorithm.
* We would like to deploy the service to a cloud provider and automate the deployment.
* We would like the API to be backward compatible.

Before you begin coding, choose one or two tasks from the above and break them into
smaller pieces, do a time estimation and keep a record of it. We need that as part
your answer. It is up to you how much time you invest, but keep in mind that we expect
some meaningful contribution.

Last but not least, even if you decided not to invest time in this task, please share
with us your feedback. What was the most enjoyable and what was annoying? Let us know
so we can improve.

Problem Definition
==================
The challenge is to build an API to offer a basic spell checking service. People will
use the API to offer corrections when people type in text fields.

## Most frequent spelling mistakes

* Deletion: One character in the string gets deleted incorrectly. Example: `Ordnary` instead of `Ordinary`.
* Replacement: One character in the string is incorrectly replaced by another one. Example: `Accedent` instead of `Accident`.
* Transposition: Swapping one pair of consecutive characters. Example: `invovle` instead of `involve`.
* Insertion: The user ends up inserting one extra character somewhere in the string. Example: `Heello` instead of `Hello`.

So, generally, the correct string is just one step of one edit distance away from what the user erroneously types in.

Please take note:
* In each of the four popular cases above, the mistake occurs only at *one* particular character (or, pair of characters in case 3).
* Assume only the letters *a-z* are involved.

## Corpus

A corpus is provided in this repo which is used to build a dictionary of words. Words are strings of letters and they may
contain hyphens and/or apostrophes. The end of the corpus is marked by "END-OF-CORPUS".

## API request/response

The API should recommend the likeliest known word from the dictionary for each of the mistyped words it receives. If given word
has no spelling errors or is not found in the dictionary, it should return it as is.

* The request has a parameter for accepting a word.
* The response must be a json document with the corrected spelling.
* When suggesting a correction, it should be the best possible suggestion (think of it as the most frequent word in the corpus).

## Tests

There is a sample test case. Make sure the test passes. If you are using another programming language, make it easy to run the test.

Requirements
============

Make sure you install the following python packages for the default implementation to work.

* flask
* python-Levenshtein
* pytest


## Run the tests
 
To run the default tests use:
```
python -m pytest --durations=0 tests
```
