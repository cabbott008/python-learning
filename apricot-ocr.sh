#! /usr/bin/env bash

for file in /home/ca/Documents/ocr/Apricot*.png; do tesseract $file ${file/.txt/}; done

for file in /home/ca/Documents/ocr/Apricot*.txt; do cat $file >> /home/ca/Documents/ocr/FinalOutput.txt; done
