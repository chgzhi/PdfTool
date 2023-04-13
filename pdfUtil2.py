# pdfUtil2.py

'''
Desc: 从pdf中提取信息等功能。
Author: Chen Guangzhi
Date: 2023-03-10
Version: 0.1

本程序依赖：
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyPDF2
'''

from PyPDF2 import PdfReader, PdfWriter, PdfMerger

# 按指定的页码范围提取pdf文档，提取出的pdf文
# 档名在原pdf文档名后加"merged"
# params:
#    1. inFilename: 输入的pdf文档名，包括完整路径
#    2. pages: 要提取的页码范围，格式为：“1-2”
def extractPdf(inFilename, pages):
    pdfReader = PdfReader(inFilename)
    pdfWriter = PdfWriter()
    
    # 确定页码范围
    startN = int(pages[0]) - 1
    endN = int(pages[2])
    
    for i in range(startN, endN):
        pdfWriter.add_page(pdfReader.pages[i])
    
    outFilename = inFilename[:-4] + "_extracted" + ".pdf"
    
    with open(outFilename, 'wb') as f:
        pdfWriter.write(f)
    return outFilename

# 将多个pdf文件合并
# params:
#    1. pdfFileList: pdf文件列表
def mergePdf(pdfFileList):
    pdfMerger = PdfMerger()
    
    for pd in pdfFileList:
        pdfMerger.append(pd,import_outline=False)
        
    outFilename = pdfFileList[0][:-4] + "merged" + ".pdf"
    pdfMerger.write(outFilename)
    return outFilename

if __name__ == '__main__':
    # test pass
    #extractPdf("C:/rbstudy/studypyqt6/pyqt6source/basic/pdfa.pdf","1-2")
    mergePdf(["C:/rbstudy/studypyqt6/pyqt6source/basic/pdfa_merged1.pdf", "C:/rbstudy/studypyqt6/pyqt6source/basic/pdfa_merged2.pdf"])