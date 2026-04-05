# modules/generate_badge.py
import os
from utils.common import load_json_file, format_lua_table, export_data_file


def export_badge_data():
    print("开始处理徽章(Badge)数据喵...")
    custom_keys = {
        "ID": "id",
        "Name": "name",
        "Quality": "quality",
        "File": "file",
        "Get": "get",
        "Desc_string": "desc",
    }

    Badge_data = load_json_file("Badge")
    if not Badge_data:
        return

    output_data = []
    for item in Badge_data:
        for row in item["Rows"].values():
            Badge_ID = row["Id"]

            gain_param2 = row.get("GainParam2", {})
            raw_get_str = gain_param2.get("LocalizedString", "")
            gain_param2_value = [raw_get_str] if raw_get_str else []

            asset_path_name = row["IconItem"].get("AssetPathName", "")
            tail_number = asset_path_name.split("_")[-1].split(".")[0]

            Desc_string = row["Desc"].get(
                "LocalizedString", "").replace("\n", "")

            extracted_data = {
                "ID": Badge_ID,
                "Name": row["Name"].get("LocalizedString", ""),
                "Quality": row["Quality"],
                "File": f"勋章_{tail_number}.png",
                "Get": gain_param2_value,
                "Desc_string": Desc_string,
            }
            custom_data = {
                custom_keys[key]: value for key, value in extracted_data.items()
            }

            output_data.append(custom_data)
    export_data_file("Badge", output_data, fileType='json')
    export_data_file("Badge", format_lua_table(output_data), fileType='lua')

    print("徽章(Badge)数据处理完成喵！")
