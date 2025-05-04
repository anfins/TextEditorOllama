import streamlit as st
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
import json
import ollama
from google.cloud import firestore



db = firestore.Client().from_service_account_json("firestorestuff.json")
def main():

    doc_ref = db.collection("entries").document("7sczhziTvkSNLME2d69K")
    doc = doc_ref.get() 

    st.write("The id is: ", doc.id)
    st.write("The contents are: ", doc.to_dict())

    


    
           

if __name__ == "__main__":
    main()