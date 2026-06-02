import streamlit as st

st.title("Juice for you ")
st.subheader("you can choose any type of juice you want")
st.subheader("Add type of juice")
juice_type = st.radio("Select type of juice",["mango","Orange","Kiwi","Guava"])
if juice_type :
    st.text("Add size of juice")
    size = st.selectbox("Give the size of juice what do you want ",["Small","Medium","Large","Extra large"])
    add_ice_cream = st.checkbox("Add icecream")
    ice_cream_type = None
    if add_ice_cream:
        ice_cream_type = st.radio("select your ice cream type",["Chocolate","vanilla","Butterscotch"])
        st.write(f"{ice_cream_type}ice cream added to your juice")
    spoon = st.slider("add slider ",0,5,3)
    if spoon >= 3 :
        st.write("You use sugar in high ammount")
    else:
        st.write("You use sugar in right ammount")
    st.text("Before confirming order please recheck your order")
    select_button = st.button("Confirm your order ")
    if select_button:
        st.success("Your order is successful !")
        if add_ice_cream:
            st.write(f"you select a awsome juice type {juice_type} ! ,your {juice_type} juice with size {size} with {spoon} spoon of sugar with {ice_cream_type} icecream is now preparing please wait for few minutes") 
        else:
            st.write(f"you select a awsome juice type {juice_type} ! ,your {juice_type} juice with size {size} with {spoon} spoon of sugar is now preparing please wait for few minutes")