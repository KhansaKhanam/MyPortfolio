import streamlit as st
import pandas as pd
from PIL import Image
from PIL import Image
import streamlit.components.v1 as components

option = ""

def select(option):
	DisplayPart(option)
def Abstract():
	st.header("Abstract", divider='blue')
	st.write(""" Amazigh languages, spoken by 14 million people across North Africa, face challenges in preservation and technological integration. This project develops an Amazigh-to-English translation system using Seq2Seq, Transformer, fine-tuned Helsinki-NLP models, and Google Translate API. The fine-tuned pre-trained Transformer Helsinki-NLP model achieved the highest BLEU score (49.27), highlighting its potential for under-resourced languages, despite having only Romanized support. Challenges faced in this project include limited data and lack of Tifinagh script support. This emphasizes the need for more resources to preserve Amazigh’s linguistic identity through technology.""")
def DisplayPart(option):
	if option == "Abstract":
		Abstract()
	elif option == "Introduction":
		Intro()
	elif option == "DataPrep/EDA":
		DataCleaning()
	elif option == "Clustering":
		Clustering()
	elif option == "ARM":
		ARM()
	elif option =="LDA":
		LDA()
	elif option == "SVM":
		SVM()
	elif option == "DT":
		DT()
	elif option == "NB":
		NB()
	elif option =="NN":
		NN()
	elif option =="Conclusions":
		Conclusions()
	else:
		st.write("Work in Progress")
st.title("Amazigh to English Language Translation | Preserving and Honoring the Amazigh Identity.")


header = st.container()
with header:
	option = st.selectbox("", ("Abstract","Introduction", "DataPrep/EDA", "Clustering", "ARM","LDA","DT","NB","SVM", "NN","Conclusions"))
header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)
select(option)
### Custom CSS for the sticky header
st.markdown(
    """
<style>
    div[data-testid="stVerticalBlock"] div:has(div.fixed-header) {
        position: sticky;
        top: 2.875rem;
        z-index: 999;
	background-color: #0c1415;
    }
    .fixed-header {
        border-bottom:1px ;
    }
</style>
    """,
    unsafe_allow_html=True
)
