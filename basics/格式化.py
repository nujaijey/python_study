# name_1 = input("姓名：")
# score_1 = input("成绩：")
# name_2 = input("姓名：")
# score_2 = input("成绩：")
# avg_score = (float(score_1) + float(score_2))/2
# print("姓名\t成绩")  # \t：横向制表符，相当于按一次tab键

# 占位符
# print("%s\t%s\n%s\t%s\n平均成绩\t%.2f" % (name_1, score_1, name_2, score_2, avg_score))

# format
# print("{:7}\t{}\n{:7}\t{}\n平均成绩\t{:.2f}".format(name_1, score_1, name_2, score_2, avg_score))

# f-string
# print(f'{name_1:7}\t{score_1}\n{name_2:7}\t{score_2}\n平均成绩\t{avg_score:.2f}')

# print("{2:7}\t{1}\n{0:7}\t{3}\n平均成绩\t{4:.2f}".format(name_1, score_1, name_2, score_2, avg_score))


print('接口测试用例执行通过率为{:.2%}'.format(400/500))
