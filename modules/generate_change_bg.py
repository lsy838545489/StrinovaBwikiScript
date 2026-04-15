# modules/generate_change_bg.py
import os
from utils.common import load_json_file, format_lua_table, export_data_file


def export_change_background_data():
    print("开始处理房间背景(ChangeBackground)数据喵...")
    custom_keys = {
        "ID": "id",
        "Name": "name",
        "Quality": "quality",
        "Get": "get",
        "Desc": "desc",
    }

    ChangeBackground_data = load_json_file("Item")
    if not ChangeBackground_data:
        return

    output_data = []
    for item in ChangeBackground_data:
        for row in item["Rows"].values():
            Items_ID = row["Id"]
            if not (93000 < Items_ID < 93999):
                continue

            gain_param2 = row.get("GainParam2", {})
            raw_get_str = gain_param2.get("LocalizedString", "")
            gain_param2_value = [raw_get_str] if raw_get_str else []

            item_localized_string = (
                row["Desc"].get("LocalizedString", "").replace("\n", "<br />")
            )

            extracted_data = {
                "ID": Items_ID,
                "Name": row["Name"].get("LocalizedString", ""),
                "Quality": row["Quality"],
                "Get": gain_param2_value,
                "Desc": item_localized_string,
            }

            # 将提取的数据映射到自定义键
            custom_data = {
                custom_keys[key]: value for key, value in extracted_data.items()
            }
            output_data.append(custom_data)

    export_data_file("ChangeBg", output_data, fileType='json')
    export_data_file("ChangeBg", format_lua_table(output_data), fileType='lua')
    print("房间背景(ChangeBackground)数据处理完成喵！")
