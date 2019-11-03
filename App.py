
from PySide2 import QtWidgets, QtGui, QtCore
import os
from PyTittler_module import *
from PIL import Image
from wand.image import Image as wi
from pytesseract import pytesseract
import shutil
import pathlib

import main

class myGraphicsView(QtWidgets.QGraphicsView):
    rectChanged = QtCore.Signal(QtCore.QRect)
    mouseReleasedEvent = QtCore.Signal(QtCore.QEvent)
    def __init__(self,parent=None):
        super(myGraphicsView,self).__init__(parent)
        self.rubberBand = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle, self)
        self.setMouseTracking(True)
        self.origin = QtCore.QPoint()
        self.changeRubberBand = False
        self.strOCR=""
        self.selectionrect = QtCore.QRect

    def mousePressEvent(self, event):
        #print("mousePressEvent")
        self.origin = event.pos()
        self.rubberBand.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
        self.rectChanged.emit(self.rubberBand.geometry())
        self.rubberBand.show()
        self.changeRubberBand = True
        QtWidgets.QGraphicsView.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        #print("mouseMoveEvent")
        if self.changeRubberBand:
            self.rubberBand.setGeometry(QtCore.QRect(self.origin, event.pos()).normalized())
            self.rectChanged.emit(self.rubberBand.geometry())
        QtWidgets.QGraphicsView.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        #print("mouseReleaseEvent")
        self.changeRubberBand = False

        self.selectedpix=self.pix.copy(self.selectionrect)
        self.selectionfile=QtCore.QFile("selectionfile.png")
        self.selectedpix.save( self.selectionfile, "PNG");
        QtWidgets.QGraphicsView.mouseReleaseEvent(self, event)

        strrectpos="Position du rectangle de selection : topleft :{} topright : {}".format(self.selectionrect.topLeft(),self.selectionrect.bottomRight())
        self.strOCR="{}".format(pytesseract.image_to_string(Image.open("selectionfile.png")))
        print("{}\n resultat OCR : \n{}".format(strrectpos,self.strOCR))
        self.mouseReleasedEvent.emit(event)

    def onRectChanged(self, r):
        self.rubberBand.geometry()
        self.selectionrect=r
        topLeft = r.topLeft()
        bottomRight = r.bottomRight()

       # print(topLeft.x(), topLeft.y(), bottomRight.x(), bottomRight.y())

    def showimage(self,pixmap):
        scene = QtWidgets.QGraphicsScene()
        self.pix=pixmap.scaledToWidth(600, QtCore.Qt.SmoothTransformation)
        scene.addPixmap(self.pix)
        self.setScene(scene)
    def getimage(self):
        return self.pix

