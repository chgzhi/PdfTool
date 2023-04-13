# pdftool.py

'''
Desc: pdf tools
Author: Chen Guangzhi
Date: 2023-03-10
Version: 0.1
'''
import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QStackedLayout,
    QWidget,
    QLineEdit,
    QLabel,
    QMessageBox,
)

from pdfUtil import jpg2pdf
from pdfUtil2 import extractPdf, mergePdf

FILE_FILTERS = [
    "Jpg files (*.jpg)",
    "Pdf files (*.pdf)",
    "All files (*)",
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pdf Tool")
        self.setFixedSize(QSize(450, 200))
        
        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()
        
        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)
        
        btn = QPushButton("jpg2pdf")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        

        
        # layout1 
        layout = QVBoxLayout()
        button1_layout = QHBoxLayout()

        button1 = QPushButton("...")
        button1.clicked.connect(self.get_filename)
        
        lbl = QLabel("请选择jpg文件")
        
        layout.addWidget(lbl)
        layout.addLayout(button1_layout)
        
        self.lineEdit1 = QLineEdit()
        
        button1_layout.addWidget(self.lineEdit1)
        button1_layout.addWidget(button1)
        
        
        
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setMaxLength(20)
        self.lineEdit2.setPlaceholderText("Enter your output filename (not contain sufix)")
        self.lineEdit2.returnPressed.connect(self.return_pressed)
        layout.addWidget(self.lineEdit2)
        
        convert2pdfBtn = QPushButton("Convert jpg to Pdf")
        convert2pdfBtn.clicked.connect(self.convert2pdf)
        layout.addWidget(convert2pdfBtn)
        
        containerJpg2pdf = QWidget()
        containerJpg2pdf.setLayout(layout)
        self.stacklayout.addWidget(containerJpg2pdf)
        
        
        ## new  
        btnExtractPdf = QPushButton("Extract Pdf")
        btnExtractPdf.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btnExtractPdf)
        
        # layout2
        layout2 = QVBoxLayout()
        layout2lbl = QLabel("请选择pdf文件")
        layout2.addWidget(layout2lbl)
        
        layout2button1_layout = QHBoxLayout()
        layout2button1 = QPushButton("...")
        layout2button1.clicked.connect(self.layout2get_filename)
        
        layout2.addLayout(layout2button1_layout)
        
        self.layout2lineEdit1 = QLineEdit()
        
        layout2button1_layout.addWidget(self.layout2lineEdit1)
        layout2button1_layout.addWidget(layout2button1)
        
        self.layout2lineEdit2 = QLineEdit()
        self.layout2lineEdit2.setMaxLength(20)
        self.layout2lineEdit2.setPlaceholderText("Enter your pages (eg. 1-2)")
        layout2.addWidget(self.layout2lineEdit2)
        
        extractpdfBtn = QPushButton("Extract pdf")
        extractpdfBtn.clicked.connect(self.extractPdf)
        layout2.addWidget(extractpdfBtn)
        
        containerExtractpdf = QWidget()
        containerExtractpdf.setLayout(layout2)
        self.stacklayout.addWidget(containerExtractpdf)
        
        ## new  
        btnMergePdf = QPushButton("Merge Pdf")
        btnMergePdf.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btnMergePdf)
        
        # layout3
        layout3 = QVBoxLayout()
        layout3lbl = QLabel("请选择多个pdf文件：")
        layout3.addWidget(layout3lbl)
        
        layout3button1_layout = QHBoxLayout()
        layout3button1 = QPushButton("...")
        layout3button1.clicked.connect(self.layout3get_filename)
        
        layout3.addLayout(layout3button1_layout)
        
        self.layout3lineEdit1 = QLineEdit()
        
        layout3button1_layout.addWidget(self.layout3lineEdit1)
        layout3button1_layout.addWidget(layout3button1)
        
        
        mergepdfBtn = QPushButton("Merge pdf")
        mergepdfBtn.clicked.connect(self.mergePdf)
        layout3.addWidget(mergepdfBtn)
        
        containerMergepdf = QWidget()
        containerMergepdf.setLayout(layout3)
        self.stacklayout.addWidget(containerMergepdf)
        
        container = QWidget()
        container.setLayout(pagelayout)
        self.setCentralWidget(container)
        
    def return_pressed(self):
        print(self.lineEdit2.text())
        #self.centralWidget().setText("BOOM!")
    def get_filename(self):
        caption = ""  # Empty uses default caption.
        initial_dir = ""  # Empty uses current folder.
        initial_filter = FILE_FILTERS[0]  # Select one from the list.
        filters = ";;".join(FILE_FILTERS)
        
        filename, selected_filter = QFileDialog.getOpenFileName(
            self,
            caption=caption,
            directory=initial_dir,
            filter=filters,
            initialFilter=initial_filter,
        )
        #print("Result:", filename, selected_filter)
        self.lineEdit1.setText(filename)
    def layout2get_filename(self):
        caption = ""  # Empty uses default caption.
        initial_dir = ""  # Empty uses current folder.
        initial_filter = FILE_FILTERS[1]  # Select one from the list.
        filters = ";;".join(FILE_FILTERS)
        
        filename, selected_filter = QFileDialog.getOpenFileName(
            self,
            caption=caption,
            directory=initial_dir,
            filter=filters,
            initialFilter=initial_filter,
        )
        #print("Result:", filename, selected_filter)
        self.layout2lineEdit1.setText(filename)
    def layout3get_filename(self):
        caption = ""  # Empty uses default caption.
        initial_dir = ""  # Empty uses current folder.
        initial_filter = FILE_FILTERS[1]  # Select one from the list.
        filters = ";;".join(FILE_FILTERS)
        
        filenames, selected_filter = QFileDialog.getOpenFileNames(
            self,
            caption=caption,
            directory=initial_dir,
            filter=filters,
            initialFilter=initial_filter,
        )
        
        self.layout3lineEdit1.setText(",".join(filenames))
    def convert2pdf(self):
        #print(type(self.lineEdit2.text()))
        #print(self.lineEdit1.text())
        inFilename = self.lineEdit1.text()
        outFilename = self.lineEdit2.text()
        
        if inFilename == "" or outFilename == "":
            button = QMessageBox.information(self, "文件名为空", "输入或输出文件名为空！")
        else:
            SaveFilename = jpg2pdf(inFilename, outFilename)
            QMessageBox.information(self, "转换成功", "转换后的文件保存在：" + SaveFilename)
    def extractPdf(self):
        inFilename = self.layout2lineEdit1.text()
        pages = self.layout2lineEdit2.text()
        if inFilename == "" or pages == "":
            button = QMessageBox.information(self, "文件名为空", "输入文件名或页码范围为空！")
        else:
            SaveFilename = extractPdf(inFilename, pages)
            QMessageBox.information(self, "提取成功", "提取后的文件保存在：" + SaveFilename)
    def mergePdf(self):
        inFilename = self.layout3lineEdit1.text()
        
        if inFilename == "":
            button = QMessageBox.information(self, "文件名为空", "没选择多个要合并的pdf文件！")
        else:
            inFilenameList = inFilename.split(",")
            SaveFilename = mergePdf(inFilenameList)
            QMessageBox.information(self, "合并成功", "合并后的文件保存在：" + SaveFilename)
        
    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)
    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)
    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)
#app = QApplication(sys.argv)
app = QApplication([])
window = MainWindow()
window.show()

app.exec()