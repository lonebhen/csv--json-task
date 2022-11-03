<h1>CSV conversion to JSON</h1>

<h3>This project reads the content of a csv file and converts it into json file </h3> <br>
<h3>It also calculates the sha256 of all json file and appends it to each line in a new csv file named <b>filename.output.csv</b>.<br>
<br>
The project was made to work has a command line tool (cli)<br>
<br>
This was done with a python module called <strong>Typer </strong> </h3>

<h2> GETTING STARTED </h2>
-- Clone this repository with command <b>git clone https://github.com/lonebhen/csv--json-task.git </b> <br><br>
-- Download all the requirements of this project with command <b>pip install -r requirements.txt</b> <br> <br>
-- Run the project 

<h2> RUNNING THE PROJECT </h2>
-- Use <b>python main.py</b> or <b>python .\main.py</b> to run his project<br>
  <img src="https://github.com/lonebhen/csv--json-task/blob/main/command_to_run.png" alt="Command to run" >
  
  
<h2> OUTPUT </h2>
-- New files would be created which include <br>
  --- JSON files <br>
  --- NEW CSV file <b>filename.output.csv</b>
  
  <h2> OUTPUT LOOK </h2>
  <img src="https://github.com/lonebhen/csv--json-task/blob/main/output1.png" alt="Output 1" ><br>
  <img src="https://github.com/lonebhen/csv--json-task/blob/main/output2.png" alt="Output 2" ><br>
  
  
  <b>This image shows the new csv file created</b><br>
  <img src="https://github.com/lonebhen/csv--json-task/blob/main/output3.png" alt="Output 3" ><br>
  
  
  <img src="https://github.com/lonebhen/csv--json-task/blob/main/terminal%20output.png" alt="Terminal Output" ><br>
  <b> Terminal Output </b>
  
  
  
  <h2>FOLDER AND FILES DESCRIPTION </h2>
  -- The <b>operations folder</b> is a package which contains all the files which work on our csv input <br>
    - <b>csv_operations.py</b> reads from our csv file and writes unto it to give us a new csv file <br>
    - <b>hash.py</b> calculates and returns the sha256 code in hexadecimal of the given json <br>
    - <b>main.py</b> contains the logic of the project 
    
    
    
  
  
  
  
