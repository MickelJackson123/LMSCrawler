day_dic = {"sat": 6, "sun": 0, "mon": 1, "tue": 2, "wed": 3, "thu": 4, "fri": 5}
static_part = " cd $HOME/PycharmProjects/LMSCrawler && ./runner.sh"
info = open("info.txt", "r")
cron = open("cron.txt", "w")
cron.write("DISPLAY=:0\n\n")

for index, line in enumerate(info.readlines()):
    if index > 1:
        line = line.strip()
        day = day_dic[line.split(",")[0]]
        hour_min = line.split(",")[1]
        hour = hour_min.split(":")[0]
        minute = hour_min.split(":")[1]
        dynamic_part = "{}0 {} * * {}".format(minute, hour, day)
        cron_job = dynamic_part + static_part + "\n"
        cron.write(cron_job)
