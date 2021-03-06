#!/usr/bin/env python

import subprocess
import os

def unicycler_runner(fastq_file_forward, fastq_file_reverse, input_directory_path, output_directory_path):
	#Create file paths.
	fastq_file_forward_path = input_directory_path + fastq_file_forward
	fastq_file_reverse_path = input_directory_path + fastq_file_reverse

	#Creating a directory inside output directory.
	output_subdir_name = fastq_file_forward.split('.')[0].split('_')[0]
	output_subdir_path = output_directory_path.rstrip('/') + '/' + output_subdir_name 

	#Check if subdir is already there.
	if not output_subdir_name in os.listdir(output_directory_path):
		os.mkdir(output_subdir_path)

	#Execute Unicycler.
	try:
		print("Running Unicycler for {} and {}".format(fastq_file_forward, fastq_file_reverse))
		uclr_output = subprocess.check_output(["unicycler", "-1", fastq_file_forward_path, "-2", fastq_file_reverse_path, "-o", output_subdir_path])
	except subprocess.CalledProcessError:
		print("Unicycler could not finish the assembly. Please check the files.")
		return False

	print("Successfully ran Unicycler for {} and {}".format(fastq_file_forward, fastq_file_reverse))
	return True


if __name__ == "__main__":
	status = main()
	print(status)