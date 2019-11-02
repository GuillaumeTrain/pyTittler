"""
Module PyTittler :                                                                  Createur :  G.TRAIN
                                                                                    Contact :   g.train@live.fr

Description:
Ce Module met à disposition des outils permettant:
 - la manipulation de fichiers : myPath
 - la convertion de fichier en image : myFileimager
 - la reconnaissance de texte dans des images : myTesseract



"""
import collections

from tkinter import Tk,Frame,Text,filedialog,messagebox,END

from pathlib import Path

def debugfunction(object,Exception):
    """Fonction générale permettant le debug des classes :
    """
    print("debug mode ON : {}".format(object))
    for key,value in object.__dict__.items():
        print("attribute : {} ==> value : {}".format(key,value))

    if Exception != None :
        print("\nThe following exceptions was raised :")
        print(Exception.__doc__)
        if hasattr(Exception, 'message'):
            print(Exception.message)

class myPath :
    def __init__(self, p, dm = False):
        self.classname = "path"
        self.functionname = "__init__"
        self.debugmode = dm
        self.debugprompt = None
        self.isfolder = None
        self.basepath = None
        self.exception = Exception()
        self.exception.__doc__ = "None"
        self.exception.message = ""
        try :
            if Path(p).exists() :
                self.basepath = Path(p)
            else :
                self.debugmode = True
                self.debugprompt = "The path does not exists or is not accessible"
        except Exception as e:
            self.debugmode = True
            self.exception = e
            self.debugprompt = "Could not create Path object into basepath"
        if self.debugmode is True :
            debugfunction(self,self.exception)
    def setpath(self,p):
        self.classname = "path"
        self.functionname = "setpath"
        try :
            self.basepath = Path(p)
        except Exception as e:
            self.exception = e
            self.debugmode = True
            self.debugprompt = "Could not set path"
        if self.debugmode is True :
            debugfunction(self,self.exception)
    def removepath(self):
        self.classname = "path"
        self.functionname = "removepath"
        try :
            self.basepath = Path()
        except Exception as e:
            self.exception = e
            self.debugmode = True
            self.debugprompt = "could not remove path from {}".format(self)
        if self.debugmode is True :
            debugfunction(self,self.exception)
    def getabsolutepath(self):

        try:
            abspath=self.basepath.resolve()
        except Exception as e:
            self.exception = e
            self.debugmode = True
            abspath = None
        if self.debugmode is True:
            debugfunction(self,self.exception)
        return abspath
    def exists(self):
        try :
            test = self.basepath.exists()
        except Exception as e:
            self.exception = e
            self.debugmode = True
            test = False

        if( self.exception == OSError ):
            self.debugprompt = "incorrect path syntax :{}".format(self.basepath)
        if (self.exception == AttributeError):
            self.debugprompt = "incorrect path, it has been replaced by None object to prevent hacking :{}".format(self.basepath)
        if self.debugmode is True :
            debugfunction(self,self.exception)

        return test




