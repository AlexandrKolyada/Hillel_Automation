from  datetime import datetime

search_line = 'TSTFEED0300|7E3E|0400'
all_timestamps = []
with open('hblog.txt', 'r', encoding='utf-8') as  file:
    for line in file:
        if search_line in line:
            index_time = line.find('Timestamp')
            time_str = line[index_time + 10 : index_time + 18]
            time_obj = datetime.strptime(time_str, "%H:%M:%S")
            all_timestamps.append(time_obj)

for i in range(len(all_timestamps) -1):
    current_time = all_timestamps[i]
    next_time = all_timestamps[i + 1]
    difference = current_time - next_time
    seconds = abs(difference.total_seconds())
    print(f"diff {i} and {i + 1}: {seconds}")

    with open('hb_test.log', 'a') as log_file:
        if 31 < seconds < 33:
            log_message = f"WARNING: Heartbeat {seconds}s at {current_time.strftime('%H:%M:%S')}\n"
            log_file.write(log_message)
            print(log_message.split())
        elif seconds >= 33:
            log_message = f"ERROR: Heartbeat {seconds}s at {current_time.strftime('%H:%M:%S')}\n"
            log_file.write(log_message)
            print(log_message.strip())