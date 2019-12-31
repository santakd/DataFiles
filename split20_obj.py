import pandas as pd
import getopt
import sys
import time
import memory_profiler

# usage
# python3 split20_obj.py <num of columns>
# python3 split20_obj.py 20

def main():
    numCols = int(sys.argv[1])
    dfSource = pd.read_csv(r'./ObjectId.csv')
    iterflag = 0
    splitfiles_rows=[]
    temp_rows = {}
    print("-------------------------------------")
    print(dfSource.count())
    for index, row in dfSource.iterrows():
        iterflag = iterflag+1
        # print(iterflag==numCols)
        temp_rows[iterflag]=row['ObjectId']
        if(iterflag==numCols):
            # print("here")
            splitfiles_rows.append(temp_rows)
            temp_rows={}
            iterflag=0
            # break
    df=pd.DataFrame(splitfiles_rows)
    #df.to_csv('./peg_test_data_'+str(numCols)+'.csv',sep=',', index=False, header=True)
    df.to_csv('./03_SmartClient_20.csv',sep=',', index=False, header=True)
    print("-------------------------------------")

if __name__ == "__main__":
    m1 = memory_profiler.memory_usage()
    t1 = time.clock()
    main()
    t2 = time.clock()
    m2 = memory_profiler.memory_usage()
    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]
    print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this program")
    print("-------------------------------------")
