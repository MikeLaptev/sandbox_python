'''
Created on Jul 29, 2015

@author: Mikhail
'''

import os
import re
import threading
import Queue
import json_file_generator

class ParallelJSONProcessing:
    
    def __init__(self, json_file_gen, output_file_name, start_directory = ".", pattern = "data_\d+(\.\d+)?\.json"):
        self.json_generator = json_file_gen
        self.output_file_name = output_file_name
        self.start_directory = start_directory
        self.pattern = pattern
        self.lock = threading.Lock()
        

    def load_list_of_json_files(self, directory, pattern):
        """
        This function loads list of files according to specific pattern
        @param directory: initial directory with json files
        @param pattern: pattern for json files names
        @return: list of files
        """
        files = []
        for name in os.listdir(directory):
            file_or_dir_name = os.path.join(directory, name)
            # we should process only files
            if os.path.isfile(file_or_dir_name):
                search_results = re.search(re.escape(os.sep) + pattern + "$", file_or_dir_name)
                if search_results is not None:
                    files.append(file_or_dir_name)
        
        return files
    
    def load_queue_of_json_files(self, directory, pattern):
        """
        This function loads list of files according to specific pattern
        @param directory: initial directory with json files
        @param pattern: pattern for json files names
        @return: list of files as a queue
        """
        files = Queue.Queue()
        for name in os.listdir(directory):
            file_or_dir_name = os.path.join(directory, name)
            # we should process only files
            if os.path.isfile(file_or_dir_name):
                search_results = re.search(re.escape(os.sep) + pattern + "$", file_or_dir_name)
                if search_results is not None:
                    files.put(file_or_dir_name)
        
        return files
    
    def process_list_of_json_files_in_parallel(self, num_of_threads = 4):
        num_of_threads = num_of_threads if num_of_threads > 1 else 1
        list_of_threads = []
        queue_with_json_files = self.load_queue_of_json_files(self.start_directory, self.pattern)
        # create list of threads
        for dummy_i in xrange(num_of_threads):
            list_of_threads.append(ProcessJSONFile(self.json_generator, queue_with_json_files, self.output_file_name, self.lock))
        # launch list of threads
        for thread_obj in list_of_threads:
            thread_obj.start()
        # join started threads to main thread
        for thread_obj in list_of_threads:
            thread_obj.join()
        

class ProcessJSONFile(threading.Thread):
    
    def __init__(self, json_generator, queue, file_with_results_name, lock):
        threading.Thread.__init__(self)
        self.json_generator = json_generator
        self.file_queue = queue
        self.results_file_name = file_with_results_name
        self.lock = lock 
    
    def calculate_checksum(self, file_name):
        """
        This function calculates seeming checksum for the file from parameter
        @param file_name: name of the json file to calculate seeming checksum 
        """
        data_from_file = self.json_generator.load_data_from_json_file(file_name)
            
        return sum(data_from_file.values())
    
    def run(self):
        
        while not self.file_queue.empty():
            # acquire the lock
            with self.lock:
                # get next file for processing
                next_file = self.file_queue.get()
                # calculate the checksum for the file
                checksum = self.calculate_checksum(next_file)
                # update the file
                with open(self.results_file_name, 'a+') as f:
                    f.write("{} >> {} >> {}\n".format(threading.current_thread().ident, next_file, checksum))


def clean_up(dir_with_tests = ".", postfix = ".json"):
    for name in os.listdir(dir_with_tests):
        if name.endswith(postfix): 
            file_or_dir_name = os.path.join(dir_with_tests, name)
            # we should process only files
            if os.path.isfile(file_or_dir_name):
                os.remove(file_or_dir_name)
    

if __name__ == '__main__':
    clean_up()
    # generate required list of json files
    json_generator = json_file_generator.MyOwnJSONProcessing()
    json_generator.generate_set_of_files_with_json_obj(1000)
    # launch processing of these files in parallel
    parallel_json_processing = ParallelJSONProcessing(json_generator, "result.log")
    parallel_json_processing.process_list_of_json_files_in_parallel()