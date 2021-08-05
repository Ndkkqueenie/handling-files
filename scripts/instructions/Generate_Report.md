## Generate a report
Next, we will write the function write_report. This function writes a dictionary of department: amount to a file.

The report should have the format:

**department1**: **amount1**

**department2**: **amount2**

`def write_report(dictionary, report_file):`

This function requires a dictionary, from the previous section, and report_file, an output file to generate report, to both be passed as parameters.

You will use the open() function to open a file and return a corresponding file object. This function requires file path and file mode to be passed as parameters. The file mode is 'r' (reading) by default, so you should now explicitly pass 'w+' mode (open for reading and writing, overwriting a file) as a parameter.

Once you open the file for writing, iterate through the dictionary and use write() on the file to store the data.

  `with open(report_file, "w+") as f:`
  
    `for k in sorted(dictionary):`
    
      `f.write(str(k)+':'+str(dictionary[k])+'\n')`
      
    `f.close()`
    
Now call the function write_report() by passing a dictionary variable from the previous section and also passing a report_file. The report_file passed within this function should be similar to /home/<username>/data/report.

`write_report(dictionary, '<report_file>')`
  
