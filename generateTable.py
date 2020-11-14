import pandas as pd

tsv = pd.read_csv("chatbot-replies.2.tsv",sep="\t")

test = pd.read_csv("aggregated-hw3-rating.test.csv")
test.columns = ["message_id","response_id"]


###########response_id, response
testresponse = pd.merge(test, tsv, on=["response_id"],how="left")
testresponse.drop_duplicates("response_id","first",inplace=True)
testresponse[["response_id","response"]].to_csv("test_idtext.csv",index=False)

#######################id, text
test = pd.read_csv("aggregated-hw3-rating.test.csv")
test.columns = ["message_id","response_id"]

a = test["message_id"]
a2 = pd.merge(a, tsv, on=["message_id"],how="left")[["message_id","message"]]

a2.columns = ["id","text"]
b = test["response_id"]
b2 = pd.merge(b, tsv, on=["response_id"],how="left")[["response_id","response"]]
# b2 = b2
print(b2.columns)
b2.columns = ["id","text"]
# print(a.columns)
# print(b.columns)
id_text = pd.concat([a2, b2], ignore_index=True)
id_text.drop_duplicates("id","first",inplace=True)
# print(len(id_text))
id_text.to_csv("id_text_test.csv",index=False)
######################message
# mes = tsv["message"].drop_duplicates("first")
# mes.to_csv("message_query.csv",index=False,header=False)
testmessage = pd.merge(test, tsv, on=["message_id"],how="left")
testmessage.drop_duplicates("message_id","first",inplace=True)
testmessage["message"].to_csv("message_query.csv",index=False,header=False)
#####################response

rep = testresponse["response"].drop_duplicates("first")
rep.to_csv("message.csv",index=False,header=False)
