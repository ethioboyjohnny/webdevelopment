import streamlit as st
import requests
import random

st.title("Origami Crane Tutorial")  


#NEW: multi select box for user to choose a difficulty level
difficulty = st.selectbox("Choose a difficulty level", ["Beginner", "Intermediate", "Advanced"])

#random trivia fact
def get_trivia_fact():
    response = requests.get("https://musely.ai/tools/random-facts-generator?topic=origami")
    fact = response.text
    return fact

#displaying a trivia fact
st.write("Did you know?")
st.write(get_trivia_fact())

#instructions based on difficulty level
if difficulty == "Beginner":
    steps = [
        "1. Start with a square piece of paper.",
        "2. Fold the paper diagonally in both directions and unfold.",
        "3. Fold the paper in half horizontally and vertically, then unfold.",
        "4. Fold the corners into the center to form a smaller square.",
        "5. Fold the side corners to the center and unfold.",
        "6. Open the top flap and fold it down to the bottom edge, forming a kite shape.",
        "7. Repeat on the other side.",
        "8. Fold the top flaps outward to form the wings.",
        "9. Fold the bottom point upward to form the head.",
        "10. Shape the head and tail to complete your crane."
    ]
    image_url = "https://static.neatorama.com/images/2008-07/frustration-origami.jpg"  
    prompt= "This might be challenging, but don't give up!"
elif difficulty == "Intermediate":
    steps = [
        "1. Start with a square piece of paper.",
        "2. Fold the paper diagonally in both directions and unfold.",
        "3. Fold the paper in half horizontally and vertically, then unfold.",
        "4. Fold the corners into the center to form a smaller square.",
        "5. Fold the side corners to the center and unfold.",
        "6. Open the top flap and fold it down to the bottom edge, forming a kite shape.",
        "7. Repeat on the other side.",
        "8. Fold the top flaps outward to form the wings.",
        "9. Fold the bottom point upward to form the head.",
        "10. Shape the head and tail to complete your crane.",
        "11. Add more detailed folds to enhance the crane's wings and tail."
    ]
    image_url = "https://i.ytimg.com/vi/fzNwka1Xs2Q/hqdefault.jpg"  
    prompt= "Take it slowly and you got this!"
else:
    steps = [
        "1. Start with a square piece of paper.",
        "2. Fold the paper diagonally in both directions and unfold.",
        "3. Fold the paper in half horizontally and vertically, then unfold.",
        "4. Fold the corners into the center to form a smaller square.",
        "5. Fold the side corners to the center and unfold.",
        "6. Open the top flap and fold it down to the bottom edge, forming a kite shape.",
        "7. Repeat on the other side.",
        "8. Fold the top flaps outward to form the wings.",
        "9. Fold the bottom point upward to form the head.",
        "10. Shape the head and tail to complete your crane.",
        "11. Add more detailed folds to enhance the crane's wings and tail.",
        "12. Create intricate folds to refine the crane's neck and beak for a more realistic look."
    ]
    image_url = "https://cdn-ak.f.st-hatena.com/images/fotolife/n/nativecamp_blog/20210610/20210610134627.jpg"  
    prompt= "This will be easy for you!"
    
#NEW: display the steps with user option to hide/show each step
for step in steps:
    if st.checkbox(step, value=True):
        st.write(step)
    else:
        pass

#NEW: allow user to input the type of paper they are using
paper_type = st.text_input("What type of paper are you using?")
if paper_type:
    st.write(f"Great! You're using {paper_type}. Let's get started with folding. {prompt}")
    st.image(image_url, caption=f"{paper_type.capitalize()} paper", width=200)  

#refresh trivia fact
if st.button("Get another trivia fact"):
    st.write("Here's another interesting fact for you:")
    st.write(get_trivia_fact())
