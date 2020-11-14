from rank_bm25 import BM25Plus
import random
import pandas as pd
test = pd.read_csv("aggregated-hw3-rating.test.csv",names=["message_id","response_id"],header=0)
alldata = pd.read_csv("id_text_all.csv",header=0)
tsv = pd.read_csv("chatbot-replies.2.tsv",sep="\t")


def getId(text):
    id = alldata[alldata["text"]==text]["id"].values[0]
    return id

def getText(id):
    text =  alldata[alldata["id"]==id]["text"]

    return text.values[0]

respIdList = tsv["response_id"].unique()
#
# respList = list(map(lambda x:getText(x), respIdList))
respList = tsv["response"].unique()
print(type(respList))


text2id = {}; id2text = {}

# for i in range(len(respList)):
#     text2id[respList[i]] = respIdList[i]
#     id2text[respIdList[i]] = respList[i]
print("字典造好")
# tokenized_corpus = [doc.split(" ") for doc in respList]
# bm25 = BM25Okapi(tokenized_corpus)
print("训练好")
mesIdList = test["message_id"].unique()
midL = []; ridL = []

for mid in mesIdList:
    midL+=[mid for i in range(10)]
    query = getText(mid)
    tokenized_query = query.split(" ")


    corpus = tsv[tsv["message_id"]==mid]["response"].drop_duplicates("first").tolist()
    tokenized_corpus = [str(doc).split(" ") for doc in corpus]
    bm25 = BM25Plus(tokenized_corpus)
    res = bm25.get_top_n(tokenized_query, corpus, n=10)
    res1 = list(map(lambda x:getId(x),res))
    if len(res1)<10:
        res2 = random.sample(list(respIdList),10-len(res1))
    #
    #     remainid = test["response_id"].drop_duplicates(keep="first").values
    #     # print(remainid)
    #     remaincorpus = list(map(lambda x: getText(x), remainid))
    #     tokenized_corpus = [doc.split(" ") for doc in remaincorpus]
    #     bm25 = BM25L(tokenized_corpus)
    #     res = bm25.get_top_n(tokenized_query, remaincorpus, n=10-len(corpusid))
    #
    #     res2 = list(map(lambda x: text2id[x], res))
        res1 = list(res1) + list(res2)
    print(len(res1))
    ridL = list(ridL) + res1

print("mlis len",len(midL))
print("rlis len", len(ridL))
final = pd.DataFrame({"message_id":midL,"response_id":ridL})
final.to_csv("final2.csv",index=False)