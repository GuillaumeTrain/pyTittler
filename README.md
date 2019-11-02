# pyTittler
PyTittler is intended to be a pdf file renamer based on user template definition

I'm not a programmer so dont blame me for the messy code, feel free to improve it if you want.

Storyline:

1) My girlfriend was frustrated do not be able to switch on my PC. (she just missed up switch on the screen)
2) She unintentionally destroyed it , making it fall from a few meters high.
3) The hard disk was damaged and with it , my pdf collection (around 50 Go). i managed to recover them using the hard disk 
serial port. The final files were unamed, and, needed to be checked one by one.
4) i decided to make an automatic process to perform this task.

Process overview (from program point of view):

1) get file to be rename path
2) get templates from some files manual analysis
3) apply each template on each file
4) summarise positive results with renaming proposal
5) copy validated proposal on the new file/folder naming proposal

Templates are composed of the following items :
- category : just a text corresponding to a top folder in the final naming sequence
- subcategory/template : just a text corresponding to a sub folder placed into category folder in the final naming sequence
- OCRtrigger : a text (redefinable in the edit line of GUI) associated with a trigger zone (Qrect)
- a tittle zone : the tittle zone is the pdf zone to be read when the trigger is positive

GUI Overview:

<a href="https://ibb.co/4Vy08sB"><img src="https://i.ibb.co/S3TZtQq/Annotation-2019-11-02-140619.png" alt="Annotation-2019-11-02-140619" border="0"></a><br /><br />


This program is based on the following technologies :

- python: python 3.7.5 (i dont know why but this program cannot run into 3.8 for now)
- Pyside2 : pyQT5 derivate for python GUI dev
- Pillow : image handleling modules/libs
- Wand : pdf to image processing core
- Tesseract : trained IA to image to text recognizing core

so you'll need the following ressouces: (all are 32bit versions for me)
pip ressources :
- pytesseract
- tesseractOCR
- pillow
- pyside2
- wand
third party software (may be installed to get the corresponding python wrapper to work well):
- ghost script
- imagemagik
- tesseract

A big refactoring based on object review and multiprocessing is needed.
I will do it later.
