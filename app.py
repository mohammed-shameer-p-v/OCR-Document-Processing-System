import streamlit as st
import pytesseract
from PIL import Image
import cv2
import numpy as np
from datetime import datetime
import re
import os

# Windows users - set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\muham\OneDrive\Desktop\Tesseract-OCR\tesseract.exe'

st.set_page_config(page_title="OCR Processor", page_icon="📄", layout="wide")

if 'count' not in st.session_state:
    st.session_state.count = 0

def preprocess_image(image):
    img = np.array(image.convert('RGB'))
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray)
    _, thresh = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return Image.fromarray(thresh)

def extract_data(text):
    data = {
        'invoice_number': 'Not Found',
        'date': 'Not Found',
        'amount': 'Not Found'
    }
    
    inv_match = re.search(r'Invoice[:\s#]*([A-Z0-9-]+)', text, re.IGNORECASE)
    if inv_match:
        data['invoice_number'] = inv_match.group(1)
    
    date_match = re.search(r'(\d{1,2}[-/]\d{1,2}[-/]\d{2,4})', text)
    if date_match:
        data['date'] = date_match.group(1)
    
    amount_match = re.search(r'Total[:\s]*\$?\s*(\d+\.?\d*)', text, re.IGNORECASE)
    if amount_match:
        data['amount'] = amount_match.group(1)
    
    return data

# UI
st.title("📄 OCR Document Processor")
st.markdown("**TCS Industry Project**")
st.divider()

with st.sidebar:
    st.header("📊 Stats")
    st.metric("Processed", st.session_state.count)

uploaded_file = st.file_uploader("📤 Upload Image", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, width=400, caption="Original")
    
    if st.button('🔍 Process', type='primary'):
        with st.spinner('Processing...'):
            try:
                processed_img = preprocess_image(image)
                st.image(processed_img, width=400, caption="Enhanced")
                
                text = pytesseract.image_to_string(processed_img)
                
                if text.strip():
                    st.subheader("📝 Extracted Text")
                    st.text_area("", text, height=200)
                    
                    data = extract_data(text)
                    
                    st.subheader("📊 Data")
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Invoice", data['invoice_number'])
                    col2.metric("Date", data['date'])
                    col3.metric("Amount", data['amount'])
                    
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"output/result_{timestamp}.txt"
                    
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(f"TEXT:\n{text}\n\n")
                        f.write(f"DATA:\n{data}\n")
                    
                    st.session_state.count += 1
                    st.success(f"✅ Saved to {filename}")
                else:
                    st.error("❌ No text found")
            except Exception as e:
                st.error(f"Error: {str(e)}")
else:
    st.info("👆 Upload an image to start")