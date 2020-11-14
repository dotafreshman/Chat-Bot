# Chat-Bot
## Introduction
Implementation of Chat-bot system, based on BM25 model. 3 of the key files are described below  
* `generateTable.py`this file will generate all the middle table used for other files, like id to text converting, all unique messages and responses or etc  
  * **input to file**`chatbot-replies.2.tsv`,`aggregated-hw3-rating.test.csv`
* `part2b_bm25L.py`this file is according to the part2b of hw3, which will generate 10 responses for each message in `aggregated-hw3-rating.test.csv`. The pipeline is following: for each message, take corresponding response in `chatbot-replies.2.tsv` as corpus, and use BM25 to rank and retrieve the first 10
  * **input to file**`chatbot-replies.2.tsv`,`id_text_all.csv`,`aggregated-hw3-rating.test.csv`
* `app.py`this file is a flask application, which facilitate interactive UI that can actually talk to the user. It uses all responses in `chatbot-replies.2.tsv` as a single corpus to retrieve responses
  * **input to file**`chatbot-replies.2.tsv`
## Document
`hw3report.docx`is report of the programs, `SI_650__Homework_3.pdf` is body of the project requirement
## Dataset
The link to all required dataset in this project is : https://drive.google.com/drive/u/0/folders/1gJBPu7s9kUoWS1u9r5ljlhZnJPLvEbBy
