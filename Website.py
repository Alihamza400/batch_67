import streamlit as st

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 1200, "image": "💻"},
    {"id": 2, "name": "Smartphone", "price": 800, "image": "📱"},
    {"id": 3, "name": "Headphones", "price": 150, "image": "🎧"},
    {"id": 4, "name": "Smartwatch", "price": 200, "image": "⌚"}
]

# Initialize session state for cart
if "cart" not in st.session_state:
    st.session_state.cart = []

st.title("🛒 Simple eCommerce Store")

# Display products
st.header("Products")
cols = st.columns(len(products))

for i, product in enumerate(products):
    with cols[i]:
        st.markdown(f"## {product['image']}")
        st.write(f"**{product['name']}**")
        st.write(f"💰 ${product['price']}")
        if st.button(f"Add to Cart {product['name']}", key=product['id']):
            st.session_state.cart.append(product)
            st.success(f"{product['name']} added to cart!")

# Cart section
st.sidebar.header("🛍️ Shopping Cart")
if st.session_state.cart:
    total_price = sum(item['price'] for item in st.session_state.cart)
    for item in st.session_state.cart:
        st.sidebar.write(f"✅ {item['name']} - ${item['price']}")
    st.sidebar.write("---")
    st.sidebar.write(f"### Total: ${total_price}")
    if st.sidebar.button("Checkout"):
        st.session_state.cart = []
        st.sidebar.success("🎉 Purchase Successful!")
else:
    st.sidebar.write("Your cart is empty.")

