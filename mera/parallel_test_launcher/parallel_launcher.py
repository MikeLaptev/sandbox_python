'''
Created on Jul 27, 2015

@author: Mikhail
'''
import os
import re
import subprocess
import threading
import time

python_exe_name = "python"
unittest_launch_parameters = "-m"
unittest_module_name = "unittest"

def get_list_of_tests(dir_with_tests):
    """
    Function reads list of files with tests in path.
    @warning: this function does not go recursively to subfolders
    @return: list of files in directory from parameters (full path to file)
    """
    # initial array for list of files
    files = []
    for name in os.listdir(dir_with_tests):
        file_or_dir_name = os.path.join(dir_with_tests, name)
        # we should process only files
        if os.path.isfile(file_or_dir_name):
            files.append(file_or_dir_name)
    
    return files

def get_list_of_tests_by_filter(dir_with_tests, file_name_filter):
    """
    Function returns list of files according to the filter
    from the directory.
    @warning: filter should be regex pattern 
    @return: list of files that names coincide with filter
    """
    # get full list of files in the directory
    all_files = get_list_of_tests(dir_with_tests)
    required_files = []
    
    for full_file_name in all_files:
        search_results = re.search(re.escape(os.sep) + file_name_filter + "$", full_file_name)
        if search_results is not None:
            required_files.append(full_file_name)
        
    return required_files

def run_test_module(module_name):
    subprocess.call([python_exe_name, unittest_launch_parameters, unittest_module_name, module_name])

if __name__ == '__main__':
    file_name_filter = "(test_\\d+)\\.py"
    list_of_test_files = get_list_of_tests_by_filter(".", file_name_filter)
    threads = []
    # creating list of threads
    for full_file_name in list_of_test_files:
        # get name of module
        search_results = re.search(re.escape(os.sep) + file_name_filter + "$", full_file_name)
        threads.append(threading.Thread(target=run_test_module, args=(search_results.group(1),)))
    start_time = time.time()
    
    # launching list of threads
    for thread_object in threads:
        thread_object.start()

    # join the main thread
    for thread_object in threads:
        thread_object.join()
        
    finish_time = time.time()
    print "Launching time:", (finish_time - start_time), "seconds"