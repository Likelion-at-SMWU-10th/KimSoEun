total_list = [] # 1) dictionary로 저장한다면?

# 질문 추가
while True:
    question = input("질문을 입력해주세요 : ")
    if (question == "q"):
        break
    else:
        total_list.append({"질문":question, "답변":""}) # 1) total_dictionary[question] = ""

# 질문에 대한 답변 저장
for i in total_list:
    print(i["질문"])    # 1) print(i)
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer  # 1) total_dictionary[i] = answer
print(total_list)