# BQUtils

- log in to gcloud project
- move your csv files to `upload` dir 

`python3 CSV2BQ.py`

#### Sample Output

➜  util git:(master) ✗ python3 CSV2BQ.py
 uploading total 48 to BQ
bq load --autodetect --source_format=CSV sample.table1 ./output/table1.csv
Upload complete.
Waiting on bqjob_r323abd4836be6560_0000016fda350922_1 ... (1s) Current status: DONE   
bq load --autodetect --source_format=CSV sample.table2 ./output/table2.csv
Upload complete.
