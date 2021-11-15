"""
Nombre: Alejandro Tejada
Curso: Diseño Compiladores
Fecha: septiembr 2021
Programa: GUI.py
Propósito: Segunda version de la interfaz
V 2.0
"""

# importing required libraries
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
import sys

from mainSemantic import Compilar
from mainIntermedio import CompilarIntermedio
import pickle


# Creating main window class
class MainWindow(QMainWindow):

    # constructor
    def __init__(self, *args, **kwargs):
        self.content_editor = ''
        super(MainWindow, self).__init__(*args, **kwargs)
        # self.setGeometry(1200, 800)

        # setting window geometry
        self.setGeometry(100, 100, 1200, 800)
        # self.setAcceptDrops(True)
        # setting font to the editor
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(10)

        # creating a layout
        mainlayout = QVBoxLayout()

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.windowEditor = QWidget()
        self.windowResults = QWidget()
        self.windowResultsIntermedio = QWidget()

        # # AddEntryToTable tabs
        self.tabs.addTab(self.windowEditor, "Editor de código")
        self.tabs.addTab(self.windowResults, "Análisis semántico")
        self.tabs.addTab(self.windowResultsIntermedio, "Código intermedio")

        self.errorForlog2 = QPlainTextEdit()
        self.errorForlog2.setFont(fixedfont)
        
        self.windowResultsIntermedio.layout = QVBoxLayout()
        self.windowResultsIntermedio.layout.addWidget(self.errorForlog2)
        self.windowResultsIntermedio.setLayout(
            self.windowResultsIntermedio.layout)
        # creating a QPlainTextEdit object
        self.editor = QPlainTextEdit()

        self.errorForLog = QLabel()
        self.errorForLog.setFont(fixedfont)
        self.errorForLog.setText("")
        self.windowResults.layout = QVBoxLayout()
        self.windowResults.layout.addWidget(self.errorForLog)
        self.windowResults.setLayout(self.windowResults.layout)

        self.editor.setFont(fixedfont)

        # self.path holds the path of the currently Abrir archivo.
        # If none, we haven't got a file open yet (or creating new).
        self.path = None

        # adding editor to the layout
        mainlayout.addWidget(self.tabs)
        # layout.addWidget(self.editor)
        self.windowEditor.layout = QVBoxLayout()
        self.windowEditor.layout.addWidget(self.editor)
        self.windowEditor.setLayout(self.windowEditor.layout)

        # creating a QWidget layout
        container = QWidget()

        # setting layout to the container
        container.setLayout(mainlayout)

        # making container as central widget
        self.setCentralWidget(container)

        # creating a status bar object
        self.status = QStatusBar()

        # setting stats bar to the window
        self.setStatusBar(self.status)

        # creating a file tool bar
        file_toolbar = QToolBar("File")

        # adding file tool bar to the window
        self.addToolBar(file_toolbar)

        # creating actions to add in the file menu
        # creating a Abrir archivo action
        open_file_action = QAction("Abrir archivo", self)

        # setting status tip
        open_file_action.setStatusTip("Abrir archivo")

        # adding action to the Abrir archivo
        open_file_action.triggered.connect(self.file_open)

        # adding this to tool bar
        file_toolbar.addAction(open_file_action)

        # similarly creating a save action
        save_file_action = QAction("Guardar", self)
        save_file_action.setStatusTip("Guardar página actual")
        save_file_action.triggered.connect(self.file_save)
        file_toolbar.addAction(save_file_action)

        # similarly creating save action
        saveas_file_action = QAction("Guardar como", self)
        saveas_file_action.setStatusTip("Save current page to specified file")
        saveas_file_action.triggered.connect(self.file_saveas)
        file_toolbar.addAction(saveas_file_action)

        compile_action = QAction("Compilar", self)
        compile_action.setStatusTip("Compilar programa actual")
        compile_action.triggered.connect(self.compilarFile)
        file_toolbar.addAction(compile_action)

        intermediate_action = QAction("CompilarIntermedio", self)
        intermediate_action.setStatusTip("Compilar programa actual")
        intermediate_action.triggered.connect(self.compilarcodigoIntermedio)
        file_toolbar.addAction(intermediate_action)

        # creating another tool bar for editing text
        edit_toolbar = QToolBar("Editar")

        # adding this tool bar to the main window
        self.addToolBar(edit_toolbar)

        # adding actions to the tool bar and menu bar

        # undo action
        undo_action = QAction("Deshacer", self)
        # adding status tip
        undo_action.setStatusTip("Deshacer último cambio")

        # when triggered undo the editor
        undo_action.triggered.connect(self.editor.undo)

        # adding this to tool and menu bar
        edit_toolbar.addAction(undo_action)

        # redo action
        redo_action = QAction("Rehacer", self)
        redo_action.setStatusTip("Rehacer ultimo cambio")

        # when triggered redo the editor
        redo_action.triggered.connect(self.editor.redo)

        # adding this to menu and tool bar
        edit_toolbar.addAction(redo_action)

        # cut action
        cut_action = QAction("Cortar", self)
        cut_action.setStatusTip("Cortar texto seleccionado")

        # when triggered cut the editor text
        cut_action.triggered.connect(self.editor.cut)

        # adding this to menu and tool bar
        edit_toolbar.addAction(cut_action)

        # copy action
        copy_action = QAction("Copiar", self)
        copy_action.setStatusTip("Copiar texto seleccionado")

        # when triggered copy the editor text
        copy_action.triggered.connect(self.editor.copy)

        # adding this to menu and tool bar
        edit_toolbar.addAction(copy_action)

        # paste action
        paste_action = QAction("Pegar", self)
        paste_action.setStatusTip("Pegar de portapapeles")

        # when triggered paste the copied text
        paste_action.triggered.connect(self.editor.paste)

        # adding this to menu and tool bar
        edit_toolbar.addAction(paste_action)

        # select all action
        select_action = QAction("Seleccionar todo", self)
        select_action.setStatusTip("Seleccionar todo el texto")

        # when this triggered select the whole text
        select_action.triggered.connect(self.editor.selectAll)

        # adding this to menu and tool bar
        edit_toolbar.addAction(select_action)

        # wrap action
        wrap_action = QAction("Wrap text to window", self)
        wrap_action.setStatusTip("Check to wrap text to window")

        # making it checkable
        wrap_action.setCheckable(True)

        # making it checked
        wrap_action.setChecked(True)

        # adding action
        wrap_action.triggered.connect(self.edit_toggle_wrap)

        # calling update title methpd
        self.update_title()

        # showing all the components
        self.show()

    # creating dialog critical method
    # to show errors
    def dialog_critical(self, s):

        # creating a QMessageBox object
        dlg = QMessageBox(self)

        # setting text to the dlg
        dlg.setText(s)

        # setting icon to it
        dlg.setIcon(QMessageBox.Critical)

        # showing it
        dlg.show()

    # action called by file open action
    def file_open(self):

        # getting path and bool value
        path, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "",
                                              "Decaf (*.decaf)")

        # if path is true
        if path:
            # try opening path
            try:
                with open(path, 'r') as f:
                    # read the file
                    text = f.read()

            # if some error occured
            except Exception as e:

                # show error using critical method
                self.dialog_critical(str(e))
            # else
            else:
                # update path value
                self.path = path

                # update the text
                self.editor.setPlainText(text)

                # update the title
                self.update_title()

    # action called by file save action
    def file_save(self):

        # if there is no save path
        if self.path is None:

            # call save as method
            return self.file_saveas()

        # else call save to path method
        self._save_to_path(self.path)

    # action called by save as action
    def file_saveas(self):

        # opening path
        path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "",
                                              "Text documents (*.txt);All files (*.*)")

        # if dialog is cancelled i.e no path is selected
        if not path:
            # return this method
            # i.e no action performed
            return

        # else call save to path method
        self._save_to_path(path)

    def compilarFile(self):
        """
        Método para compilar
        """
        if self.path is None:
            return self.file_saveas()
        self._save_to_path(self.path)

        input = self.path

        if self.editor.toPlainText() != '':
            programaCompilado = Compilar(input)

            if programaCompilado.HasLexicalError():
                print('Se encontraron errores semánticos.\n ',
                      programaCompilado.errorFromAntlr.lexicalErrors)
                errores = '\n'.join(
                    programaCompilado.errorFromAntlr.lexicalErrors)
                self.errorForLog.setText(errores)

            else:
                if programaCompilado.printer.tipoNodo[programaCompilado.printer.root] == 'error' or len(programaCompilado.printer.errores.errores) > 0:
                    errores = '\n'.join(
                        programaCompilado.printer.errores.getAllErrors())
                    self.errorForLog.setText(errores)
                else:
                    self.errorForLog.setText(
                        'No se encontraron errores de análisis semántico.')
            self.tabs.setCurrentIndex(1)

    def compilarcodigoIntermedio(self):
        """
        Método para generar Codigo intermedio
        """
        if self.path is None:
            return self.file_saveas()
        self._save_to_path(self.path)

        input = self.path

        if self.editor.toPlainText() != '':
            programaCompilado = CompilarIntermedio(input)
            # we drop the values for the piccke
            infile = open("codigoIntermedioFinal", 'rb')
            arrayIntermedio = pickle.load(infile)
            if(arrayIntermedio != None):
                acumulador=""
                for x in arrayIntermedio:
                    acumulador= acumulador + x + '\n'
                self.errorForlog2.setPlainText(acumulador)
            else:
                self.errorForlog2.setPlainText(
                    'No se ha generado nada de codigo intermedio V2')
            self.tabs.setCurrentIndex(2)
    # save to path method

    def _save_to_path(self, path):

        # get the text
        text = self.editor.toPlainText()

        # try catch block
        try:

            # opening file to write
            with open(path, 'w') as f:

                # write text in the file
                f.write(text)

        # if error occurs
        except Exception as e:

            # show error using critical
            self.dialog_critical(str(e))

        # else do this
        else:
            # change path
            self.path = path
            # update the title
            self.update_title()

    def edit_toggle_wrap(self):
        self.editor.setLineWrapMode(
            1 if self.editor.lineWrapMode() == 0 else 0)

    # update title method
    def update_title(self):
        self.setWindowTitle("%s" % (os.path.basename(self.path)
                                    if self.path else "Untitled"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("PyQt5-Note")
    window = MainWindow()
    app.exec_()