class MyApp(main.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.setupUi(self)
        self.initfb()
        self.initfl()
        self.initssi()
        self.initttv()
        self.initscanner()
        self.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.getpathfromcursor)
        self.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), self.getandshowimage)
        self.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"),self.addcategory)
        self.connect(self.pushButton_6, QtCore.SIGNAL("clicked()"), self.add)
        self.connect(self.pushButton_5, QtCore.SIGNAL("clicked()"), self.removechild)
        self.graphicsView.mouseReleasedEvent.connect(self.showOCRres)
        self.graphicsView.rectChanged.connect(self.graphicsView.onRectChanged)
        self.connect(self.pushButton_7,QtCore.SIGNAL("clicked()"),self.scan)
        self.connect(self.pushButton_8, QtCore.SIGNAL("clicked()"), self.rename)
        self.UnAutorizedchartable=["< ",">",":",'"',"/","\\","|","?","*","©",",",";","'","‘","»"]
        self.spacechartable=["\n","   ","  "]
        self.filenamemaxchar=30
        print("init ok")

    def initscanner(self):
        self.treeWidget_3.setHeaderLabels(['File name', 'Category', 'Template', 'Tittle','Path',"Type"])
        self.treeWidget_3.invisibleRootItem().takeChildren()
        folderlist_root = self.treeWidget.invisibleRootItem()
        folderlist_root_childcount = folderlist_root.childCount()
        if folderlist_root_childcount > 0:
            for i in range(folderlist_root_childcount):
                folderlist = folderlist_root.child(i)
                folderlist_childcount = folderlist.childCount()
                for j in range(folderlist_childcount):
                    folder = folderlist.child(j)
                    print("ajout de {} au scanner".format(folder.text(0)))
                    fname=folder.text(0)
                    ftype =folder.text(1)
                    fpath = folder.text(2)
                    self.treeWidget_3.addTopLevelItem(QtWidgets.QTreeWidgetItem([fname,None,None,None,fpath,ftype]))
                    print("ok")

    def rename(self):
        filelist_root = self.treeWidget_3.invisibleRootItem()
        filelist_childcount = filelist_root.childCount()
        for i in range(filelist_childcount):
            file = filelist_root.child(i)
            print("analyse du fichier {} :".format(file.text(0)))
            if file.text(1) is "":
                pass
            else :
                source_file=pathlib.Path(file.text(4))
                target_file = os.path.join("C:", "\savedfiles", "{}".format(file.text(1)), "{}".format(file.text(2)),"{}{}".format(file.text(3),file.text(5)))
                indice=0
                while os.path.exists(target_file) :
                    target_file = os.path.join("C:", "\savedfiles", "{}".format(file.text(1)),"{}".format(file.text(2)), "{}{}".format(file.text(3)+"-copie{}".format(indice), file.text(5)))
                    indice=indice+1
                targetdir = os.path.join("C:", "\savedfiles", "{}".format(file.text(1)), "{}".format(file.text(2)))
                os.makedirs(targetdir,exist_ok=True)
                print("source file : "+ str(source_file))
                print("target file : "+ str(target_file))
                print("target folder : " + str(target_file))
                shutil.copy(str(source_file), str(target_file))

    def scan(self):
        self.initscanner()
        filelist_root = self.treeWidget_3.invisibleRootItem()
        filelist_childcount = filelist_root.childCount()

        template_category_root = self.treeWidget_2.invisibleRootItem()
        category_count=template_category_root.childCount()

        print(" template_category_count : {} ".format( category_count))

        if category_count>0 and filelist_childcount>0:

            i=0
            for i in range(filelist_childcount):
                file = filelist_root.child(i)
                print("analyse du fichier {} :".format(file.text(0)))
                if file.text(1) is "" :
                    j=0
                    for j in range(category_count):
                        category=template_category_root.child(j)
                        subcategory_count=category.childCount()
                        k=0
                        for k in range(subcategory_count):
                            print("={}".format(k))
                            subcategory=category.child(k)
                            template_count=subcategory.childCount()
                            l=0
                            for l in range(template_count):
                                templatedefinition = subcategory.child(l)
                                triggertargets=[]
                                tittletargetdefinition=subcategory.child(0).child(0)
                                tittletarget=[tittletargetdefinition.data(3,0),
                                              tittletargetdefinition.data(4,0),
                                              tittletargetdefinition.data(5,0),
                                              tittletargetdefinition.data(6,0)]

                                triggertargets.append([templatedefinition.data(2,0),
                                                            templatedefinition.data(3,0),
                                                            templatedefinition.data(4,0),
                                                            templatedefinition.data(5,0),
                                                            templatedefinition.data(6,0)])
                                for target in triggertargets :
                                    OCRtarget = target[0]
                                    file_abspath = file.data(4,0)
                                    detection_zone = QtCore.QRect(QtCore.QPoint(int(target[1]),int(target[2])),
                                                                  QtCore.QPoint(int(target[3]),int(target[4])))
                                    print("OCRtarget :{}\nfile_abspath : {} \ndetection_zone {}".format(OCRtarget,file_abspath,detection_zone))
                                    try:
                                        with wi(filename=file_abspath + "[0]",
                                                resolution=300) as page_image:
                                            page_image.save(filename='tempsc.jpg')
                                            pixmap = QtGui.QPixmap('tempsc.jpg')
                                            self.scanner_pix=pixmap.scaledToWidth(600, QtCore.Qt.SmoothTransformation)
                                            self.scanner_selectedpix = self.scanner_pix.copy(detection_zone)
                                            self.scanner_selectionfile = QtCore.QFile("scannerrect.png")
                                            self.scanner_selectedpix.save(self.scanner_selectionfile, "PNG");
                                            strOCR = "{}".format(pytesseract.image_to_string(Image.open("scannerrect.png")))
                                            #print("strOCR : {} vs OCRtarget : {}".format(strOCR,OCRtarget))
                                            if OCRtarget in strOCR :
                                                print("OCRtarget : {} found in {}".format(OCRtarget,file_abspath))
                                                file.setText(1,category.text(0))
                                                file.setText(2,subcategory.text(1))

                                                tittle_zone = QtCore.QRect(QtCore.QPoint(int(tittletarget[0]), int(tittletarget[1])),
                                                                              QtCore.QPoint(int(tittletarget[2]), int(tittletarget[3])))
                                                self.scanner_tittleselectionfile = QtCore.QFile("scannerrecttittle.png")
                                                self.scanner_tittleselectedpix = self.scanner_pix.copy(tittle_zone)
                                                self.scanner_tittleselectedpix.save(self.scanner_tittleselectionfile, "PNG");
                                                strtittle = "{}".format(pytesseract.image_to_string(Image.open("scannerrecttittle.png")))
                                                charnum=0
                                                strfilename=""

                                                for char in strtittle:
                                                    if charnum < self.filenamemaxchar:
                                                        #print("char : "+char)
                                                        unwanted=False
                                                        returnline=False
                                                        for unautorizedchar in self.UnAutorizedchartable :
                                                            #print("strtittle : " + unautorizedchar)
                                                            if char is unautorizedchar :
                                                                unwanted = True
                                                        for spacechar in self.spacechartable :
                                                            if char is spacechar:
                                                                returnline=True
                                                        if unwanted is True:
                                                            pass
                                                        elif returnline is True :
                                                            #print("strfilename : " + " ")
                                                            strfilename=strfilename+" "
                                                        else :
                                                           # print("strfilename : " + strfilename)
                                                            strfilename=strfilename+strtittle[charnum]
                                                    else :
                                                        pass
                                                    charnum=charnum+1
                                                    file.setText(3,strfilename )
                                    except:
                                        print("wand file error : ".format(file_abspath))
                                        pass

    def getselectedindex(self):
        index = self.treeWidget_2.currentIndex()

        return index

    def getselecteditem(self):
        Item = self.treeWidget_2.currentItem()

        return Item

    def add(self):
        item = self.getselecteditem()
        print("add value : {}".format(item.data(0,0)))
        print("add context test :")

        if (item.parent() is None ):
            print("item.parent() : {}".format(item.parent()))
            print('add template requested')
            self.addtemplate()

        elif (item.parent().parent() is None):
            print("item.parent().parent(): {}".format(item.parent().parent()))
            print('add OCRtarget requested')
            self.addOCRtarget()

        elif (item.parent().parent().parent() is None):
            print("item.parent().parent().parent() : {}".format(item.parent().parent().parent()))
            print('add tittletarget requested')
            self.addtittletarget()

        else:
            print ("no context found")
            pass

    def addcategory(self):
        print("add category : {}".format(self.lineEdit.text()))
        self.treeWidget_2.addTopLevelItem(QtWidgets.QTreeWidgetItem([self.lineEdit.text()]))

    def getcategory(self):
        item=QtCore.QAbstractItemModel()
        print("addcat : {}".format(self.treeWidget_2.selectedItems()[0].data()))
        if (not item.parent()):
            item = self.treeWidget_2.selectedItems()[0]
        return item

    def addtemplate(self):
        print("adding template")
        item = self.getselectedindex()
        injectionitem = QtWidgets.QTreeWidgetItem([item.data(),self.lineEdit.text(),"",""])
        self.treeWidget_2.selectedItems()[0].addChild(injectionitem)

    def addOCRtarget(self):
        item = self.getselecteditem()
        topleft = self.graphicsView.selectionrect.topLeft()
        bottomright = self.graphicsView.selectionrect.bottomRight()
        print(topleft)
        print(bottomright)
        injectionitem = QtWidgets.QTreeWidgetItem([item.data(0,0),
                                                   item.data(1,0),
                                                   self.lineEdit.text(),
                                                   str(topleft.x()),
                                                   str(topleft.y()),
                                                   str(bottomright.x()),
                                                   str(bottomright.y())])
        self.treeWidget_2.selectedItems()[0].addChild(injectionitem)

    def addtittletarget(self):
        print("adding template")
        item = self.getselecteditem()
        topleft = self.graphicsView.selectionrect.topLeft()
        bottomright = self.graphicsView.selectionrect.bottomRight()
        print(topleft)
        print(bottomright)
        injectionitem = QtWidgets.QTreeWidgetItem(
            [item.data(0, 0),
             item.data(1, 0),
             item.data(2, 0),
             str(topleft.x()),
             str(topleft.y()),
             str(bottomright.x()),
             str(bottomright.y()),
             self.lineEdit.text()])
        self.treeWidget_2.selectedItems()[0].addChild(injectionitem)

    def gettemplate(self):
        item = self.getselecteditem()
        res = None
        if (not item.parent.parent()):
            res = self.treeWidget_2.selectedItems()
        return res

    def getOCRtarget(self):
        item = self.getselectedindex()
        res = None
        if (not item.parent.parent.parent()):
            res = self.treeWidget_2.selectedItems()
        return res

    def removechild(self):
        item = self.treeWidget_2.currentItem()
        item.takeChildren()
        item.__str__()

    def showOCRres(self):
        print("showOCR : {}".format(self.graphicsView.strOCR))
        self.lineEdit.setText(self.graphicsView.strOCR)

    def initfb(self):
        path = "Ce PC"
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(path))
        self.treeView.setSortingEnabled(True)

    def initfl(self):
        self.treeWidget.setHeaderLabels(['File','type','absolute path'])
        #self.treeWidget.

    def initttv(self):
        self.treeWidget_2.setHeaderLabels(['Category', 'Subcategory','OCRtarget',"topleft.x","topleft.y","bottomright.x","bottomright.y","title example"])

    def initssi(self):
        picturearea=myGraphicsView(self.frame_4)
        #self.graphicsView.destroy()
        self.graphicsView = picturearea
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setFixedSize(QtCore.QSize(607, 858))
        self.verticalLayout_8.addWidget(self.graphicsView)

    def additemtofl(self,path):
        self.treeWidget.addTopLevelItem(path)

    def getandshowimage(self):
        print("{}".format(self.treeWidget.selectedIndexes()[0].data()))
        print("{}".format(self.treeWidget.selectedIndexes()[2].data()))
        with wi(filename=self.treeWidget.selectedIndexes()[2].data()+"[0]", resolution=300) as page_image:
           # with wi(pic) as page_image:
                page_image.save(filename='temp.jpg')
                # qimage=QtGui.QImage()
                # data=page_image.make_blob(format=fmt)
                # qimage.loadFromData(data)
                pixmap=QtGui.QPixmap('temp.jpg')

                self.graphicsView.showimage(pixmap)

    def getpathfromcursor(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        item=QtWidgets.QTreeWidgetItem([file_path])
        if myPath(file_path).exists():

            p=myPath(file_path)
            if p.basepath.is_dir() :
                for child in p.basepath.iterdir():
                    if child.is_file() and "pdf" in child.suffix :
                        item.addChild(QtWidgets.QTreeWidgetItem([child.name,child.suffix,str(child.resolve())]))
                        print (child)
            elif p.basepath.is_file() and "pdf" in p.basepath.suffix :
                    item.addChild(QtWidgets.QTreeWidgetItem([p.basepath.name,p.basepath.suffix,str(p.basepath.resolve())]))
                    print (p.basepath)

        self.treeWidget.addTopLevelItem(item)

if __name__=='__main__':
    pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
    app=QtWidgets.QApplication()
    a = MyApp()
    a.show()
    app.exec_()