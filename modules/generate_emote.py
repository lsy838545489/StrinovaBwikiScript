# modules/generate_emote.py
import os
from utils.common import load_json_file, format_lua_table, export_data_file


def export_emote_data():
    print("开始处理表情(Emote)数据喵...")

    id_to_Role_name = {
        20101001: "米雪儿·李",
        20105001: "奥黛丽·格罗夫",
        20107001: "玛德蕾娜·利里",
        20108001: "信",
        20109001: "令",
        20110001: "白墨",
        20112001: "绯莎",
        20115001: "芙拉薇娅",
        20119001: "艾卡",
        20120001: "珐格兰丝",
        20121001: "忧雾",
        20122001: "玛拉",
        20123001: "蕾欧娜",
        20124001: "心夏",
        20125001: "千代",
        20128001: "拉薇",
        20130001: "汐",
        20131001: "伊薇特",
        20132001: "明",
        20133001: "梅瑞狄斯",
        20137001: "香奈美",
        20146001: "星绘",
        20205001: "加拉蒂亚·利里",
        20101201: "米雪儿·李",
        20128201: "拉薇",
        20131201: "伊薇特",
        20124201: "心夏",
        20105201: "奥黛丽·格罗夫",
        20107201: "玛德蕾娜·利里",
        20112201: "绯莎",
        20133201: "梅瑞狄斯",
        20137201: "香奈美",
        20146201: "星绘",
    }

    # 自定义键映射
    custom_keys = {
        "ID": "id",
        "Name": "name",
        "Role": "role",
        "Quality": "quality",
        "File": "file",
        "Get": "get",
        "Desc": "desc"
    }

    Emote_data = load_json_file("Emote")
    if not Emote_data:
        return

    output_data = []

    # 处理 Emote_data 中的每一项
    for item in Emote_data:
        for row in item['Rows'].values():
            gain_param2 = row.get('GainParam2', {})
            raw_get_str = gain_param2.get(
                'LocalizedString', '').replace('储备', '未实装')
            gain_param2_value = [raw_get_str] if raw_get_str else []

            asset_path_name = row['IconItem'].get('AssetPathName', '')
            tail_number = asset_path_name.split('.')[-1].split('_')[-1]

            Desc_string = row['Desc'].get(
                'LocalizedString', '').replace('\n', '')

            Role_id = id_to_Role_name.get(
                row.get('RoleSkinId', 0), row.get('RoleSkinId', ''))

            extracted_data = {
                "ID": row['Id'],
                "Name": row['Name'].get('LocalizedString', ''),
                "Role": Role_id,
                "Quality": row['Quality'],
                "File": f"表情_{tail_number}.png",
                "Get": gain_param2_value,
                "Desc": Desc_string
            }

            # 将提取的数据映射到自定义键
            custom_data = {
                custom_keys[key]: value for key, value in extracted_data.items()}
            output_data.append(custom_data)

    export_data_file("Emote", output_data, fileType='json')
    export_data_file("Emote", format_lua_table(output_data), fileType='lua')
    print("表情(Emote)数据处理完成喵！")
