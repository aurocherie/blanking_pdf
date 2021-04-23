#!/usr/bin/python3

import fitz
import sys, getopt

# Usage : insert_rect.py -i inputfile (without ext pdf) -d x_first_pages_to_delete -g x_first_pages_with_big_pict -p small_pic_from_page_y -l lateral_page_from_page_z
 
#input_file = "OME_DH_DS_000045_ES_v04.1.pdf"
#output_file = "OOME_DH_DS_000045_ES_v04.1vu.pdf"
#barcode_file = "/local/home/ronan/soft/Pdf_TB04/essai/blanc.png"

bigpicture = "/local/home/ronan/soft/Pdf_TB04/essai/big_blanc.png"
lateralpicture = "/local/home/ronan/soft/Pdf_TB04/essai/lateral_blanc.png"
smallpicture = "/local/home/ronan/soft/Pdf_TB04/essai/small_blanc.png"
#smallpicture = "/local/home/ronan/soft/Pdf_TB04/essai/big_blanc.png"
#lateralpicture = "/local/home/ronan/soft/Pdf_TB04/essai/big_blanc.png"

def main(argv):

 input_file = ''
 output_file = ''
 nb_delete = 0
 nb_big = 0
 nb_small = 0
 nb_lateral = 0

 try:
     opts, args = getopt.getopt(argv,"i:d:g:p:l:",["ifile=","ofile="])
 except getopt.GetoptError:
      print ('insert_rect.py -i inputfile -d x_first_pages_to_delete -g x_first_pages_with_big_pict -p small_pic_from_page_y -l lateral_page_from_page_z')
      sys.exit(2)
 for opt, arg in opts:
      if opt == '-h':
         print ('insert_rect.py -i inputfile -d x_first_pages_to_delete -g x_first_pages_with_big_pict -p small_pic_from_page_y -l lateral_page_from_page_z')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         input_file = arg + ".pdf"
         output_file = arg + "_vu.pdf"
      elif opt in ("-d", "--ifile"):
         nb_delete = int(arg)
         print("delete ",nb_delete," first pages")
      elif opt in ("-g", "--ofile"):
         nb_big = int(arg)
         print("big picture on ",nb_big," first pages")
      elif opt in ("-p", "--ofile"):
         nb_small = int(arg)
         print("small picture from page ",nb_small)
      elif opt in ("-l", "--ofile"):
         nb_lateral = int(arg)
         print("lateral picture from page ",nb_lateral)
   
 print ('Input file is ', input_file)
 print ('Output file is ', output_file)

# insert big picture
 image_file = open(bigpicture, 'rb').read()
 # define the position (upper-right corner)
 image_rectangle = fitz.Rect(0,-80,750,210)
 # retrieve the first page of the PDF
 file_handle = fitz.open(input_file)
# first_page = file_handle[0]
 for page in file_handle.pages(0, nb_big, 1):
      # add the image
      page.insertImage(image_rectangle, stream=image_file)

# insert small picture
 image_file = open(smallpicture, 'rb').read()
 # define the position (upper-right corner) 1000 55
 image_rectangle = fitz.Rect(0,0,400,35)
 # retrieve the first page of the PDF
# file_handle = fitz.open(input_file)
 for page in file_handle.pages(nb_small, file_handle.pageCount, 1):
      # add the image
      page.insertImage(image_rectangle, stream=image_file)

# insert lateral picture
 image_file = open(lateralpicture, 'rb').read()
 # define the position (upper-right corner)
 image_rectangle = fitz.Rect(510,-50,720,850)
 # retrieve the first page of the PDF
# file_handle = fitz.open(input_file)
 for page in file_handle.pages(nb_lateral, file_handle.pageCount, 1):
      # add the image
      page.insertImage(image_rectangle, stream=image_file)

# delete first pages
 l = list(range(nb_delete, file_handle.pageCount))    # 2-end
 file_handle.select(l)                           # delete all others
 file_handle.save(output_file, garbage=3) # save and clean new PDF
 file_handle.close()

 #file_handle.save(output_file)

if __name__ == "__main__":
   main(sys.argv[1:])
