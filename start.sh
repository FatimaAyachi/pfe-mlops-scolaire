#!/bin/bash

# 1. تشغيل FastAPI في الخلفية على المنفذ 8080
uvicorn api.main:app --host 127.0.0.1 --port 8080 &

# 2. الانتظار لثانيتين للتأكد من أن الـ API قد اشتغل
sleep 2

# 3. تشغيل واجهة Streamlit وتوجيهها للمنفذ الذي يفرضه موقع Render ديناميكياً
streamlit run app/app.py --server.port $PORT --server.address 0.0.0.0
