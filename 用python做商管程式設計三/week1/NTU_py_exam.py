import csv

class time: # 建立一個time的class裡面有三種變數(hour, min, sec)
    def __init__(self, hour, min, sec):
        self.hour = hour
        self.min = min
        self.sec = sec

start_time = input("enter the start time that you want to calculate: ").split(":")
startTime = time(start_time[0], start_time[1], start_time[2])
end_time = input("enter the end time that you want to calculate: ").split(":")
endTime = time(end_time[0], end_time[1], end_time[2])

def calculate(total_status, problem_number, status):
    if status == 'Accepted':
        total_status[problem_number][0] += 1
    elif status == 'Compile Error':
        total_status[problem_number][1] += 1
    elif status == 'Runtime Error':
        total_status[problem_number][2] += 1
    elif status == 'Time Limit Exceed':
        total_status[problem_number][3] += 1
    else:
        total_status[problem_number][4] += 1

file_1 = r"C:\Users\user\Desktop\vscode\python\NTU_py\midterm2.csv" # 字串前加入r符號，可以讓字串內的跳脫字元失去效用
with open(file_1, "r", encoding='utf-8') as csvfile: # 開啟檔案並讀取他
    reader = csv.DictReader(csvfile) # 可用column的名字來稱呼該column，且會自動忽略column名稱那行
    total_status = [[0] * 5 for _ in range(4)] # 結果有五種，題目有四題

    for row in reader:
        submission_time = row['SubmissionTime'].split(":")
        Time = time(submission_time[0], submission_time[1], submission_time[2]) # 用class存提交時間
        problem_number = int(row['Problem'])-1 # 記錄此題是第幾題
        status = row['Status'] # 記錄此題的提交狀態
        if startTime.hour == endTime.hour and startTime.hour == Time.hour: # 起始時間語結束時間在同一個小時內，且提交時間也在同一小時內
            if startTime.min == endTime.min and startTime.min == Time.min: # 起始時間語結束時間在同一個分鐘內，且提交時間也在同一分鐘內
                if Time.sec >= startTime.sec and Time.sec <= endTime.sec: # 此種情況只要秒數在兩者範圍內就要記錄
                    # print(row['SubmissionID'])
                    calculate(total_status, problem_number, status)
            elif Time.min >= startTime.min and Time.min < endTime.min: # 起始時間與結束時間在同一小時內，但分鐘數不同
                if  Time.sec >= startTime.sec: # 此種情況只要分鐘在兩者範圍內且秒數在起始範圍以上即可
                    # print(row['SubmissionID'])
                    calculate(total_status, problem_number, status)
            elif Time.min == endTime.min: # 起始時間與結束時間在同一小時內，且提交時間恰好在結束時間上
                if Time.sec <= endTime.sec: # 此種情況只要秒數在結束範圍以內即可
                    # print(row['SubmissionID'])
                    calculate(total_status, problem_number, status)
        elif Time.hour > startTime.hour and Time.hour < endTime.hour : # 起始時間與結束時間在不同小時，且提交時間剛好在這範圍內，此種情況皆要記錄
            # print(row['SubmissionID'])
            calculate(total_status, problem_number, status)
        elif Time.hour == startTime.hour: # 起始時間與結束時間在不同小時，且提交時間恰好與起始時間同一小時
            if Time.min > startTime.min: # 此種情況只要分鐘數在起始範圍以上即可
                # print(row['SubmissionID'])
                calculate(total_status, problem_number, status)
            elif Time.min == startTime.min: # 若恰好提交時間與起始時間同一分鐘
                if Time.sec >= startTime.sec: # 此種情況則要判斷秒數是否在起始範圍以上
                    # print(row['SubmissionID'])
                    calculate(total_status, problem_number, status)
        elif Time.hour == endTime.hour: # 起始時間與結束時間在不同小時，且提交時間恰好與結束時間同一小時
            if Time.min < endTime.min: # 此種情況只要分鐘數在結束範圍以內即可
                # print(row['SubmissionID'])
                calculate(total_status, problem_number, status)
            elif Time.min == endTime.min: # 若恰好提交時間與結束時間同一分鐘
                if Time.sec <= endTime.sec: # 此種情況則要判斷秒數是否在結束範圍以內
                    # print(row['SubmissionID'])
                    calculate(total_status, problem_number, status)

print(f"{total_status[0]};{total_status[1]};{total_status[2]};{total_status[3]};")
