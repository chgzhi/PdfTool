# pdfUtil.py

'''
Desc: pdf auxily function
Author: Chen Guangzhi
Date: 2023-03-10
Version: 0.1

本程序依赖：
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple fitz
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyMuPDF
'''

import os 
import fitz 


#
# inFilename: 绝对路径，包含所有
# outFilename: 仅包含名称，不包含扩展名
def jpg2pdf(inFilename, outFilename):
    baseDir = os.path.dirname(inFilename)
    
    imgJpg = fitz.open(inFilename)
    
    pdfBytes = imgJpg.convert_to_pdf()
    imgPdf = fitz.open("pdf",pdfBytes)
    
    saveFilename = baseDir + "/"+ outFilename + ".pdf"
    imgPdf.save(saveFilename)
    
    return saveFilename
    
    
if __name__ == '__main__':
    # test pass
    jpg2pdf("C:/rbstudy/studypyqt6/pdfTool/otje.jpg","test")
