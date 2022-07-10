
# the first word-breaking method
# hmm

Step 1.
    # convert token to id
    python CreateLexicon.py

Step 2.
    # gen lang model
    python BiLMTrain.py

Step 3.
    # viterbi
    python ViterbiCWS.py

------------- 

# the second word-breaking method
# length match

Step 1.
    # dict search
    python BMM.py

