import os

dst_files = os.listdir("./dash/data")
src_files = os.listdir("../abr_server/probability/user-study")

for src_file in src_files:
    uid = src_file.strip(".txt")

    if uid not in dst_files:
        # print(uid)

        cmd = f"scp -r zhuqi@172.29.114.202:~/Documents/ttstream/contentServer/dash/data-5/{uid}/ ./dash/data/"

        print(cmd)

        # os.system(cmd)
    tmp = 1

    # v12044gd0000cc6gm2bc77u6pg1mi2n0