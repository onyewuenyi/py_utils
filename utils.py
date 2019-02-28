import os
import gzip
import re

# TODO mv to cfg file
groups = {
    "seq": [],
    "clk": [],
    "gcdn": []
} 
STDLIB_CELL_PREFIX = "ec0" # project specific 


def is_gzip(filepath):
    return filepath.endswith(".gz")

def parse_cells(filepath, group):
    """
    Return a list of of the cell group from a netlist
    filepath - netlist path
    group - list of the stdlib cell groups patterns
    out - list of cells of the specified group 

    groups - seq, clk, gcdn, comb
    """
    cell_list = []
    if is_gzip:
        with gzip.open(filepath) as f:
            for line in f:
                line = line.strip()
                if not line.startswith(f{STDLIB_CELL_PREFIX}):
                    continue
                    
                for cel in group:
                    re_obj = re.compile(rf'(\S+{cell}\S+$')
                    match = re_obj.search(line)

                    if match:
                        cell_list.append(match.groups()[0]) 
    else:
        with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line.startswith(f{STDLIB_CELL_PREFIX}):
                continue
                
            for cel in group:
                re_obj = re.compile(rf'(\S+{cell}\S+$')
                match = re_obj.search(line)

                if match:
                    cell_list.append(match.groups()[0]) 
    return cell_list



