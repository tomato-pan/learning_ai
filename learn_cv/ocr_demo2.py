from cnocr import CnOcr 
ocr = CnOcr() 
res = ocr.ocr('/Users/panjwangsu.com/Desktop/panj_python/learning_ai/635.png')
for i in res:
    print(i)
print("Predicted Chars:", res)