Llama 3.1 8b modeli ile geliştirilmiş RAG sistem modelidir. Bu branch üzerinde sadece RAG sistemi içerisine sağlanan dosya ile soru-cevap yapılabilecek dokümanlar bulunmaktadır. Kodlar modelin localde çalışacak şekilde ayarlanmıştır. OpenAI API Key ile kullanımı mümkündür

------------

master ---> Dosya ile soru-cevap 

memory ---> Hafıza sistemi ile modelle RAG sisteminden ayrı olarak sohbet botu olarak kullanılırken hafızalı bir model

fastapi ---> Memory branchi üzerindeki sistemin RestAPI ile local sunucu üzerinde çalışması

------------

.env Dosyası içeriği

OPENAI_API_KEY= YOUR-API-KEY-PASTE-HERE


