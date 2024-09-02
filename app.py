import streamlit as st
import pandas as pd
#Printing Statement with emoji

st.write("Hello, *World!* :sunglasses:")

st.title("Welcome to My Streamlit App")

# Header
st.header("This is a Header")

# Subheader
st.subheader("This is a Subheader")

# Regular text
st.text("This is some regular text.")

# Markdown text
st.markdown("""
### Markdown Section
You can use **markdown** to format text with different styles such as *italic*, **bold**, or `code`.

- Bullet list item 1
- Bullet list item 2

1. Numbered list item 1
2. Numbered list item 2
""")

# Caption
st.caption("This is a caption for additional context.")

# Code block
st.code("""
# Sample Python code
def hello_world():
    print("Hello, World!")
""", language='python')

# Display LaTeX equations
st.latex(r'''
E = mc^2
''')

arr = pd.DataFrame({
    'one':[1,2,3,4],
    'two':[6,7,8,9]
})
st.write(arr)

st.metric(label="Temperature",value="31 ° C",delta="1.2 ° C")
st.metric(label="Population",value="123 Billions",delta="1 Million")

st.bar_chart(arr)
st.line_chart(arr)
st.area_chart(arr)