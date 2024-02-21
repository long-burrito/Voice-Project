September 10th: Initial work started, at this time the my-voice-analysis python is being implemented to extract information from voice recordings.

September 19th: README file has been uploaded to the folder. Some tinkering around has been done.

September 23rd: Multiple voice recordings have been recorded and stored within the repository.

October 12th: Started testing the program on different recordings, testing things from speaking speed to total time spoken. These things are easy to test for and are useful for checking whether the program is accurately giving feedback. 

October 26th: Started inputting data from the stats.csv file that represents the average prosodic values of over 600 native speakers into the program. Separated the outputs of the program into 2 different categories: percentiles and raw values in the form of a float. 

October 30th: Added a feature to the program that a new test file can be recorded on the spot so that you can see it work with whatever audio you need it to, rather than a pre-recorded message.

November 7th: Experimented with outputting data from the Pandas DataFrames into a table using the MatPlotLib Python library.

November 9th: Transformed the Pandas dataframe of prosodic values from being separated by columns to being separated by rows to make it easy to compare the average prosodic values to the ones collected by the voice-program.py with the provided audio file. I dropped values that correlate with the length of time spoken to avoid any bias, as making it longer could potentially mess with any comparisons made.

December 5th: Worked on classifier that would identify whether a reader is educated or not.

January 22nd: Found out about cosine similarity and euclidean distance matrices, will implement into final paper

February 2nd: Started conducting recordings of selected readers, 8 in total

February 4th: Finished conducting recordings of selected readers

February 4th: Worked on analyzing the data, collecting it into a .csv file, and then created matrices and did classifier training
