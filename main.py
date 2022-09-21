from pydub import AudioSegment
from os import walk, path
from inputimeout_kureha_edit import inputimeout, TimeoutOccurred

if __name__ == "__main__":
    # 到时候换成Win32 API
    # https://blog.csdn.net/weixin_44634704/article/details/123006497
    kugou_folder_path = input("KuGou Music Download Path >> ").strip(" ").strip("'").strip("\"")

    meta_file_data_base = []
    change_file_data_base = []

    for (path_, dir_list, file_list) in walk(kugou_folder_path):
        for file_name in file_list:
            meta_file_data_base.append(path.join(path_, file_name))

    while True:
        # print(f"\r开始监视酷狗下载文件夹 -- 新增{len(change_file_data_base)}个文件。", end="")
        # print("下载完成开始移动文件请按下 e和回车 。")
        # key = input("")
        try:
            key = inputimeout(prompt=f"\r开始监视酷狗下载文件夹 -- 新增{len(change_file_data_base)}个文件。", timeout=3)
        except TimeoutOccurred:
            key = 0
        if key in {"E", "e"}:
            break
        for (pr_path, pr_dir_list, pr_file_list) in walk(kugou_folder_path):
            for pr_file_name in pr_file_list:
                try:
                    meta_file_data_base.index(path.join(pr_path, pr_file_name))
                except ValueError as VE:
                    meta_file_data_base.append(path.join(pr_path, pr_file_name))
                    change_file_data_base.append(path.join(pr_path, pr_file_name))

    # TODO: 之后开始写用户结束监视后的 文件筛选 文件自动转换 文件自动转移至目标目录
