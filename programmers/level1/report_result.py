def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    report_id = []
    num_of_report = []
    stop_id = []
    #중복 제거
    report = list(dict.fromkeys(report))
    #신고된 아이디 구하기
    for id in report:
        report_id.append(list(id.split())[1])
    for id in id_list:
        if id in report_id:
            count = count_num_of_report(id,report_id)
            num_of_report.append(count)
        else:
            num_of_report.append(0)
    for num in num_of_report:
        if num >= k:
            stop_id.append(id_list[num_of_report.index(num)])
            num_of_report[num_of_report.index(num)] = -1
    for id in report:
        if id.split()[1] in stop_id:
            answer[id_list.index(id.split()[0])] += 1
    
    return answer
        
def count_num_of_report(element,report_id):
    count = 0
    for i in report_id:
        if element == i:
            count += 1
    return count
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

print(solution(id_list,report,k))