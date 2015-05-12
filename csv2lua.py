#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Convert csv file to lua script'''

import os
import os.path
import csv
import gl

def get_outputfile_name(inputname):
    # if inputEnds not in inputname:
    #     print("error file: ", inputname)
    #     return
    # outputDirName = os.path.join(os.getcwd(), outputDir)
    return inputname + ".lua"
    # return os.path.join(outputDirName, outputname)

def write2lua(filekey, f, row, i, keysArr, typesArr):
    print 'write begin', i, row, len(row)
    newDefine = False
    if row[0] != "":
        gl.name = row[0]
        gl.level = 1
        newDefine = True
    if newDefine:
        f.writelines(filekey + "." + gl.name + " = {\n")
        for index, item in enumerate(row):
            if index >= 1:
                k = keysArr[index]
                t = typesArr[index].lower()
                if t == "number":
                    if item == "":
                        f.writelines("    " + k + " = " + "0,\n")
                    else:
                        f.writelines("    " + k + " = " + item + ",\n")
                elif t == "bool":
                    if item == "":
                        f.writelines("    " + k + " = " + "false,\n")
                    else:
                        f.writelines("    " + k + " = " + item.lower() + ",\n")
                elif t == "string":
                    f.writelines("    " + k + ' = "' + item + '",\n' )
                else:
                    print 'Error, unsupport type: ', t
                    return
        f.writelines("}\n\n")

    f.writelines("why!!!!!!!!!!!!!!!!!\n\n")
    print 'why222222'
    f.wirtelines("why22222222")
    f.writelines(filekey + "." + gl.name + "\[" + gl.level + "\] = {\n")
    print 'why2!!!!!!!!!!!!!!!!!!!!!!!!!'
    for index, item in enumerate(row):
        if index >= 1:
            k = keysArr[index]
            t = typesArr[index].lower()
            if t == "int":
                if item == "":
                    f.writelines("    " + k + " = " + "0,\n")
                else:
                    f.writelines("    " + k + " = " + item + ",\n")
            elif t == "bool":
                if item == "":
                    f.writelines("    " + k + " = " + "false,\n")
                else:
                    f.writelines("    " + k + " = " + item.lower() + ",\n")
            elif t == "string":
                f.writelines("    " + k + ' = "' + item + '",\n' )
            else:
                print 'Error, unsuppurt type: ', t
            return

    f.writelines("}\n\n")
    gl.level += 1

def convert2lua(inputname):
    try:
        with open(inputname, "rb") as f:
            reader = csv.reader(f)

            print "write start"
            tempkey = inputname[:-4]
            print tempkey, inputname
            outputname = get_outputfile_name(tempkey)
            print 'outputname: ', outputname
            filekey = str.split(tempkey, "/")[-1]
            print outputname, filekey
            f = open(outputname, "w")
            f.write("-- this file is generated by program!\n-- never modify it!!!\n-- source file: " + filekey + ".csv\n\n")
            f.writelines("local " + filekey + " = {}\n\n")

            i = 0
            for row in reader:
                i += 1
                print i, gl.keyLine, gl.typeLine, gl.defineLine
                if len(row) <= 0:
                    print 'Error, len(row) <= 0', inputname, i
                    return
                if i == gl.keyLine:
                    print '11111'
                    gl.keysArr = row
                    continue
                if i == gl.typeLine:
                    print '22222'
                    gl.typesArr = row
                    continue
                if i >= gl.defineLine:
                    print i, gl.defineLine
                    print len(gl.keysArr), len(gl.typesArr)
                    print "main: ", i, gl.keysArr, gl.typesArr
                    print
                    if len(gl.keysArr) <= 0 or len(gl.typesArr) <= 0:
                        print 'Error, no keysArr or typesArr', i, gl.keysArr, gl.typesArr
                        return
                else:
                    print "else, ", i
                    continue

                write2lua(filekey, f, row, i, gl.keysArr, gl.typesArr)
    except:
        print 'Error, fail convert:', inputname
        print

def get_filename_list(dirname):
    flist = []
    for root, dirs, files in os.walk(dirname):
        for name in files:
            if name.endswith(gl.inputEnds):
                flist.append(os.path.join(root, name))
    return flist

def explore():
    inputDirName = os.path.join(os.getcwd(), gl.inputDir)
    print inputDirName
    flist = get_filename_list(inputDirName)
    for fname in flist:
        print(fname)
        convert2lua(fname)
    print("Finished!")

if __name__ == '__main__':
    # with open("building.csv", "rb") as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         print row
    #         print
    #     print reader
    explore()