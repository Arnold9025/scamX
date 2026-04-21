# 🛡️ Scam Detection App (MVP)

An intelligent application that detects scams across **messages, emails, screenshots, and images**, and clearly explains **why** they are suspicious.

---

## 🚀 Overview

This project is designed to help users identify and understand potential scams by analyzing various types of content:

- 📩 Emails  
- 💬 Text messages (SMS)  
- 🖼️ Screenshots  
- 📎 Uploaded images  

The system flags suspicious content, assigns a **risk score**, and provides **human-readable explanations** so users can make informed decisions.

---

## ✨ Key Features

### 🔍 Multi-Input Analysis
- Paste text messages or emails
- Upload `.eml` files or raw email content
- Paste screenshots directly from clipboard
- Upload images (phishing, invoices, fake login pages)

---

### ⚠️ Scam Detection Engine
Each input is analyzed and returns:

- **Risk Level**: `Safe`, `Review`, `High Risk`
- **Confidence Score**
- **Scam Category** (phishing, invoice fraud, etc.)
- **Detailed Reasons**
- **Recommended Action**

---

### 🧠 Explainable AI (Core Feature)

Unlike traditional spam filters, this app explains *why* something is suspicious:

“This message creates urgency, contains a suspicious link, and impersonates a bank using a non-official domain.”

---

### 🎯 Highlight Suspicious Content
- Detects and highlights phrases like:
  - “act now”
  - “verify your account”
  - “click here”
  - “send code”

---

### 📂 Unified Dashboard
Organized view with filters:

- All
- Safe
- Suspicious
- High Risk
- Needs Review

Filter by:
- Type (SMS / Email / Image)
- Reason (Urgency / Money request / Impersonation)

---

### 🏷️ Feedback System
Users can label results:
- `Scam`
- `Safe`
- `Unsure`

This feedback improves future detection.

---

## 🧪 Detection Approach

The system uses a **hybrid model**:

### ⚙️ Rule-Based Detection
Fast heuristics:
- Suspicious links or shortened URLs
- Sender domain mismatch
- Requests for OTP/password
- Gift card / crypto / wire transfer requests
- Urgency or pressure tactics

---

### 🤖 AI Classification
- Scam probability scoring
- Category classification
- Natural language explanation generation

---

### 🖼️ OCR for Images
- Extracts text from screenshots/images
- Applies same detection logic
- Detects:
  - Fake login pages
  - QR code scams
  - Brand impersonation
  - Typos in company names

---

## 🧩 Supported Scam Types

- Phishing
- Fake bank alerts
- Delivery scams
- Fake invoices
- Job scams
- Crypto scams
- Gift card scams
- Tech support scams
- Romance scams
- Government/tax scams
- Account verification scams
- Lottery/prize scams

---

## 🖥️ Tech Stack

### Frontend
- React (web dashboard PWA App)
- React Native / Expo (mobile)

### Backend
- FastAPI (Python)

### Services
- OCR: Tesseract or cloud OCR
- AI: LLM (OpenAI or local model)
- Email parsing: Gmail / Outlook APIs (future)

### Infrastructure
- PostgreSQL
- Celery / Background jobs
- S3-compatible storage (for images)

---

## 📡 API Endpoints

POST /analyze/text  
POST /analyze/email  
POST /analyze/image  
POST /analyze/screenshot  

GET  /messages  
POST /feedback  
POST /connect/gmail  

---

## 🗄️ Database Schema

### users
- id
- email
- created_at

### submissions
- id
- user_id
- type (`sms`, `email`, `image`, `screenshot`)
- raw_text
- file_url
- created_at

### analyses
- id
- submission_id
- score
- risk_level
- category
- reasons_json
- recommendation
- model_version
- created_at

### feedback
- id
- analysis_id
- label (`safe`, `scam`, `unsure`)
- created_at

---

## 🔄 Processing Pipeline

1. Receive input (text or image)
2. If image → extract text via OCR
3. Normalize content
4. Extract:
   - URLs
   - Emails
   - Phone numbers
   - Keywords (urgency, money, identity)
5. Run rule-based checks
6. Run AI classifier
7. Combine results:
   - Score
   - Category
   - Explanation
8. Store result
9. Display to user

---

## 🚧 MVP Scope

### ✅ Included
- Text input analysis
- Image upload + OCR
- Scam detection + explanation
- Filtering dashboard
- User feedback system

### ❌ Not Included (yet)
- Real-time SMS sync
- Automatic email deletion
- Browser phishing detection
- Advanced ML training pipelines
- Deep visual fraud detection

---

## 📈 Roadmap

### Phase 1
- Core analysis engine
- Text + image support
- Basic UI

### Phase 2
- Dashboard + filters
- History + saved results
- Feedback learning

### Phase 3
- Gmail / Outlook integration
- Bulk scanning
- Auto inbox filtering

---

## 💡 Vision

Build a system that not only detects scams — but **teaches users how to recognize them**.

---

## 💰 Monetization (Future)

- Free tier: limited scans/day
- Premium: inbox integration, history, bulk scanning
- Business: team & family protection

---

## 🧠 MVP Pitch

An app that lets users paste messages, screenshots, emails, or images, then detects likely scams, flags them, and clearly explains why they are suspicious.