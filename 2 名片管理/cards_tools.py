# 记录所有的名片字典
cards_list = []

def show_menu():
    #  显示菜单
    print("*" * 50)
    print("欢迎使用【名片管理系统】 v 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)

def new_card():
    
    print("-" * 50)
    print("新增名片")

    #1. 提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq号码：")
    email_str = input("请输入邮箱：")

    cards_dict = {"name": name_str, 
                  "phone": phone_str,
                  "qq": qq_str, 
                  "email": email_str}

    cards_list.append(cards_dict)
    
    print(cards_list)

    print("添加 %s 的名片成功" % name_str)

def show_all():
    print("-" * 50)
    print("显示所有名片")

    # 
    if len(cards_list) == 0:
        print("请输入名片信息！")

        # return:
        return

    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end = "\t\t")
        
    print("")

    print("=" * 50)

    for cards_dict in cards_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (cards_dict["name"],
                                             cards_dict["phone"],
                                             cards_dict["qq"],
                                             cards_dict["email"]))

def search_card():
    print("-" * 50)
    print("搜索名片")

    # 1. 提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名：")

    # 2. 遍历名片列表，查找要搜索的姓名，如果没有找到，需要提示用户
    for cards_dict in cards_list:
        if cards_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱\t\t")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (cards_dict["name"],
                                             cards_dict["phone"],
                                             cards_dict["qq"],
                                             cards_dict["email"]))

            # TODO 针对找到的名片记录执行修改和删除的操作
            deal_card(cards_dict)

            break

    else:
        print("抱歉，没有找到 %s" % find_name)


def deal_card(find_dict):
    print(find_dict)

    action_str = input("请选择要执行的操作 [1] 修改 [2] 删除 [0] 返回上级菜单")

    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ：")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：")
        print("修改名片成功！")

    elif action_str == "2":
        cards_list.remove(find_dict)
        print("删除名片成功！")

def input_card_info(dict_value, tip_message):

    # 提示用户输入内容 
    result_str = input(tip_message)

    # 针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str

    # 如果用户没有输入内容，返回‘字典中原有的值’ 
    else:
        return dict_value   
