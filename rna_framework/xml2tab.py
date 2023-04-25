######################################################################################################
# Convert an XML file output from the RNA framework to a tab-delimited file
#
# Author: Kobie Kirven
######################################################################################################

#-- Imports --#
import argparse 
import os
import xml.etree.ElementTree as ET

# -- functions --
def get_tab(react_file, output):

    # get the sequence and id
    tree = ET.parse(react_file)
    root = tree.getroot()
    for child in root:
        data = "".join(child[1].text.split("\n\t\t\t")).strip("\n\t\t").split(",")
        output.write(f"{child.attrib['id']}\t{','.join(data).strip(')')}\n")

def get_xml_files_in_dir(directory):
    if directory.endswith("/"):
        return [directory + f for f in os.listdir(directory) if f.endswith(".xml")]
    else:
        return [directory + "/" + f for f in os.listdir(directory) if f.endswith(".xml")]

# -- main -- #
if __name__ == "__main__":

    # get the arguments
    parser = argparse.ArgumentParser(description='Convert an XML file or directory of XML files output from the RNA framework to a tab-delimited file')
    parser.add_argument('-i', dest="react_file", help='XML file or directory of XML files')
    parser.add_argument('-o', dest="out_file", help='fasta file')
    args = parser.parse_args()

    # get the tab file
    output = open(args.out_file, "w")
    if args.react_file.endswith(".xml"):
        get_tab(args.react_file, output)
    else:
        xml_files = get_xml_files_in_dir(args.react_file)
        for xml_file in xml_files:
            get_tab(xml_file, output)
