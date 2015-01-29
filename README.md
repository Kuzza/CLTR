# CLTR
Continuous Language Text Recognition

This program provide a rough language classification of a continuous stream of documents, using keyword matching.

The program is configured by giving it a set of languages, and for each language a list of keywords (conf.json file); then it will say for each document which language text it contains (or "I don't know"), based on whether it finds any keywords it knows.
A socket is used for the stream of the documents.
