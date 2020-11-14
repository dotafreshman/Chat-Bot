from flask import Flask, render_template, request
from rank_bm25 import BM25Okapi
import pandas as pd
import metapy
app = Flask(__name__)

# def bmhelper(query):
#     results = ranker.score(inv_idx, query, 1)[0]
#     return results


@app.route("/")
def home():

    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    what_the_user_said = request.args.get('msg')
    tokenized_query = what_the_user_said.split(" ")
    # corpus = pd.read_csv("message.csv",names=["m"])
    # corpus = corpus["m"].values.tolist()

    res = bm25.get_top_n(tokenized_query, corpus, n=1)[0]

    #



    # TODO: Design a ranking function that treats what_the_user_said as the
    # query and returns the set of relevant responses to that. Your bot can
    # respond with any relevant response or the most-relevant.
    # See the homework for suggestions on possible rankers.



    return res

if __name__ == "__main__":
    # global inv_idx
    # inv_idx = metapy.index.make_inverted_index('covid_ir-config.toml')
    # global ranker
    # ranker = metapy.index.OkapiBM25()
    # global query
    # query = metapy.index.Document()

    global bm25
    global corpus
    print("please wait patiently, the program is makeing a about 1min training.....")
    corpus = pd.read_csv("chatbot-replies.2.tsv", sep="\t")
    corpus = corpus["response"].drop_duplicates("first").values.tolist()
    tokenized_corpus = [str(doc).split(" ") for doc in corpus]
    bm25 = BM25Okapi(tokenized_corpus)

    # query.content("Hello, Americans")
    # global results
    # results = ranker.score(inv_idx, query, 1)[0]
    
    # IMPLEMENTATION HINT: you probably want to load and cache your conversation
    # database (provided by us) here before the chatbot runs
       
    app.run()
