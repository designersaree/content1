import streamlit as st
import sqlite3
import os

# Create folders
os.makedirs("uploads/images", exist_ok=True)

# Database
conn = sqlite3.connect("database.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS content (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    body TEXT,
    image TEXT,
    price REAL
)
""")
conn.commit()

st.title("📝 Content Selling App")

menu = ["Create Content", "View Content"]
choice = st.sidebar.selectbox("Menu", menu)

# CREATE CONTENT
if choice == "Create Content":
    st.subheader("Create New Content")

    title = st.text_input("Title")
    body = st.text_area("Write your content")
    price = st.number_input("Price (₹)", min_value=0.0)
    image = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    if st.button("Publish"):
        img_path = ""
        if image:
            img_path = f"uploads/images/{image.name}"
            with open(img_path, "wb") as f:
                f.write(image.getbuffer())

        c.execute(
            "INSERT INTO content (title, body, image, price) VALUES (?, ?, ?, ?)",
            (title, body, img_path, price)
        )
        conn.commit()
        st.success("Content published successfully!")

# VIEW CONTENT
elif choice == "View Content":
    st.subheader("Available Content")

    c.execute("SELECT * FROM content")
    rows = c.fetchall()

    for row in rows:
        st.markdown(f"### {row[1]}")
        st.write(f"💰 Price: ₹{row[4]}")

        if row[3]:
            st.image(row[3], width=300)

        st.info("🔒 Pay to unlock full content")
        st.write(row[2][:100] + "...")
        st.markdown("---")
