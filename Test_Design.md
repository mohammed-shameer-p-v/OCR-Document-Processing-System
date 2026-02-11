# Test Design Document

## Project: OCR Document Processing System
**Date:** February 11, 2026  
**Prepared By:** MOHAMMED SHAMEER P V  
**College:** YENEPOYA BANGALORE  
**Version:** 1.0  

---

## 1. Test Objective

The objective of this test design document is to validate the functionality, accuracy, and reliability of the OCR Document Processing System in extracting text and structured data from invoice images.

---

## 2. Test Scope

The following functionalities are covered under this testing phase:

- Text extraction from invoice images
- Image preprocessing quality enhancement
- Data field identification (Invoice Number, Date, Amount)
- Error handling for missing or invalid data
- File generation and saving mechanism
- Processing counter functionality
- Support for multiple image formats

---

## 3. Test Environment

**Hardware:**
- 64-bit Processor (Intel/AMD)
- Minimum 8GB RAM
- SSD Storage

**Software:**
- Operating System: Windows 11
- Python Version: 3.12.x
- Tesseract OCR: 5.x
- Streamlit Framework: Latest Stable Version
- OpenCV: Latest Stable Version

**Browser:**
- Google Chrome / Microsoft Edge (Latest Version)

---

## 4. Test Cases

---

### TC01: Invoice Number Extraction

**Objective:** Verify correct extraction of invoice number  
**Priority:** High  
**Precondition:** Valid invoice image is uploaded  

**Test Steps:**
1. Upload invoice containing "Invoice Number: INV-12345"
2. Click "Process" button
3. Observe extracted invoice number

**Expected Result:** Invoice Number = INV-12345  
**Actual Result:** To be filled during test execution  
**Status:** Pass / Fail  

---

### TC02: Date Extraction

**Objective:** Verify correct extraction of invoice date  
**Priority:** High  
**Precondition:** Valid invoice image is uploaded  

**Test Steps:**
1. Upload invoice containing "Date: 11/02/2026"
2. Click "Process" button
3. Observe extracted date

**Expected Result:** Date = 11/02/2026  
**Actual Result:** To be filled during test execution  
**Status:** Pass / Fail  

---

### TC03: Amount Extraction

**Objective:** Verify correct extraction of total invoice amount  
**Priority:** High  
**Precondition:** Valid invoice image is uploaded  

**Test Steps:**
1. Upload invoice containing "Total: $550.00"
2. Click "Process" button
3. Observe extracted amount

**Expected Result:** Amount = 550.00  
**Actual Result:** To be filled during test execution  
**Status:** Pass / Fail  

---

### TC04: Image Enhancement Quality

**Objective:** Verify preprocessing improves OCR accuracy  
**Priority:** Medium  
**Precondition:** Moderate-quality image uploaded  

**Test Steps:**
1. Upload invoice image
2. Click "Process"
3. Compare original and enhanced image
4. Validate readability improvement

**Expected Result:** Enhanced image displays improved contrast and clarity  
**Actual Result:** To be filled during execution  
**Status:** Pass / Fail  

---

### TC05: Missing Data Handling

**Objective:** Verify system handles images without invoice data  
**Priority:** Medium  
**Precondition:** Non-invoice image uploaded  

**Test Steps:**
1. Upload image without invoice information
2. Click "Process"
3. Observe displayed results

**Expected Result:** All fields display "Not Found"  
**Actual Result:** To be filled during execution  
**Status:** Pass / Fail  

---

### TC06: File Format Support

**Objective:** Verify support for PNG, JPG, and JPEG formats  
**Priority:** Medium  
**Precondition:** Valid images available in different formats  

**Test Steps:**
1. Upload PNG format image
2. Upload JPG format image
3. Upload JPEG format image
4. Verify processing and extraction

**Expected Result:** All formats processed successfully  
**Actual Result:** To be filled during execution  
**Status:** Pass / Fail  

---

### TC07: Result File Generation

**Objective:** Verify result file creation and storage  
**Priority:** High  
**Precondition:** Valid invoice processed  

**Test Steps:**
1. Process invoice image
2. Check output folder
3. Open saved file and verify content

**Expected Result:** Result file created in output/ folder containing extracted text and structured data  
**Actual Result:** To be filled during execution  
**Status:** Pass / Fail  

---

### TC08: Processing Counter

**Objective:** Verify counter increments after each process  
**Priority:** Low  
**Precondition:** Application running  

**Test Steps:**
1. Note initial counter value
2. Process one image
3. Verify counter increments
4. Process another image
5. Confirm counter increments again

**Expected Result:** Counter increases by 1 per successful processing  
**Actual Result:** To be filled during execution  
**Status:** Pass / Fail  

---

## 5. Test Data Requirements

- Sample invoice images (PNG, JPG, JPEG)
- Clear printed text images
- Low-quality images for robustness testing
- Non-invoice images for negative testing

---

## 6. Pass / Fail Criteria

**Pass Criteria:**
- All high-priority test cases must pass
- Minimum 80% overall pass rate
- No critical defects identified

**Fail Criteria:**
- Any high-priority test case fails
- Overall pass rate below 80%
- Critical system failure observed

---

## 7. Risk Assessment

**High Risk:**
- Tesseract path configuration errors
- Poor image quality affecting OCR accuracy

**Medium Risk:**
- Regex pattern mismatch for varied invoice formats
- Large image processing performance delays

**Low Risk:**
- Minor UI display issues
- Counter reset on application restart

---

## 8. Test Schedule

- Test Design Preparation: February 11, 2026
- Test Execution: February 11, 2026
- Test Report Submission: February 11, 2026

---

## 9. Approval

**Prepared By:** MOHAMMED SHAMEER P V  
**College:** YENEPOYA BANGALORE  
**Date:** February 11, 2026  
**Status:** Approved for Test Execution
