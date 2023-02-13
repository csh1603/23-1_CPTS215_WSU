##############################################
# Title: PA1 - Tweets
# Author: Seunghyun Cho
# Version: 3.10.6
# Date: Feb 4th, 2023
#
# Description: This program merges two tweet feeds into one reverse chronological order.
##############################################
import re
import sys

def main():
    # give file name as a parameter to t1(first original tweet), t2(second original tweet), and out(output file)
    t1 = sys.argv[1]
    t2 = sys.argv[2]
    out = sys.argv[3]

    # make a list of information (records_list_1, records_list_2) per line in each file (t1, t2)
    records_list_1 = read_tweets(t1)
    records_list_2 = read_tweets(t2)

    print("Reading files...")
    # print which file has more tweets
    if len(records_list_1) > len(records_list_2):
        print("{0} contained the most tweets with {1}.".format(t1, len(records_list_1)))
    elif len(records_list_2) > len(records_list_1) :
        print("{0} contained the most tweets with {1}.".format(t2, len(records_list_2)))
    else:
        print("{0} and {1} contained the same amount of tweets with {3}".format(t1, t2, len(records_list_1)))

    # merging files
    print("\nMerging files...")
    merged_list = merge_tweets(records_list_1, records_list_2)
    print("Files Merged.")

    # write output of merge_tweets() into out
    print("\nWriting file...")
    write_tweets(out, merged_list)
    print("File written.")

    # using 'for' to show top 5 newest tweets
    print("\nDisplaying 5 newest tweeters and tweets.")
    for i in range(5):
        print("@{0} \"{1}\"".format(merged_list[i].get('tweeter'), format(merged_list[i].get('tweet'))))

# make the dictionary of tweets containing each information (tweeter, tweet, when they posted)
# then put them into list and return the list
def read_tweets(file):
    # returning list
    record_list = []
    # open file and divide into each information
    with open (file, "r", encoding = 'utf-8') as f:
        for line in f:
            # divide information by their traits (tweeter, tweet, year, month, year, day, time)
            match = re.search(r'@(\w+) "(.*)" (\d+) (\d+) (\d+) (\d+:\d+:\d+)', line)
            # If it has more information, put more in record_list
            if match:
                record_list.append({'tweeter': match.group(1), 'tweet': match.group(2), 'year': int(match.group(3)), 'month': int(match.group(4)), 'day': int(match.group(5)), 'time': match.group(6)})
    return record_list

# merge two tweets into reverse chronological order
def merge_tweets(list1, list2):
    # list containing merged information, does not have any order
    temp_list = []
    for i in range(len(list1)):
        temp_list.append(list1[i])
    for i in range(len(list2)):
        temp_list.append(list2[i])
    # merging by the time the tweet is posted - newest is on the top
    merged_list = sorted(temp_list, key = lambda tweet: (tweet['year'], tweet['month'], tweet['day'], tweet['time']), reverse = True)
    return merged_list

# write merged list into output file (out)
def write_tweets(out, merged_list):
    with open (out, "w+", encoding = 'utf-8') as f:
        # repeat as much as the amount of data on list
        for i in range(len(merged_list)):
            f.write("@" + merged_list[i].get('tweeter'))
            f.write(" \"" + merged_list[i].get('tweet')+"\" ")
            f.write(str(merged_list[i].get('year')) + " ")
            f.write(str(merged_list[i].get('month')) + " ")
            f.write(str(merged_list[i].get('day')) + " ")
            f.write(merged_list[i].get('time'))
            f.write("\n")
    f.close()

if __name__ == "__main__":
    main()